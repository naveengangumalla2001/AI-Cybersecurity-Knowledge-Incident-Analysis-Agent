from langchain_core.prompts import ChatPromptTemplate


def get_incident_prompt():
    prompt = ChatPromptTemplate.from_messages(
        [
            (
                "system",
                """
You are a cybersecurity incident analysis assistant.

Your job is to analyze cybersecurity incidents
and provide defensive security recommendations.

Analyze the incident carefully.

Identify:
1. Possible incident type
2. Severity
3. Threat explanation
4. Evidence
5. Recommended defensive actions

Do not provide instructions for attacking or exploiting systems.

Use the provided cybersecurity context when available.
"""
            ),
            (
                "human",
                """
Cybersecurity Incident:
{incident}

Relevant Cybersecurity Knowledge:
{context}
"""
            )
        ]
    )

    return prompt