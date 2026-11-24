# ai-link-analysis

## Windows VS Code setup
Open this folder in VS Code (File > Open Folder). Open Terminal > New Terminal.

```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
pip install -r requirements.txt
Copy-Item .env.example .env
```
Fill `.env` with your API credentials. Run:
```powershell
python -m uvicorn app.main:app --host 127.0.0.1 --port 4000
```
Open http://localhost:4000/docs; expand POST /link-analysis, click Try it out, enter `{"url":"https://example.com"}`, click Execute.

Run `python -m pytest -q` in a second terminal. Real integration calls need credentials and network access. No live results or latency benchmarks are claimed.

## Architecture
`app/main.py` routes requests; `schemas.py` defines validation; `config.py` loads secrets; `services/` holds processing and LLM integration; `utils/` holds deterministic validation; `tests/` contains smoke tests.

## Deployment
Push this folder to its own public GitHub repository, excluding .env. On Render create a Python web service linked to the repository. Build: `pip install -r requirements.txt`. Start: `uvicorn app.main:app --host 0.0.0.0 --port $PORT`. Add environment variables in the dashboard. Share /docs and test POST /link-analysis. Protect public demos with access controls and provider spending limits before exposing paid APIs.

## Limitations
Single HTML page; no JavaScript rendering. Competitors are explicitly unverified hypotheses. Public DNS addresses are checked and pinned; use isolated egress and rate limits for production. Fewer than five services may be returned when evidence is insufficient.

## Model Research and Recommendation

Recommended Provider: Google Gemini

Recommended Model: Gemini 3.5 Flash-Lite

Model ID: gemini-3.5-flash-lite

Reasons for selection:

- Free-tier API availability, subject to quotas.
- Cost-effective website content analysis.
- Support for structured JSON output.
- Compatible with Pydantic validation.
- Optimized for low-latency processing.
- Configurable model selection through environment variables.

The application records actual LLM response time
and token usage in the terminal logs.

Accuracy and performance must be evaluated using
actual website analysis test cases.

Competitor suggestions are AI-generated and
explicitly marked as unverified.

## Submission evidence
Add your actual Swagger screenshots, successful responses and error tests after running. Never commit API credentials or sensitive data.

## LLM Model Research and Cost Optimization

This application uses Google Gemini 3.5 Flash-Lite
for AI-powered website content analysis.

A detailed comparison of Google Gemini, OpenAI and
Anthropic models, including API pricing, accuracy
evaluation, response speed, cost optimization and
fallback strategies, is available below.

[View Complete LLM Model Research](MODEL_RESEARCH.md)