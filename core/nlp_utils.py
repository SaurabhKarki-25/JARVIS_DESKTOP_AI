import difflib

# ---------------- WAKE WORD VARIANTS ----------------
WAKE_WORDS = [
    "jarvis", "parvis", "parviz", "jarvish", "jarvez"
]

# ---------------- JUNK / FILLER WORDS ----------------
FILLER_WORDS = [
    "ok", "please", "the", "this", "is", "my", "your", "a", "an", "to"
]

# ---------------- WINDOWS APPS (ALIASES) ----------------
WINDOWS_APPS = {
    "notepad": [
        "notepad", "note pad", "notepd", "note pad app",
        "text editor", "notes", "write notes"
    ],
    "explorer": [
        "file manager", "file explorer", "explorer", "files", "folders"
    ],
    "settings": [
        "settings", "setting", "system settings", "windows settings"
    ],
    "control_panel": [
        "control panel", "control", "system control"
    ],
    "task_manager": [
        "task manager", "taskmanager", "tasks", "process manager"
    ],
    "chrome": [
        "chrome", "google chrome", "browser", "internet"
    ],
    "word": [
        "word", "ms word", "microsoft word", "document editor"
    ],
    "powerpoint": [
        "powerpoint", "ppt", "ms powerpoint", "presentation"
    ],
    "bluetooth": [
        "bluetooth", "blue tooth", "bt", "wireless"
    ],
    
    
}

# ================= WEB APPS =================
WEB_APPS = {
    "youtube": [
        "youtube", "you tube", "utube", "you toob",
        "video", "videos", "play video", "watch video"
    ],

    "whatsapp": [
        "whatsapp", "whats app", "what app", "whtspp",
        "chat", "message", "messages", "wa"
    ],

    "gmail": [
        "gmail", "mail", "email", "google mail",
        "check mail", "open mail"
    ],

    "google": [
        "google", "browser", "internet", "search",
        "web", "chrome"
    ]
}

# ---------------- NORMALIZE TEXT ----------------
def normalize(text: str) -> str:
    text = text.lower()

    # remove wake words
    for w in WAKE_WORDS:
        text = text.replace(w, "")

    # remove filler words
    for f in FILLER_WORDS:
        text = text.replace(f, "")

    # clean extra spaces
    return " ".join(text.split())


# ---------------- FUZZY MATCH HELPER ----------------
def fuzzy_match(word, choices, cutoff=0.75):
    matches = difflib.get_close_matches(word, choices, n=1, cutoff=cutoff)
    return matches[0] if matches else None


# ---------------- DETECT WINDOWS APP (FUZZY) ----------------
def detect_app(text: str):
    words = text.split()

    for app, aliases in WINDOWS_APPS.items():
        for alias in aliases:
            alias_words = alias.split()
            for w in words:
                if fuzzy_match(w, alias_words):
                    return app
            if alias in text:
                return app
    return None

def detect_web_app(text: str):
    for app, aliases in WEB_APPS.items():
        for alias in aliases:
            if alias in text:
                return app
    return None
