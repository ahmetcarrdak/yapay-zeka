import webbrowser
from noronlar.speakAndListen import speak, listen


def google_search(query):
    search_url = f"https://www.google.com/search?q={query}"
    webbrowser.open(search_url)


def sorgu():
    speak("Google'da ne aramak istersiniz?")
    q = listen()
    if q is not None:
        google_search(q)
    else:
        speak("Anlaşılamadı. Lütfen tekrar deneyin.")
