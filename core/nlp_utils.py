import re

# ---------- NORMALIZE USER TEXT ----------
def normalize(text: str) -> str:
    text = text.lower()
    text = re.sub(r"[^a-z0-9 ]", " ", text)
    return " ".join(text.split())


# ---------- WINDOWS APPS ----------
WINDOWS_APPS = {
    "notepad": ["notepad", "note pad", "notes"],
    "explorer": ["file manager", "file explorer", "explorer", "files"],
    "settings": ["settings", "system settings"],
    "control_panel": ["control panel"],
    "task_manager": ["task manager", "tasks", "processes"],
}


def detect_app(text: str):
    for app, aliases in WINDOWS_APPS.items():
        for a in aliases:
            if a in text:
                return app
    return None


# ---------- WEB APPS ----------
WEB_APPS = {
    "youtube": ["youtube", "you tube", "utube"],
    "whatsapp": ["whatsapp", "whats app", "whtspp"],
    "gmail": ["gmail", "mail", "email"],
    "google": ["google", "browser", "internet"]
}


def detect_web_app(text: str):
    for app, aliases in WEB_APPS.items():
        for a in aliases:
            if a in text:
                return app
    return None
