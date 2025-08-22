from dotenv import load_dotenv
from langchain_groq import ChatGroq
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
import os

load_dotenv()
api_key = os.getenv("GOOGLE_API_KEY")
## Simple one-line prompt
prompt = PromptTemplate.from_template("{question}")
llm = ChatGroq(
    model="llama-3.1-8b-instant",
    temperature=0,
    timeout=None,
    max_retries=2,
    # other params...
)
parser = StrOutputParser()

## Chain: Prompt->Model->Parser
chain = prompt | llm | parser

## Run it
result = chain.invoke({"question": "what is th capital of India?"})
print(result)
