from langchain_google_genai import ChatGoogleGenerativeAI
from models.profile import Profile
from config import GOOGLE_API_KEY


class ProfileAnalyzer:

    def __init__(self):
        self.llm = ChatGoogleGenerativeAI(
            model="gemini-3.8-flash",
            google_api_key=GOOGLE_API_KEY
        )

    def analyze(self, profile_text: str) -> Profile:

        structured_llm = self.llm.with_structured_output(Profile)

        prompt = f"""
You are an expert professional profile analyst.

Analyze the following user-provided professional profile.

Extract ONLY information explicitly present in the source.

Do not invent:
- qualifications
- employers
- dates
- skills
- achievements
- certifications
- responsibilities

If information is unavailable, leave the field empty.

PROFILE:

{profile_text}
"""

        result = structured_llm.invoke(prompt)

        return result