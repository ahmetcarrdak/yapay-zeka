import os
from gtts import gTTS
import speech_recognition as sr
from colorama import Fore


def speak(text):
    tts = gTTS(text=text, lang='tr')
    tts.save("temp.mp3")
    os.system("afplay temp.mp3")


def listen():
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        print(Fore.GREEN + "Sizi dinliyorum...")
        recognizer.adjust_for_ambient_noise(source, duration=0.5)
        audio = recognizer.listen(source)

    try:
        print(Fore.BLUE + "Ses algılanıyor...")
        text = recognizer.recognize_google(audio, language="tr-TR")
        print(Fore.CYAN + "Söylenen: " + text)
        return text.lower()
    except sr.UnknownValueError:
        print(Fore.RED + "İstek anlaşılmadı")
        return None
    except sr.RequestError as e:
        print(Fore.RED + "İstek anlaşılmadı: {0}".format(e))
        return None