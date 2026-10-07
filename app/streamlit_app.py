import sys
from pathlib import Path

import streamlit as st


# Add project root to Python path
PROJECT_ROOT = Path(__file__).resolve().parent.parent

if str(PROJECT_ROOT) not in sys.path:
    sys.path.insert(0, str(PROJECT_ROOT))


from app.agent.graph import build_graph


# --------------------------------------------------
# Page Configuration
# --------------------------------------------------

st.set_page_config(
    page_title="AI Cybersecurity Incident Analysis Agent",
    page_icon="🛡️",
    layout="wide"
)


# --------------------------------------------------
# Build LangGraph Agent
# --------------------------------------------------

agent = build_graph()


# --------------------------------------------------
# Title
# --------------------------------------------------

st.title("🛡️ AI Cybersecurity Incident Analysis Agent")

st.write(
    "Analyze cybersecurity incidents using "
    "RAG, LangGraph, Gemini, and Pydantic."
)


# --------------------------------------------------
# Incident Input
# --------------------------------------------------

st.subheader("Enter Cybersecurity Incident")

incident = st.text_area(
    "Incident Description",
    placeholder=(
        "Example: A web server received 5000 failed "
        "login attempts from multiple IP addresses "
        "within 10 minutes."
    ),
    height=180
)


# --------------------------------------------------
# Analyze Button
# --------------------------------------------------

if st.button("🔍 Analyze Incident", type="primary"):

    # Check empty input
    if not incident.strip():

        st.warning(
            "Please enter a cybersecurity incident."
        )

    else:

        with st.spinner("Analyzing incident..."):

            try:

                # --------------------------------------------------
                # Run LangGraph Agent Directly
                # --------------------------------------------------

                result = agent.invoke(
                    {
                        "incident": incident,
                        "context": "",
                        "analysis": {}
                    }
                )

                # Get final structured analysis
                analysis = result["analysis"]

                # --------------------------------------------------
                # Success Message
                # --------------------------------------------------

                st.success(
                    "Incident analysis completed successfully!"
                )

                # --------------------------------------------------
                # Incident Type
                # --------------------------------------------------

                st.subheader("🚨 Incident Type")

                st.write(
                    analysis.get(
                        "incident_type",
                        "Not available"
                    )
                )

                # --------------------------------------------------
                # Severity
                # --------------------------------------------------

                st.subheader("⚠️ Severity")

                st.write(
                    analysis.get(
                        "severity",
                        "Not available"
                    )
                )

                # --------------------------------------------------
                # Threat Explanation
                # --------------------------------------------------

                st.subheader("🔎 Threat Explanation")

                st.write(
                    analysis.get(
                        "threat_explanation",
                        "Not available"
                    )
                )

                # --------------------------------------------------
                # Evidence
                # --------------------------------------------------

                st.subheader("📋 Evidence")

                evidence = analysis.get(
                    "evidence",
                    []
                )

                if evidence:

                    for item in evidence:

                        st.markdown(
                            f"- {item}"
                        )

                else:

                    st.write(
                        "No evidence identified."
                    )

                # --------------------------------------------------
                # Recommended Defensive Actions
                # --------------------------------------------------

                st.subheader(
                    "🛡️ Recommended Defensive Actions"
                )

                actions = analysis.get(
                    "recommended_actions",
                    []
                )

                if actions:

                    for index, action in enumerate(
                        actions,
                        start=1
                    ):

                        st.markdown(
                            f"{index}. {action}"
                        )

                else:

                    st.write(
                        "No recommendations available."
                    )

                # --------------------------------------------------
                # Structured JSON
                # --------------------------------------------------

                with st.expander(
                    "View Structured JSON Output"
                ):

                    st.json(analysis)

            # --------------------------------------------------
            # Error Handling
            # --------------------------------------------------

            except Exception as e:

                error_message = str(e)

                # Print error in Streamlit Cloud logs
                print("\n========== ERROR ==========")
                print("Error Type:", type(e))
                print("Error Message:", error_message)
                print("===========================\n")

                # Gemini quota error
                if (
                    "429" in error_message
                    or "RESOURCE_EXHAUSTED" in error_message
                ):

                    st.error(
                        "Gemini API quota exceeded. "
                        "Please try again later."
                    )

                # Gemini service unavailable
                elif (
                    "503" in error_message
                    or "UNAVAILABLE" in error_message
                ):

                    st.error(
                        "Gemini service is temporarily "
                        "unavailable. Please try again later."
                    )

                # Other errors
                else:

                    st.error(
                        f"Analysis failed: {error_message}"
                    )


# --------------------------------------------------
# Footer
# --------------------------------------------------

st.divider()

st.caption(
    "AI Cybersecurity Incident Analysis Agent | "
    "RAG + LangGraph + Gemini + FastAPI"
)