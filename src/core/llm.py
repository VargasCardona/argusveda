from langchain_openai import ChatOpenAI
from dotenv import load_dotenv
import os

load_dotenv()

llm = ChatOpenAI(
    openai_api_key=os.getenv("API_KEY"),
    openai_api_base="https://opencode.ai/zen/v1",
    model="big-pickle",
)
