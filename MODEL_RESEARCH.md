
# LLM Model Research and Recommendation

## AI-Powered Website Link Analysis API

Last Updated: 24 November 2026

---

## 1. Research Objective

The objective of this research is to identify a suitable
Large Language Model (LLM) for an AI-powered website
link analysis application.

The model should provide:

- Accurate website content understanding.
- Relevant competitor analysis.
- Business-specific SEO recommendations.
- Target search query generation.
- Service identification.
- Target audience identification.
- Reliable structured JSON output.
- Fast response times.
- Low API cost.
- Efficient processing of website content.

---

## 2. LLM Provider and Model Comparison

Three LLM providers were evaluated through their
official documentation, pricing and supported features.

| Criteria | Google Gemini | OpenAI | Anthropic |
|---|---|---|---|
| Model | Gemini 3.5 Flash-Lite | GPT-6.1 Terra | Claude Haiku 5.5 |
| Model ID | gemini-3.5-flash-lite | gpt-6.1-terra | claude-haiku-5-5 |
| Input Cost / 1M Tokens | $0.30 | $1.00 | $0.10 |
| Output Cost / 1M Tokens | $2.50 | $5.00 | $0.50 |
| Context / Input Capacity | Approximately 1M | Approximately 1M | 1M |
| Structured JSON Support | Yes | Yes | Yes |
| Speed Positioning | Low latency | Fast | Fast |
| Website Understanding | Suitable for extraction and analysis | Suitable for detailed analysis | Suitable for extraction and classification |
| Measured Accuracy | Not yet benchmarked | Not benchmarked | Not benchmarked |
| Free Tier | Available, subject to quota | Not assumed | Not assumed |
| Project Integration | Implemented | Previous integration | Proposed alternative |
| Recommendation | Primary model | Alternative | Cost-efficient alternative |

All prices are in USD per million tokens.

Prices represent standard, uncached API usage for
the estimated short-input workload.

Claude Haiku 5.5 pricing increases for prompts above
100,000 input tokens. OpenAI long-context pricing may
also differ from the standard rates.

Provider pricing and availability may change.

---

## 3. Individual Model Evaluation

### 3.1 Google Gemini 3.5 Flash-Lite

Provider: Google

Model ID: gemini-3.5-flash-lite

Advantages:

- Available free-tier API usage within eligible quotas.
- Designed for low-latency and cost-efficient processing.
- Supports structured JSON generation.
- Supports large input documents.
- Suitable for website content extraction and analysis.
- Compatible with Pydantic response validation.
- Easy integration through the Google GenAI Python SDK.

Limitations:

- Free-tier usage is subject to rate limits.
- Complex analysis may require a more capable model.
- Generated competitor information requires verification.
- JavaScript-rendered or inaccessible website content
  cannot be analyzed unless successfully extracted.

Suitability:

Recommended primary model for this application.

---

### 3.2 OpenAI GPT-6.1 Terra

Provider: OpenAI

Model ID: gpt-6.1-terra

Advantages:

- Supports structured outputs.
- Supports large context windows.
- Supports configurable reasoning effort.
- Suitable for business content understanding.
- Can generate detailed business recommendations.

Limitations:

- Higher estimated token cost for this workload.
- Requires available API quota and billing.
- Response time varies with reasoning effort.

Suitability:

A potential alternative for more complex analysis.

The project's previous GPT-4.1 mini integration
encountered an HTTP 429 API quota or rate-limit error.

The application was therefore migrated to Google Gemini.

GPT-6.1 Terra is included as a current comparison
model and has not been tested in this implementation.

---

### 3.3 Anthropic Claude Haiku 5.5

Provider: Anthropic

Model ID: claude-haiku-5-5

Advantages:

- Competitive API pricing for shorter prompts.
- Supports structured JSON outputs.
- Designed for latency-sensitive processing.
- Suitable for extraction and classification.
- Supports large context windows.

Limitations:

- Requires a separate API integration.
- Tokenization differs from other providers.
- Higher pricing applies to long-context requests.
- Project-specific accuracy requires testing.

Suitability:

A cost-efficient alternative for future evaluation
and fallback integration.

---

## 4. Final Model Selection

Recommended Provider: Google Gemini

Recommended Model: Gemini 3.5 Flash-Lite

Model ID: gemini-3.5-flash-lite

SDK: google-genai

Google Gemini was selected based on the following:

1. Free-tier availability for development and testing.
2. Low estimated API costs.
3. Structured JSON response support.
4. Compatibility with FastAPI and Pydantic.
5. Efficient processing of extracted website content.
6. Low-latency model design.
7. Straightforward Python SDK integration.
8. Configurable model selection.

Gemini is selected as the most practical model for
the current implementation.

This recommendation is based on documented capabilities,
pricing and integration requirements, rather than a
claim of superior benchmarked accuracy.

---

## 5. Estimated API Cost Analysis

### Assumed Token Consumption per Website

| Parameter | Estimated Usage |
|---|---:|
| Input Tokens | 5,000 |
| Output Tokens | 1,500 |
| Total Tokens | 6,500 |
| LLM Calls | 1 |

Output token estimates should include billable reasoning
tokens wherever applicable.

These values are estimates, not measured API usage.

### Cost Calculation Formula

Total API Cost = Input Cost + Output Cost

Input Cost = (Input Tokens / 1,000,000) x Input Price

Output Cost = (Output Tokens / 1,000,000) x Output Price

### Google Gemini 3.5 Flash-Lite

Input Cost = (5,000 / 1,000,000) x $0.30
           = $0.00150

Output Cost = (1,500 / 1,000,000) x $2.50
            = $0.00375

Total Estimated Cost per Request = $0.00525

Within eligible free-tier quotas, token charges may be $0.

### OpenAI GPT-6.1 Terra

Input Cost = (5,000 / 1,000,000) x $1.00
           = $0.00500

Output Cost = (1,500 / 1,000,000) x $5.00
            = $0.00750

Total Estimated Cost per Request = $0.01250

### Anthropic Claude Haiku 5.5

Input Cost = (5,000 / 1,000,000) x $0.10
           = $0.00050

Output Cost = (1,500 / 1,000,000) x $0.50
            = $0.00075

Total Estimated Cost per Request = $0.00125

---

## 6. Cost Comparison at Different Request Volumes

| Number of Requests | Gemini 3.5 Flash-Lite | GPT-6.1 Terra | Claude Haiku 5.5 |
|---:|---:|---:|---:|
| 1 | $0.00525 | $0.01250 | $0.00125 |
| 100 | $0.525 | $1.25 | $0.125 |
| 1,000 | $5.25 | $12.50 | $1.25 |
| 10,000 | $52.50 | $125.00 | $12.50 |
| 100,000 | $525.00 | $1,250.00 | $125.00 |

All values are hypothetical paid-tier token costs.

The comparison excludes:

- Free-tier discounts.
- Hosting infrastructure.
- Network and search API charges.
- Additional reasoning tokens beyond the estimate.
- Failed requests and retries.
- Taxes and currency conversion charges.

Identical token counts are assumed for comparison.
Actual token counts may differ between providers.

Although Claude Haiku 5.5 has lower estimated paid-token
costs for this workload, Gemini is preferred for the
current implementation due to free-tier availability
and the existing SDK integration.

---

## 7. Response Speed Evaluation

All three models are designed for relatively fast
processing, according to their provider documentation.

For the current Gemini implementation:

- Preliminary expected end-to-end response time:
  5 to 30 seconds under normal conditions.
- Configured LLM request timeout: 90 seconds.
- Actual latency depends on website accessibility,
  input size, output length, model reasoning,
  network conditions and provider load.

The above response-time range is a planning estimate,
not a measured result or provider guarantee.

The application records actual LLM response time
using Python's time.monotonic() function.

End-to-end API response time should be measured
separately because it includes website extraction
and response validation.

---

## 8. Accuracy and Quality Evaluation

Model accuracy should be evaluated using actual
website content and manually reviewed outputs.

Evaluation criteria:

1. Correct brand name and business category.
2. Accurate identification of website services.
3. Relevant competitor suggestions.
4. Relevant search queries.
5. Practical SEO improvements.
6. Appropriate target audience identification.
7. Valid structured JSON output.
8. Absence of unsupported factual claims.

Suggested evaluation rubric:

| Evaluation Criteria | Weight |
|---|---:|
| Brand and Business Understanding | 15% |
| Competitor Relevance | 20% |
| Search Query Relevance | 15% |
| SEO Recommendation Quality | 15% |
| Service Identification | 15% |
| Target Audience Accuracy | 10% |
| JSON Response Validity | 10% |
| Total | 100% |

No comparative accuracy percentage is claimed until
the models have been tested using the same websites,
prompts and evaluation criteria.

Structured JSON validity does not automatically
guarantee factual accuracy.

---

## 9. Benchmark Testing

The following websites are proposed for testing:

| Website | Business Category |
|---|---|
| https://www.python.org | Technology and Programming |
| https://www.shopify.com | E-commerce |
| https://www.kitsacitsolutions.com | IT Services |
| https://www.microsoft.com | Enterprise Technology |
| https://www.hubspot.com | CRM and Digital Marketing |

### Benchmark Results

| Website | HTTP Status | Input Tokens | Output Tokens | LLM Latency | Total Latency | Quality Score |
|---|---|---|---|---|---|---|
| python.org | Pending | Pending | Pending | Pending | Pending | Pending |
| shopify.com | Pending | Pending | Pending | Pending | Pending | Pending |
| kitsacitsolutions.com | Pending | Pending | Pending | Pending | Pending | Pending |
| microsoft.com | Pending | Pending | Pending | Pending | Pending | Pending |
| hubspot.com | Pending | Pending | Pending | Pending | Pending | Pending |

The benchmark table should be updated using actual
application execution logs and manual evaluation.

Inaccessible websites should be recorded as failed
extraction attempts rather than model accuracy failures.

---

## 10. Cost Optimization Strategies

### Implemented Strategies

#### Website Content Cleaning

BeautifulSoup removes unnecessary HTML elements
such as scripts and styles before sending website
content to the LLM.

#### Input Size Limitation

Extracted website text is limited to avoid
unnecessarily large API requests.

#### Single LLM Request

All five website analysis sections are generated
through a single LLM request.

This reduces repeated context transmission and
unnecessary API calls.

#### Structured Output Validation

Gemini receives a JSON schema and the generated
response is validated using Pydantic.

#### Configurable Output Limit

The LLM service uses a maximum output token limit
to control response size.

#### Model Configuration

The model name is configurable through environment
variables without changing the API endpoint.

#### Token Usage Monitoring

Gemini usage metadata is recorded in application logs.

This helps measure actual token consumption and
estimate API costs.

#### Latency Monitoring

The LLM execution duration is recorded to support
performance evaluation.

### Proposed Production Improvements

- Cache successful analysis results with a suitable TTL.
- Avoid repeatedly analyzing unchanged website content.
- Implement API authentication and rate limiting.
- Apply bounded retry logic for transient failures.
- Introduce provider spending limits.
- Use smaller models for simple extraction tasks.
- Route complex analysis to more capable models.
- Deduplicate repeated website content.
- Monitor JSON validation failures and factual quality.

These improvements are proposed and should not be
treated as implemented functionality.

---

## 11. Structured JSON Output

Google Gemini is configured using:

- response_mime_type: application/json
- response_json_schema: Pydantic-generated JSON schema
- max_output_tokens: 8192

The application validates the returned JSON before
sending the final response through FastAPI.

The structured response contains:

1. Competitor Analysis.
2. Top Five Target Search Queries.
3. SEO Improvements.
4. Top Services.
5. Target Audience Identification.

---

## 12. Error Handling and Reliability

The LLM integration handles:

- Missing API credentials.
- Invalid API credentials.
- API permission errors.
- API rate-limit errors.
- Unavailable models.
- Invalid JSON responses.
- Empty model responses.
- Request failures.

The website extraction layer also validates URLs
and blocks restricted network addresses to reduce
SSRF risks.
### Automatic Retry Mechanism

The Gemini integration implements automatic retries
with exponential backoff for transient API failures.

Configuration:

- Maximum attempts: 4, including the initial request.
- Initial retry delay: 2 seconds.
- Maximum retry delay: 15 seconds.
- Exponential backoff factor: 2.
- Retryable HTTP codes: 500, 502, 503 and 504.

If all attempts fail, the application returns a
meaningful error response instead of fabricated
or incomplete analysis results.
---

## 13. Factual Accuracy and Hallucination Prevention

The application analyzes actual extracted website
content rather than relying entirely on model knowledge.

The prompt instructs the LLM to:

- Ground brand details in website content.
- Avoid inventing products and services.
- Label inferred recommendations.
- Avoid fabricated search volumes.
- Mark competitor suggestions as unverified.

The current implementation does not independently
verify competitor information using a search API.

Competitor suggestions must therefore be treated as
AI-generated recommendations rather than confirmed
market research.

---

## 14. Fallback Model Strategy

Primary Model:

Google Gemini 3.5 Flash-Lite

Proposed Fallback Model:

Anthropic Claude Haiku 5.5

Additional Alternative:

OpenAI GPT-6.1 Terra

For production deployment, a provider-independent
LLM service can route requests to an alternative
provider when the primary provider is unavailable.

Fallback integration would require separate API
credentials, SDK configuration and schema testing.

Automatic cross-provider fallback is not implemented
in the current version.

---

## 15. Environment Configuration

The application uses the following environment variables:

GEMINI_API_KEY=your_api_key
GEMINI_MODEL=gemini-3.5-flash-lite

Actual API credentials are stored securely in the
local .env file and excluded from GitHub using
.gitignore.

---

## 16. Final Recommendation

| Parameter | Recommendation |
|---|---|
| LLM Provider | Google Gemini |
| Model | Gemini 3.5 Flash-Lite |
| Model ID | gemini-3.5-flash-lite |
| Estimated Input Tokens | 5,000 |
| Estimated Output Tokens | 1,500 |
| Estimated Paid Cost per Analysis | $0.00525 |
| Eligible Free-Tier Token Cost | $0 within quotas |
| Expected End-to-End Response Time | 5-30 seconds, unmeasured estimate |
| Structured JSON | Supported |
| Output Validation | Pydantic |
| Fallback Model | Claude Haiku 5.5, proposed |
| Integration Status | Gemini implemented |

Google Gemini provides a practical balance between
development accessibility, response generation speed,
structured output capabilities and API cost for
the website link analysis application.

Production-level model selection should be finalized
after measuring actual latency, token usage, output
quality and operational reliability.

---

## 17. Official References

1. Google Gemini API Pricing
   https://ai.google.dev/gemini-api/docs/pricing

2. Google Gemini 3.5 Flash-Lite Model Documentation
   https://aistudio.google.com/docs/models/gemini-3.5-flash-lite

3. Google Gemini Structured Output Documentation
   https://ai.google.dev/gemini-api/docs/structured-output

4. Google Gemini API Rate Limits
   https://ai.google.dev/gemini-api/docs/rate-limits

5. OpenAI API Pricing
   https://developers.openai.com/api/docs/pricing

6. OpenAI GPT-6.1 Terra Documentation
   https://developers.openai.com/api/docs/models/gpt-6.1-terra

7. Anthropic Claude Haiku 5.5 Documentation
   https://platform.claude.com/docs/en/models/haiku-5-5/overview

8. Anthropic Structured Output Documentation
   https://platform.claude.com/docs/en/build-with-claude/structured-outputs

9. Google GenAI Python SDK
   https://github.com/googleapis/python-genai
