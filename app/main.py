from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

from app.agent.graph import build_graph


# --------------------------------------------------
# FastAPI Application
# --------------------------------------------------

app = FastAPI(
    title="AI Cybersecurity Incident Analysis Agent",
    description="AI-powered cybersecurity incident analysis using RAG and LangGraph",
    version="1.0.0"
)


# --------------------------------------------------
# Request Schema
# --------------------------------------------------

class IncidentRequest(BaseModel):
    incident: str


# --------------------------------------------------
# Build LangGraph Agent
# --------------------------------------------------

agent = build_graph()


# --------------------------------------------------
# Home Endpoint
# --------------------------------------------------

@app.get("/")
def home():

    return {
        "message": "AI Cybersecurity Incident Analysis Agent is running"
    }


# --------------------------------------------------
# Incident Analysis Endpoint
# --------------------------------------------------

@app.post("/analyze")
def analyze(request: IncidentRequest):

    # Check for empty incident description
    if not request.incident.strip():

        raise HTTPException(
            status_code=400,
            detail="Incident description cannot be empty."
        )

    # Initial LangGraph state
    state = {
        "incident": request.incident,
        "context": "",
        "analysis": {}
    }

    try:

        # Run LangGraph agent
        result = agent.invoke(state)

        # Return final structured analysis
        return result["analysis"]

    except Exception as e:

        # Print complete error in terminal
        print("\n========== ERROR ==========")
        print("Error Type:", type(e))
        print("Error Message:", str(e))
        print("===========================\n")

        error_message = str(e)

        # --------------------------------------------------
        # Gemini Quota / Rate Limit Error
        # --------------------------------------------------

        if (
            "429" in error_message
            or "RESOURCE_EXHAUSTED" in error_message
        ):

            raise HTTPException(
                status_code=429,
                detail="Gemini API quota exceeded. Please try again later."
            )

        # --------------------------------------------------
        # Gemini Temporary Service Error
        # --------------------------------------------------

        elif (
            "503" in error_message
            or "UNAVAILABLE" in error_message
        ):

            raise HTTPException(
                status_code=503,
                detail="Gemini service is temporarily unavailable. Please try again later."
            )

        # --------------------------------------------------
        # Other Errors
        # --------------------------------------------------

        else:

            raise HTTPException(
                status_code=500,
                detail=f"Incident analysis failed: {error_message}"
            )