import json

def load_json(time, text):
    time_start = min(time)
    time_end = max(time)

    data = {
        "response": {
            "retelling": text,
            "time-start": time_start,
            "time-end": time_end
        }
    }
    
    return data

def get_args_json(json_data):
    try:
        messages = json_data.get("messages", [])
        if "content" in messages[0]:
            return get_args_day(json_data)
        elif "retell" in messages[0]:
            return get_args_week(json_data)
        else:

            return fail_json_handle()
    except:
        return fail_json_handle()

def get_args_day(json_data):
    contents = []
    time = []
    try:
        messages = json_data.get("messages", [])
        for message in messages:
            content = message.get("content")
            message_time = message.get("time")
            name = message.get("username")

            contents.append("От: " + name + ";" + " Текст сообщения: " + content + ";" + " Время отпарвки: " + message_time)
            time.append(message_time)
    
        return contents, time
    
    except:
        fail_json_handle()
        
def get_args_week(json_data):
    retells = []
    days = []
    try:
        messages = json_data.get("messages", [])  
        for message in messages:
            retell = message.get("retell")
            day = message.get("day")
            retells.append(retell)
            days.append(day)

        return retells, days

    except:
        return fail_json_handle()
    
def fail_json_receive() -> dict :
    data = {
        "responses": [ 
            {
            "response": "failed to receive json",
            "time-start": None,
            "time-end": None,
            "chat-id": None
            }
        ]
    }
    return data

def fail_json_handle() -> tuple[list, list]:
    response = "Failed to handle json"
    day = None
    return  response, day
