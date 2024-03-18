import json

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
        messages = json_data.get("messages", [])  
        for message in messages:
            content = message.get("content")
            message_time = message.get("time")
            name = message.get("username")
            chat_id = message.get("chat-id")

            contents.append("От: " + name + ";" + " Текст сообщения: " + content + ";" + " Время отпарвки: " + message_time)
            time.append(message_time)
            names.append(name)

        return contents, time, chat_id

    except Exception as e:
        print("Ошибка при разборе JSON:", e)
        return None, None, None, None