from core.nlp_utils import normalize, detect_app, detect_web_app
from core.logger import log_user, log_jarvis
from system.system_info import get_info
from web.weather import get_weather
import os
import webbrowser
import urllib.parse
import subprocess


class JarvisAgent:

    def process(self, text: str) -> str:
        raw = text
        cleaned = normalize(raw)

        log_user(raw)

        # ================= GREETING =================
        if cleaned in ["", "jarvis", "hi", "hello", "hlo", "hey"]:
            reply = "Yes sir, I am listening"
            log_jarvis(reply)
            return reply

        # ================= EXIT =================
        if any(x in cleaned for x in ["bye", "goodbye", "see you"]):
            reply = "Goodbye sir, see you next time"
            log_jarvis(reply)
            return reply

        # ================= WEATHER =================
        if "weather" in cleaned:
            reply = get_weather()
            log_jarvis(reply)
            return reply

        # ================= SYSTEM INFO =================
        if any(x in cleaned for x in ["system", "cpu", "ram", "battery"]):
            reply = get_info()
            log_jarvis(reply)
            return reply

        # ================= TASK MANAGER =================
        if any(x in cleaned for x in [
            "process", "processes", "desktop processes",
            "running apps", "running applications",
            "task manager", "tasks"
        ]):
            os.system("taskmgr")
            reply = "Opening Task Manager"
            log_jarvis(reply)
            return reply

        # ================= FILE MANAGER SEARCH =================
        if "search" in cleaned and any(x in cleaned for x in ["file manager", "files", "file", "explorer"]):

            query = cleaned
            for word in [
                "search", "in", "on", "inside",
                "file manager", "files", "file", "explorer"
            ]:
                query = query.replace(word, "")

            query = query.strip()

            if query:
                subprocess.Popen(
                    f'explorer "search-ms:query={query}"',
                    shell=True
                )
                reply = f"Searching {query} in File Explorer"
            else:
                reply = "What file should I search for?"

            log_jarvis(reply)
            return reply

        # ================= YOUTUBE SEARCH =================
        if "search" in cleaned and "youtube" in cleaned:
            query = (
                cleaned.replace("search", "")
                .replace("on youtube", "")
                .replace("youtube", "")
                .strip()
            )

            if query:
                url = "https://www.youtube.com/results?search_query=" + urllib.parse.quote(query)
                webbrowser.open(url)
                reply = f"Searching {query} on YouTube"
            else:
                reply = "What should I search on YouTube?"

            log_jarvis(reply)
            return reply

        # ================= GOOGLE SEARCH =================
        if "search" in cleaned:
            query = cleaned.replace("search", "").replace("on google", "").strip()
            webbrowser.open(
                "https://www.google.com/search?q=" + urllib.parse.quote(query)
            )
            reply = f"Searching {query} on Google"
            log_jarvis(reply)
            return reply

        # ================= CLOSE APPS =================
        if "close" in cleaned:
            app = detect_app(cleaned)

            if app == "notepad":
                os.system("taskkill /im notepad.exe /f")
                reply = "Notepad closed successfully"

            elif app == "explorer":
                os.system("taskkill /f /im explorer.exe")
                os.system("start explorer.exe")
                reply = "File Explorer closed"

            else:
                reply = "I could not identify the application to close"

            log_jarvis(reply)
            return reply

        # ================= OPEN APPS =================
        if "open" in cleaned:

            # ----- WINDOWS APPS -----
            app = detect_app(cleaned)

            if app == "notepad":
                os.system("start notepad")
                reply = "Opening Notepad"

            elif app == "explorer":
                os.system("start explorer")
                reply = "Opening File Explorer"

            elif app == "settings":
                os.system("start ms-settings:")
                reply = "Opening Settings"

            elif app == "control_panel":
                os.system("control")
                reply = "Opening Control Panel"

            elif app == "task_manager":
                os.system("taskmgr")
                reply = "Opening Task Manager"

            # ----- WEB APPS -----
            else:
                web_app = detect_web_app(cleaned)

                if web_app == "youtube":
                    webbrowser.open("https://www.youtube.com")
                    reply = "Opening YouTube"

                elif web_app == "whatsapp":
                    webbrowser.open("https://web.whatsapp.com")
                    reply = "Opening WhatsApp"

                elif web_app == "gmail":
                    webbrowser.open("https://mail.google.com")
                    reply = "Opening Gmail"

                elif web_app == "google":
                    webbrowser.open("https://www.google.com")
                    reply = "Opening Google"

                else:
                    query = cleaned.replace("open", "").strip()
                    webbrowser.open(
                        "https://www.google.com/search?q=" + urllib.parse.quote(query)
                    )
                    reply = f"I could not find {query} on your system, searching on Google"

            log_jarvis(reply)
            return reply

        # ================= FALLBACK =================
        reply = "Sorry sir, I did not understand that command"
        log_jarvis(reply)
        return reply
