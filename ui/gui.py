import tkinter as tk
import threading

from core.listener import listen_once
from core.speaker import speak
from core.agent import JarvisAgent

agent = JarvisAgent()


# ================== COLORS & STYLES ==================
BG_MAIN = "#0b1220"
BG_CHAT = "#020617"
BG_INPUT = "#020617"
ACCENT = "#38bdf8"
BTN_MIC = "#22c55e"
BTN_MIC_ACTIVE = "#facc15"
BTN_SEND = "#2563eb"
TEXT_COLOR = "#e5e7eb"


class JarvisUI:
    def __init__(self, root):
        self.root = root
        self.root.title("JARVIS • Desktop AI Assistant")
        self.root.state("zoomed")
        self.root.configure(bg=BG_MAIN)

        # ================= HEADER =================
        header = tk.Frame(root, bg=BG_MAIN, height=70)
        header.pack(fill=tk.X)

        title = tk.Label(
            header,
            text="J A R V I S",
            font=("Segoe UI", 26, "bold"),
            fg=ACCENT,
            bg=BG_MAIN
        )
        title.pack(pady=10)

        # ================= CHAT AREA =================
        chat_container = tk.Frame(root, bg=BG_MAIN)
        chat_container.pack(fill=tk.BOTH, expand=True, padx=25, pady=(5, 10))

        self.chat = tk.Text(
            chat_container,
            bg=BG_CHAT,
            fg=TEXT_COLOR,
            font=("Consolas", 13),
            wrap="word",
            bd=0,
            padx=20,
            pady=20
        )
        self.chat.pack(fill=tk.BOTH, expand=True)
        self.chat.configure(state="disabled")

        # ================= INPUT BAR =================
        bottom = tk.Frame(root, bg=BG_MAIN, height=90)
        bottom.pack(fill=tk.X, padx=25, pady=15)

        # ---- Input box (rounded feel using padding) ----
        input_container = tk.Frame(
            bottom,
            bg=BG_INPUT,
            highlightthickness=2,
            highlightbackground=ACCENT
        )
        input_container.pack(side=tk.LEFT, fill=tk.X, expand=True, padx=(0, 15))

        self.entry = tk.Entry(
            input_container,
            font=("Segoe UI", 15),
            bg=BG_INPUT,
            fg="white",
            insertbackground="white",
            bd=0
        )
        self.entry.pack(fill=tk.X, ipady=10, padx=15)
        self.entry.bind("<Return>", self.send_text)

        # ---- Send Button ----
        self.send_btn = tk.Button(
            bottom,
            text="Send",
            font=("Segoe UI", 12, "bold"),
            bg=BTN_SEND,
            fg="white",
            activebackground="#1d4ed8",
            bd=0,
            padx=25,
            pady=12,
            command=self.send_text
        )
        self.send_btn.pack(side=tk.LEFT, padx=(0, 15))

        # ---- Mic Button (Big + 3D Feel) ----
        self.mic_btn = tk.Button(
            bottom,
            text="🎙",
            font=("Segoe UI", 22),
            bg=BTN_MIC,
            fg="black",
            activebackground=BTN_MIC_ACTIVE,
            bd=0,
            width=4,
            command=self.listen_voice
        )
        self.mic_btn.pack(side=tk.RIGHT)

        # ================= STARTUP =================
        self.log_jarvis("System online. Type or speak your command.")
        speak("System online. Type or speak your command.")

    # ================= CHAT HELPERS =================
    def log_user(self, text):
        self.chat.configure(state="normal")
        self.chat.insert(tk.END, f"\n🧑 You:\n{text}\n")
        self.chat.configure(state="disabled")
        self.chat.see(tk.END)

    def log_jarvis(self, text):
        self.chat.configure(state="normal")
        self.chat.insert(tk.END, f"\n🤖 Jarvis:\n{text}\n")
        self.chat.configure(state="disabled")
        self.chat.see(tk.END)

    # ================= TEXT COMMAND =================
    def send_text(self, event=None):
        text = self.entry.get().strip()
        self.entry.delete(0, tk.END)

        if not text:
            return

        self.log_user(text)

        reply = agent.process(text)
        self.log_jarvis(reply)
        speak(reply)

    # ================= VOICE COMMAND =================
    def listen_voice(self):
        threading.Thread(target=self._voice_bg, daemon=True).start()

    def _voice_bg(self):
        # Mic animation (visual feedback)
        self.mic_btn.config(bg=BTN_MIC_ACTIVE)
        self.log_jarvis("Listening...")

        text = listen_once()

        self.mic_btn.config(bg=BTN_MIC)

        if not text:
            self.log_jarvis("I could not hear you.")
            speak("I could not hear you.")
            return

        self.log_user(text)
        reply = agent.process(text)
        self.log_jarvis(reply)
        speak(reply)


def run_ui():
    root = tk.Tk()
    JarvisUI(root)
    root.mainloop()
