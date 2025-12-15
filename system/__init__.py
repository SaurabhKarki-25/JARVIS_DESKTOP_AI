import subprocess
import psutil
import webbrowser

APP_MAP = {
    "chrome": "chrome.exe",
    "calculator": "calc.exe",
    "notepad": "notepad.exe",
    "cmd": "cmd.exe",
    "paint": "mspaint.exe"
}

def open_system_app(name):
    name = name.lower()

    if name == "google":
        webbrowser.open("https://www.google.com")
        return True

    if name == "youtube":
        webbrowser.open("https://www.youtube.com")
        return True

    exe = APP_MAP.get(name)
    if not exe:
        return False

    subprocess.Popen(exe)
    return True

def close_app(name):
    exe = APP_MAP.get(name)
    if not exe:
        return False

    for p in psutil.process_iter(["name"]):
        if p.info["name"] and p.info["name"].lower() == exe:
            p.kill()
            return True
    return False

def close_safe_apps():
    closed = []
    for exe in APP_MAP.values():
        for p in psutil.process_iter(["name"]):
            if p.info["name"] and p.info["name"].lower() == exe:
                p.kill()
                closed.append(exe)
    return closed
