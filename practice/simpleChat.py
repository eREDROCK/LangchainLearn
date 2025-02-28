from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.messages import AIMessage, HumanMessage, SystemMessage
from langchain_core.prompts import PromptTemplate
import os

api_key = os.getenv("GOOGLE_API_KEY")
if not api_key:
    raise ValueError("Please set the GOOGLE_API_KEY environment variable")

model = ChatGoogleGenerativeAI(
    model="gemini-2.0-flash",
    temperature=0,
)

messages = [
    SystemMessage("あなたは最強の魔法使いのフリーレンです．"),
    HumanMessage("フリーレン様，お呼びでしょうか？"),
    AIMessage("魔法は好きか？"),
    HumanMessage("ほどほどでございます．"),
]
output = model.invoke(messages)

for chunk in model.stream(messages):
    print(chunk.content, end="", flush=True)