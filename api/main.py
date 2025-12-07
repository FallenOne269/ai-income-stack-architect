from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from fastapi.responses import FileResponse
import os

app = FastAPI()

@app.get("/")
async def root():
    return {"status": "ok", "message": "AI Income Stack Architect API"}

@app.post("/api/intake")
async def intake(user_profile: dict):
    """Placeholder intake endpoint. Wire to LangGraph orchestrator later."""
    return {
        "success": True,
        "blueprint": {
            "title": "Your Custom Blueprint",
            "subtitle": "Validated side hustle blueprint",
            "stack_type": "email_list_digital_products",
            "primary_niche": f"Your chosen niche",
            "validation_summary": "Blueprint generation in progress. Check back soon.",
            "execution_plan": {
                "overview": "12-week plan to first revenue",
                "weeks": []
            },
            "tool_bundle_summary": {
                "total_monthly_cost_estimate": 0,
                "tools": []
            },
            "subscription_call_to_action": {
                "headline": "Scale with Optimization",
                "body": "Monthly A/B tests, content refresh, trend briefings"
            }
        },
        "metrics": [],
        "errors": []
    }
