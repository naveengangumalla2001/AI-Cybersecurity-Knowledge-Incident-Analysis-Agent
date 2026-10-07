from typing import TypedDict


class AgentState(TypedDict):

    incident: str

    context: str

    analysis: dict