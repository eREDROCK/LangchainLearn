from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser, PydanticOutputParser
from pydantic import BaseModel, Field
import os

api_key = os.getenv("GOOGLE_API_KEY")
if not api_key:
    raise ValueError("Please set the GOOGLE_API_KEY environment variable")

model = ChatGoogleGenerativeAI(
    model="gemini-2.0-flash",
    temperature=0,
)

class GameIdea(BaseModel):
    title: list[str] = Field(description="テーマから連想されるゲームのタイトル")
    description: list[str] = Field(description="ゲームの概要")

output_parser = PydanticOutputParser(pydantic_object = GameIdea)

prompt = ChatPromptTemplate.from_messages(
    [
        ("system", "ユーザーが入力したテーマに沿ったゲームの企画を複数考えてください．\n\n{format_instructions}"),
        ("human","{theme}"),
    ]
)

prompt_with_format_instructions = prompt.partial(
    format_instructions = output_parser.get_format_instructions()
)

# chain = prompt_with_format_instructions | model | output_parser
chain = prompt_with_format_instructions | model.with_structured_output(GameIdea)
game_idea =chain.invoke({"theme": "せん"})
print(type(game_idea))
print(game_idea)