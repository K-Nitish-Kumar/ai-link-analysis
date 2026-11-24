from pydantic import BaseModel, HttpUrl, Field
from typing import Literal
class Request(BaseModel):
    url: HttpUrl
class Brand(BaseModel):
    name: str
    category: str
    summary: str
class Competitor(BaseModel):
    name: str
    strengths: list[str]
    weaknesses: list[str]
    evidence_status: Literal['AI suggestion - unverified']
class CompetitorAnalysis(BaseModel):
    brand_overview: str
    products_services: list[str]
    competitors: list[Competitor]
    strengths: list[str]
    opportunities: list[str]
class Query(BaseModel):
    query: str
    platforms: list[Literal['Google','Facebook','Instagram','LinkedIn','X']]
    intent: str
    business_relevance: str
    target_audience: str
class SEO(BaseModel):
    primary_keyword: str
    secondary_keywords: list[str]
    long_tail_keywords: list[str]
    business_keywords: list[str]
    recommended_title: str
    title_structure: str
    meta_description: str
    supporting_content: list[str]
class Service(BaseModel):
    name: str
    description: str
    target_industry: str
    target_customer: str
    main_benefit: str
    evidence_status: Literal['website','inferred']
class Audience(BaseModel):
    primary_audience: list[str]
    secondary_audience: list[str]
    industries: list[str]
    business_types: list[str]
    customer_profiles: list[str]
    geographic_focus: str | None
    customer_needs: list[str]
    interests: list[str]
    marketing_segments: list[str]
class Analysis(BaseModel):
    competitor_analysis: CompetitorAnalysis
    target_search_queries: list[Query] = Field(min_length=5,max_length=5)
    seo_improvements: SEO
    top_services: list[Service] = Field(max_length=5)
    target_audience: Audience
class ModelOutput(BaseModel):
    brand: Brand
    analysis: Analysis
class Response(ModelOutput):
    success: bool
    website: str
    sources: list[str]
