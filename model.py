import google.generativeai as genai
from google.generativeai.generative_models import ChatSession
from dotenv import load_dotenv
import os
from json_parse import *

def model(json_data: dict) -> dict:
    """
    Process JSON data and generate a response using GenAI model.

    :param json_data: JSON data to be processed.
    :type json_data: dict
    :return: Response data.
    :rtype: dict
    """

    load_dotenv()
    GOOGLE_API_KEY = os.getenv("GOOGLE_API_KEY")
    genai.configure(api_key=GOOGLE_API_KEY)

    model = genai.GenerativeModel('gemini-pro')
    config, safe = get_configs()
    messages, time, chat_id = get_args_json(json_data)
    chat = model.start_chat(history=[])
    response = create_response(messages, chat, safe, config)
    response_data = create_json(time, chat_id, response)
    return response_data

def create_response(messages: str, chat: ChatSession, safety_settings: dict = None, generation_config: dict = None) -> str:
    """
    Create a response based on messages from a chat session.

    :param messages: List of messages from the chat session.
    :type messages: List[str]
    :param chat: Chat session object.
    :type chat: ChatSession
    :param safety_settings: Safety settings for message generation, defaults to None.
    :type safety_settings: Optional[Dict]
    :param generation_config: Generation configuration settings, defaults to None.
    :type generation_config: Optional[Dict]
    :return: Generated response text.
    :rtype: str
    """
    text = ""
    for message in messages:
        text += message + "\n"

    prompt = "Привет! Я - телеграмм бот, который собирает сообщения из чата за определённый промежуток времени и после этого отправляет их мне. Моя задача - сделать краткий пересказ всей беседы. Вот сообщения из нашего нашего чата: " + text + ". Пожалуйста, сформулируйте краткий пересказ этой беседы на основе обсуждений её участников. Желательно подмечать моменты вызвавшие бурную реакцию либо обсуждения в чате. Также важно сформулировать ответ ёмким, то есть нужно выделить самые важные моменты беседы."
    
    response = chat.send_message(prompt, safety_settings=safety_settings, generation_config=generation_config)

    return response.text

def get_configs() -> tuple[dict[str, any], list[dict[str, str]]]:
    """
    Get configurations for the model.

    :return: A tuple containing a configuration dictionary and a list of safe settings.
    :rtype: Tuple[Dict[str, Any], List[Dict[str, str]]]
    """

    config = {"max_output_tokens": 2048, "temperature": 0.4, "top_p": 1, "top_k": 32}
    safe = [
        {"category": "HARM_CATEGORY_HARASSMENT", "threshold": "BLOCK_NONE",},
        {"category": "HARM_CATEGORY_HATE_SPEECH","threshold": "BLOCK_NONE",},
        {"category": "HARM_CATEGORY_SEXUALLY_EXPLICIT","threshold": "BLOCK_NONE",},
        {"category": "HARM_CATEGORY_DANGEROUS_CONTENT","threshold": "BLOCK_NONE",},
    ]
    return config, safe