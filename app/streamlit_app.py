import streamlit as st
import requests


# --------------------------------------------------
# Page Configuration
# --------------------------------------------------

st.set_page_config(
    page_title="AI Cybersecurity Incident Analysis Agent",
    page_icon="🛡️",
    layout="wide"
)


# --------------------------------------------------
# Title
# --------------------------------------------------

st.title("🛡️ AI Cybersecurity Incident Analysis Agent")

st.write(
    "Analyze cybersecurity incidents using "
    "RAG, LangGraph, Gemini, and Pydantic."
)


# --------------------------------------------------
# FastAPI URL
# --------------------------------------------------

API_URL = "http://127.0.0.1:8000/analyze"


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

                # Send request to FastAPI
                response = requests.post(
                    API_URL,
                    json={
                        "incident": incident
                    },
                    timeout=120
                )

                # --------------------------------------------------
                # Successful Response
                # --------------------------------------------------

                if response.status_code == 200:

                    result = response.json()

                    st.success(
                        "Incident analysis completed successfully!"
                    )

                    # --------------------------------------------------
                    # Incident Type
                    # --------------------------------------------------

                    st.subheader("🚨 Incident Type")

                    st.write(
                        result.get(
                            "incident_type",
                            "Not available"
                        )
                    )

                    # --------------------------------------------------
                    # Severity
                    # --------------------------------------------------

                    st.subheader("⚠️ Severity")

                    severity = result.get(
                        "severity",
                        "Not available"
                    )

                    st.write(severity)

                    # --------------------------------------------------
                    # Threat Explanation
                    # --------------------------------------------------

                    st.subheader("🔎 Threat Explanation")

                    st.write(
                        result.get(
                            "threat_explanation",
                            "Not available"
                        )
                    )

                    # --------------------------------------------------
                    # Evidence
                    # --------------------------------------------------

                    st.subheader("📋 Evidence")

                    evidence = result.get(
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
                    # Recommended Actions
                    # --------------------------------------------------

                    st.subheader(
                        "🛡️ Recommended Defensive Actions"
                    )

                    actions = result.get(
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
                    # Raw JSON
                    # --------------------------------------------------

                    with st.expander(
                        "View Structured JSON Output"
                    ):

                        st.json(result)

                # --------------------------------------------------
                # Quota Error
                # --------------------------------------------------

                elif response.status_code == 429:

                    st.error(
                        "Gemini API quota exceeded. "
                        "Please try again after the quota resets."
                    )

                # --------------------------------------------------
                # Gemini Service Error
                # --------------------------------------------------

                elif response.status_code == 503:

                    st.error(
                        "Gemini service is temporarily "
                        "unavailable. Please try again later."
                    )

                # --------------------------------------------------
                # Bad Request
                # --------------------------------------------------

                elif response.status_code == 400:

                    st.warning(
                        "Incident description cannot be empty."
                    )

                # --------------------------------------------------
                # Other API Errors
                # --------------------------------------------------

                else:

                    try:

                        error = response.json()

                        st.error(
                            error.get(
                                "detail",
                                "An error occurred."
                            )
                        )

                    except Exception:

                        st.error(
                            f"API Error: {response.status_code}"
                        )

            # --------------------------------------------------
            # FastAPI Connection Error
            # --------------------------------------------------

            except requests.exceptions.ConnectionError:

                st.error(
                    "Could not connect to FastAPI. "
                    "Please make sure the FastAPI server is running."
                )

            # --------------------------------------------------
            # Timeout Error
            # --------------------------------------------------

            except requests.exceptions.Timeout:

                st.error(
                    "The request took too long. "
                    "Please try again."
                )

            # --------------------------------------------------
            # Unexpected Error
            # --------------------------------------------------

            except Exception as e:

                st.error(
                    f"Unexpected error: {str(e)}"
                )


# --------------------------------------------------
# Footer
# --------------------------------------------------

st.divider()

st.caption(
    "AI Cybersecurity Incident Analysis Agent | "
    "RAG + LangGraph + Gemini + FastAPI"
)