from flask import Flask, request, jsonify
from langchain_groq import ChatGroq
from langchain_core.prompts import ChatPromptTemplate
import requests 

app = Flask(__name__)


@app.route('/chat', methods=['POST'])
def chat_with_llm():
    data = request.json
    print(data)
    prompt_message = data.get('prompt')

    try:
        GROQ_API_KEY = "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"
        chat = ChatGroq(temperature=0, model_name="llama3-8b-8192", groq_api_key=GROQ_API_KEY)
        system = """You are a helpful assistant. You know only what is told you to do. You don't have any other knowledge
        about world at all. 
        Here is what you know: 
                If user asks you to retrieve all arangements, return message all_arangements.
                If user asks you to book an arangement, retrieve message book_arangement.
                If user asks you to generate travel plan, you need to be provided with travelling location and number of days. Your task is to return to the user
                plan in json format filled with day(from 1 to number of days user provided to you), time, activity in that time, location of activity (f.e. restaurant dinner place, museums,hotels) and price. You don't need
                to be provided with users preferences to generate this plan, only location and no of days. Do not send any additional text except array of json objects, f.e.
                Keys of json: day, time, activity, location, price.
        """
        human = "{text}"
        prompt = ChatPromptTemplate.from_messages([("system", system), ("human", human),("placeholder","{agent_scratchpad}")])
        chain = prompt | chat 
        response = chain.invoke({"text":prompt_message})
        print(response) #.content
        return jsonify({'response': response.content})
    except Exception as e:
        return jsonify({'error': str(e)}), 500


if __name__ == '__main__':
    app.run(port=5000)
