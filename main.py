from langchain_openai import ChatOpenAI
from langchain_core.prompts import ChatPromptTemplate
from dotenv import load_dotenv
import os

load_dotenv()

llm = ChatOpenAI(
    openai_api_key=os.getenv("API_KEY"),
    openai_api_base="https://opencode.ai/zen/v1",
    model="big-pickle"
)

prompt = ChatPromptTemplate.from_template(
    "Responde de forma corta: {pregunta}"
)

chain = prompt | llm

respuesta = chain.invoke({
    "pregunta": "¿Qué es LangChain?"
})

print(respuesta.content)
