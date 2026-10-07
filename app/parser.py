from pydantic import BaseModel, Field


class IncidentAnalysis(BaseModel):
    incident_type: str = Field(
        description="Possible type of cybersecurity incident"
    )

    severity: str = Field(
        description="Severity level of the incident"
    )

    threat_explanation: str = Field(
        description="Explanation of the potential threat"
    )

    evidence: list[str] = Field(
        description="Evidence identified from the incident"
    )

    recommended_actions: list[str] = Field(
        description="Recommended defensive actions"
    )