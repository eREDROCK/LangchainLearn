from langchain_google_genai import ChatGoogleGenerativeAI
import os

api_key = os.getenv("GOOGLE_API_KEY")
if not api_key:
    raise ValueError("Please set the GOOGLE_API_KEY environment variable")

model = ChatGoogleGenerativeAI(
    api_key=api_key,
    model="gemini-2.0-flash",
    temperature=0,
    max_tokens=None,
    timeout=None,
    max_retries=2,
)

output = model.invoke("Hello, who are you?")

print(output)