def classify_intent(cmd):
    if any(w in cmd for w in ["open", "start", "launch"]):
        return {"intent": "open_app"}, 0.9

    if cmd.startswith("close"):
        return {"intent": "close_app"}, 0.9

    if "search" in cmd and "youtube" in cmd:
        return {"intent": "search_youtube"}, 0.9

    if "search" in cmd and "google" in cmd:
        return {"intent": "search_google"}, 0.9

    if "system status" in cmd:
        return {"intent": "system_status"}, 0.9

    if "battery" in cmd:
        return {"intent": "battery_status"}, 0.9

    if any(w in cmd for w in ["hello", "hi", "hey jarvis"]):
        return {"intent": "greeting"}, 0.9

    return None, 0.0
