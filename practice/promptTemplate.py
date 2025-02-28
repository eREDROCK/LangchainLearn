from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.messages import AIMessage, HumanMessage, SystemMessage
from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder
import os

api_key = os.getenv("GOOGLE_API_KEY")
if not api_key:
    raise ValueError("Please set the GOOGLE_API_KEY environment variable")

model = ChatGoogleGenerativeAI(
    model="gemini-2.0-flash",
    temperature=0,
)

prompt = ChatPromptTemplate.from_messages(
    [
        ("system", "あなたは最強のハンターです．"),
        MessagesPlaceholder("chat_history", optional=True),
        ("human", "{input}"),
    ]
)

prompt_value = prompt.invoke(
    {
        "chat_history": [
            HumanMessage("最強のハンターになりたいんだ．"),
            AIMessage("どうして？"),
        ],
        "input": "最強を目指すことに意味なんてあるか？",
    }
)

print(model.invoke(prompt_value).content)