import os

from dotenv import load_dotenv
from langchain_google_genai import ChatGoogleGenerativeAI

from app.parser import IncidentAnalysis


load_dotenv()


def get_model():

    api_key = os.getenv("GOOGLE_API_KEY")

    if not api_key:
        raise ValueError(
            "GOOGLE_API_KEY was not found. "
            "Please check your .env file."
        )

    model = ChatGoogleGenerativeAI(
        model="gemini-3.6-flash",
        google_api_key=api_key
    )

    return model.with_structured_output(IncidentAnalysis)