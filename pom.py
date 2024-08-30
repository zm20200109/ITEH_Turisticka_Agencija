from flask import Flask, request, jsonify
from langchain_groq import ChatGroq
from langchain_core.prompts import ChatPromptTemplate
import requests 
from langchain_core.tools import tool, Tool
from langchain.agents import AgentExecutor, create_tool_calling_agent



GROQ_API_KEY = "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"
chat = ChatGroq(temperature=0, model_name="llama3-8b-8192", groq_api_key=GROQ_API_KEY)
#llm_with_tools = chat.bind_tools([get_all_arangements])
system = """You are a helpful assistant. If user asks you to retrieve all arangements, return message all_arangements. 
       If user wants to book an arangement, retrieve book_arangement.
        """
human = "{text}"
prompt_message="retrieve me all arangements."
prompt = ChatPromptTemplate.from_messages([("system", system), ("human", human)])
chain = prompt | chat 
response = chain.invoke({"text":prompt_message})
print(response)