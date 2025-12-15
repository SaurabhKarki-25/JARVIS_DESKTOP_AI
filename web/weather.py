import requests

def get_weather(city="Delhi"):
    try:
        return requests.get(f"https://wttr.in/{city}?format=3").text
    except:
        return "Weather service is not available right now"
