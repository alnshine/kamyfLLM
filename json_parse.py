import json

def create_json(time: list[str], chat_id: int, text: str) -> dict:
    """
    Generate a JSON file with response data.
    
    :param time: List of timestamps.
    :type time: List[str]
    :param chat_id: Chat ID.
    :type chat_id: str
    :param text: Retelling text.
    :type text: str
    :return: Dictionary containing response data.
    :rtype: dict
    """
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
    
    return data

def get_args_json(json_data: dict) -> tuple[list[str], list[str], list[str]]:
    """
    Parse a JSON file and extract contents, time, names.
    
    :param json_data: Dictionary containing JSON data.
    :type json_data: dict
    :return: A tuple containing three lists: contents, time, and names.
    :rtype: Tuple[List[str], List[str], List[str]]
    """
    try:
        contents = []
        time = []
        names = []
        chat_id = None
        messages = json_data.get("messages", [])  
        if "content" not in messages[0]:
            return get_args_week(json_data)
        for message in messages:
            content = message.get("content")
            message_time = message.get("time")
            name = message.get("username")
            chat_id = message.get("chat_id")

            contents.append("От: " + name + ";" + " Текст сообщения: " + content + ";" + " Время отпарвки: " + message_time)
            time.append(message_time)
            names.append(name)

        return contents, time, chat_id

    except Exception as e:
        print("Ошибка при разборе JSON:", e)
        return None, None, None, None
    
def get_args_week(json_data: dict) -> tuple[list[str], list[str], list[str]]:
    try:
        retels = []
        times = []
        chat_id = None
        messages = json_data.get("messages")
        for message in messages:
            time = message.get("time")
            retel = "День: " + time + "\n" + message.get("retell")
            retels.append(retel)
            times.append(time)
        return retels, times, chat_id
    except:
        data = {
            "response": {
                "retelling": "не получилось обработать сообщения за неделю",
                "time-start": "2024-03-17T08:30:45.123456789Z",
                "time-end": "2024-03-17T08:50:00.890123456Z",
                "chat-id": 0
                }
            }
        return data