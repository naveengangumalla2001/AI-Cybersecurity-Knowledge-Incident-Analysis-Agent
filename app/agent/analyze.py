from app.agent.state import AgentState
from app.model import get_model
from app.prompt import get_incident_prompt


def analyze_incident(state: AgentState):

    incident = state["incident"]
    context = state["context"]

    model = get_model()
    prompt = get_incident_prompt()

    chain = prompt | model

    result = chain.invoke(
        {
            "incident": incident,
            "context": context
        }
    )

    return {
        "analysis": result.model_dump()
    }