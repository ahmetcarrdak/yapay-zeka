from noronlar.speakAndListen import listen, speak
from face.intelFace import intelFace
from googlesearch import search
from bs4 import BeautifulSoup
import requests
import subprocess

nova_flag = True

while True:
    try:
        intelFace()
        if nova_flag:
            print(f"Buyrun")
            speak(f"Buyrun")
        nova_flag = False
        command = listen()

        if command is not None:
            if "beni duyuyor musun" in command:
                speak("Evet sizi duyabiliyorum, nasıl yardımcı olabilirim?")
            else:
                print("\nGoogle'da bulunan sonuçlar:")
                for j in search(command, num_results=1):
                    response = requests.get(j)
                    soup = BeautifulSoup(response.text, 'html.parser')
                    print(f"Başlık: {soup.title.string}")
                    print("İçerik:")
                    print(soup.get_text())
                    subprocess.call(['say', soup.get_text()])
                    print("-----")
                    break
    except KeyboardInterrupt:
        speak("Kapandı")
        print("İyi günler")
        break
