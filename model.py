import google.generativeai as genai
from google.generativeai.generative_models import ChatSession
from dotenv import load_dotenv
import os
from json_parse import *

def create_response(messages:str, chat:ChatSession, safety_settings=None, generation_config=None) -> str:
    text = ""
    for message in messages:
        text += message + "\n"
    first_prompt = "Привет! Я - телеграмм бот, который собирает сообщения из чата за час и после этого отправляет их мне. Моя задача - сделать краткий пересказ всей беседы. Вот последний час нашего чата: " + text + ". Пожалуйста, сформулируйте краткий пересказ этой беседы на основе сообщений её участников."
    final_prompt = chat.send_message(first_prompt, safety_settings=safety_settings, generation_config=generation_config)

    return final_prompt.text

def genai_configure(api_key:str):
    load_dotenv()
    GOOGLE_API_KEY = os.getenv(api_key)
    genai.configure(api_key=GOOGLE_API_KEY)

def model(json_data):
    genai_configure("GOOGLE_API_KEY")
    model = genai.GenerativeModel('gemini-pro')

    config = {"max_output_tokens": 2048, "temperature": 0.4, "top_p": 1, "top_k": 32}

    safe = [
        {
            "category": "HARM_CATEGORY_HARASSMENT",
            "threshold": "BLOCK_NONE",
        },
        {
            "category": "HARM_CATEGORY_HATE_SPEECH",
            "threshold": "BLOCK_NONE",
        },
        {
            "category": "HARM_CATEGORY_SEXUALLY_EXPLICIT",
            "threshold": "BLOCK_NONE",
        },
        {
            "category": "HARM_CATEGORY_DANGEROUS_CONTENT",
            "threshold": "BLOCK_NONE",
        },
    ]
    chat = model.start_chat(history=[])
    messages, time, chat_id = get_args_json(json_data)
    response = create_response(messages, chat, safe, config)
    response_data = load_json(time, chat_id, response)
    return response_data
