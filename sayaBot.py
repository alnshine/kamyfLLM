import google.generativeai as genai
from google.generativeai.generative_models import ChatSession
from dotenv import load_dotenv
import os
import json
import requests

def get_args_json(json_data):
    """
    This function parses json file
    """
    contents = []
    time = []
    names = []
    chat_id = None
    prompt = ""

    try:
        messages = json_data.get("messages", [])  # Получаем список сообщений из JSON данных

        for message in messages:
            content = message.get("content")
            message_time = message.get("time")
            name = message.get("username")
            chat_id = message.get("chat-id")

            contents.append("От: " + name + ";" + " Текст сообщения: " + content + ";" + " Время отпарвки: " + message_time)
            time.append(message_time)
            names.append(name)

        return contents, time, names, chat_id

    except Exception as e:
        print("Ошибка при разборе JSON:", e)
        return None, None, None, None

def create_response(messages:str, chat:ChatSession, safety_settings=None, generation_config=None) -> str:
    first_prompt = "Я тебе сейчас передам сообщения по одному. Не генерируй ответ до момента пока я не передам тебе START_PEREPHRASE. После этого сделай краткий перессказ полученной беседы. Пересказ должен быть емким, его цель: краткая выжимка всей беседы, и выжимка должна быть короче самой беседы."
    chat.send_message(first_prompt, safety_settings=safety_settings, generation_config=generation_config)
    for message in messages:
        try:
            response = chat.send_message(message, safety_settings=safety_settings, generation_config=generation_config)
            # print(response.text)
        except:
            perephrase = "перефразируй это сообщение: " + message
            try:
                response = chat.send_message(perephrase, safety_settings=safety_settings, generation_config=generation_config)
                # print(response.text)
            except:
                print("ERROR: ", response.text)
                return
    final_prompt = chat.send_message("START_PEREPHRASE", safety_settings=safety_settings, generation_config=generation_config)
    return final_prompt.text

def load_json(time, chat_id, text):
    time_start = min(time)
    time_end = max(time)

    data = {
        "response": {
            "retelling": text,
            "time-start": time_start,
            "time-end": time_end,
            "chat-id": chat_id
        }
    }

    # Генерация уникального имени для файла
    file_name = "response.json"

    with open(file_name, "w", encoding="utf-8") as json_file:
        json.dump(data, json_file, ensure_ascii=False, indent=2)
    
    return data

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
    messages, time, names, chat_id = get_args_json(json_data)
    response = create_response(messages, chat, safe, config)
    response_data = load_json(time, chat_id, response)
    return response_data


def main():
    model("example.json")

if __name__ == "__main__":
    main()