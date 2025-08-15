from langgraph.graph import StateGraph,START,END
from typing import TypedDict,Annotated
from langchain_core.messages import BaseMessage
from langchain_google_genai import ChatGoogleGenerativeAI
from langgraph.graph.message import add_messages
from dotenv import load_dotenv
from langgraph.checkpoint.sqlite import SqliteSaver
from langchain_core.messages import HumanMessage
import os
import sqlite3

load_dotenv()

api_key=os.getenv('GOOGLE_API_KEY')

llm = ChatGoogleGenerativeAI(model="gemini-2.5-pro")

class ChatState(TypedDict):
    messages: Annotated[list[BaseMessage],add_messages]


def chat_nodes(state: ChatState):
    messages=state['messages']
    response=llm.invoke(messages)
    return {'messages':response}

conn=sqlite3.connect(database="chatbot.db",check_same_thread=False)

## Checkpointer
checkpointer=SqliteSaver(conn=conn)

graph=StateGraph(ChatState)
graph.add_node('chat_node',chat_nodes)
graph.add_edge(START,'chat_node')
graph.add_edge('chat_node',END)

chatbot=graph.compile(checkpointer=checkpointer)

def retrieve_all_threads():
    all_threads=set()
    for checkpoints in (checkpointer.list(None)):
        all_threads.add(checkpoints.config['configurable']['thread_id'])
    return (list(all_threads))