from datetime import datetime

def get_time_vibe():
    hour = datetime.now().hour
    if 5 <= hour < 12:
        return "energetic"
    elif 12 <= hour < 18:
        return "happy"
    elif 18 <= hour < 22:
        return "chill"
    return "sad"
