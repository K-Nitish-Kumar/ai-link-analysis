
import json
import time
import logging

from google import genai
from google.genai import types, errors

from fastapi import HTTPException
from pydantic import ValidationError

from app.config import GEMINI_API_KEY, GEMINI_MODEL


logger = logging.getLogger(__name__)


def prepare_schema(value):
    """
    Convert single-value constants into enums
    for Gemini JSON schema compatibility.
    """

    if isinstance(value, dict):

        result = {}

        for key, item in value.items():

            if key == "const":
                result["enum"] = [item]
            else:
                result[key] = prepare_schema(item)

        return result

    if isinstance(value, list):
        return [prepare_schema(item) for item in value]

    return value


def generate(schema, instruction, data):

    if not GEMINI_API_KEY:
        raise HTTPException(
            status_code=503,
            detail="Configure GEMINI_API_KEY in .env"
        )

    start = time.monotonic()

    try:

        with genai.Client(
    api_key=GEMINI_API_KEY,
    http_options=types.HttpOptions(
        timeout=90000,
        retry_options=types.HttpRetryOptions(
            attempts=4,
            initial_delay=2.0,
            max_delay=15.0,
            exp_base=2.0,
            http_status_codes=[500, 502, 503, 504]
        )
    )
) as client:

            response = client.models.generate_content(

                model=GEMINI_MODEL,

                contents=json.dumps(
                    data,
                    ensure_ascii=False
                ),

                config=types.GenerateContentConfig(

                    system_instruction=instruction,

                    response_mime_type="application/json",

                    response_json_schema=prepare_schema(
                        schema.model_json_schema()
                    ),

                    max_output_tokens=8192

                )

            )

        if not response.text:

            raise HTTPException(
                status_code=502,
                detail="Gemini returned an empty response"
            )

        result = schema.model_validate_json(
            response.text
        )

        elapsed = time.monotonic() - start

        logger.info(
            "Gemini model=%s latency=%.2fs usage=%s",
            GEMINI_MODEL,
            elapsed,
            response.usage_metadata
        )

        return result

    except errors.APIError as exc:

        code = getattr(exc, "code", None)

        logger.error(
            "Gemini API failed: status=%s",
            code
        )

        if code == 429:

            raise HTTPException(
                status_code=429,
                detail=(
                    "Gemini API quota or rate limit exceeded. "
                    "Check your Google AI Studio limits."
                )
            ) from exc

        if code in (401, 403):

            raise HTTPException(
                status_code=502,
                detail="Gemini API key or permission error"
            ) from exc
        if code == 503:

            raise HTTPException(
                status_code=503,
                detail=(
                    "Gemini service is temporarily unavailable. "
                    "Automatic retries were unsuccessful. "
                    "Please retry later."
                ),
                headers={"Retry-After": "30"}
            ) from exc
        if code == 404:

            raise HTTPException(
                status_code=502,
                detail="Gemini model not found or unavailable"
            ) from exc

        raise HTTPException(
            status_code=502,
            detail=f"Gemini API request failed: {code}"
        ) from exc

    except (ValidationError, ValueError) as exc:

        logger.error(
            "Gemini response validation failed: %s",
            type(exc).__name__
        )

        raise HTTPException(
            status_code=502,
            detail="Gemini returned invalid structured JSON"
        ) from exc

    except HTTPException:
        raise

    except Exception as exc:

        logger.error(
            "Gemini integration failed: %s",
            type(exc).__name__
        )

        raise HTTPException(
            status_code=502,
            detail="Gemini integration failed"
        ) from exc
