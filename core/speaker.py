import subprocess

def speak(text: str):
    if not text:
        return

    # clean text to avoid breaking PowerShell
    safe_text = text.replace('"', '').replace("'", "")

    command = [
        "powershell",
        "-Command",
        (
            "Add-Type -AssemblyName System.Speech; "
            "$speak = New-Object System.Speech.Synthesis.SpeechSynthesizer; "
            f"$speak.Speak('{safe_text}')"
        )
    ]

    try:
        subprocess.run(command, shell=False)
    except Exception as e:
        print("[TTS ERROR]", e)
