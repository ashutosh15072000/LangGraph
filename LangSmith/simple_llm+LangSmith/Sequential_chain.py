from langchain_groq import ChatGroq
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
import os

os.environ['LANGCHAIN_PROJECT'] = "Sequential LLM App"

load_dotenv()

llm = ChatGroq(
    model="llama-3.1-8b-instant",
    temperature=0.5,
    timeout=None,
    max_retries=2,
    # other params...
)


prompt1 = PromptTemplate(
    template = "Generate a detailed reports on {topic}",
    input_variables = ['topic']
)

prompt2 = PromptTemplate(
    template = "Generate a 5 pointer summary from the following text /n {text}",
    input_variables = ['text'] 
) 

parser = StrOutputParser()

chain = prompt1 | llm | parser | prompt2 | llm | parser

config = {
    "run_name": "Sequential Chain",
    'tags' : {'llm app','report generation','summarization'},
    'metadata':{'model':'llama-3.1-8b-instant','temperature':0.7,'parser':'stroutputparser'}
}

result = chain.invoke({"topic":"Unempolyment in india"},config=config)

print(result)
