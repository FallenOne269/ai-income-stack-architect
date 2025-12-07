from typing import List, Optional
from pydantic import BaseModel, Field

class StackProfile(BaseModel):
    user_summary: str
    chosen_stacks: List[dict]
    disqualified_stacks: List[dict] = []

class NichePlan(BaseModel):
    stack_type: str
    primary_niche: str
    content_angles: List[str]
    keyword_clusters: List[dict]
    offer: dict
    landing_page: dict

class ExecutionPlan(BaseModel):
    stack_type: str
    primary_niche: str
    weeks: List[dict]
    notes: Optional[str] = None

class ToolBundle(BaseModel):
    stack_type: str
    monthly_budget_cap: float
    recommended_tools: List[dict]
    total_monthly_cost_estimate: Optional[float] = None
    notes: Optional[str] = None

class Blueprint(BaseModel):
    title: str
    subtitle: str
    user_summary: str
    stack_overview: dict
    offer_and_positioning: dict
    execution_plan: dict
    tool_bundle_summary: dict
    subscription_call_to_action: dict
