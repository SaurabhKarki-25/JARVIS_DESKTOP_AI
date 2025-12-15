import speech_recognition as sr
import sounddevice as sd
import numpy as np
import scipy.io.wavfile as wav
import tempfile
import os

SAMPLE_RATE = 16000
DURATION = 5  # seconds

recognizer = sr.Recognizer()
recognizer.dynamic_energy_threshold = True


def listen_once():
    try:
        print("[MIC] Listening (sounddevice + Google STT)...")

        audio = sd.rec(
            int(DURATION * SAMPLE_RATE),
            samplerate=SAMPLE_RATE,
            channels=1,
            dtype="int16"
        )
        sd.wait()

        with tempfile.NamedTemporaryFile(suffix=".wav", delete=False) as f:
            wav.write(f.name, SAMPLE_RATE, audio)
            temp_file = f.name

        with sr.AudioFile(temp_file) as source:
            audio_data = recognizer.record(source)

        os.remove(temp_file)

        text = recognizer.recognize_google(audio_data)
        text = text.lower()

        print("[MIC HEARD]:", text)
        return text

    except sr.UnknownValueError:
        print("[MIC] Could not understand")
        return ""

    except Exception as e:
        print("[MIC ERROR]", e)
        return ""
