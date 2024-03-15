import sinir_agları.hava_durumu
import sinir_agları.web_browser
from noronlar.speakAndListen import listen, speak
from noronlar.db_control import customer_control
from face.intelFace import intelFace

nova_flag = True
customer_control()

while True:
    try:
        intelFace()
        if nova_flag:
            print(f"Merhaba Ahmet bey, ben Nova. Size nasıl yardımcı olmamı istersiniz")
            speak(f"Merhaba Ahmet bey, ben Nova. Size nasıl yardımcı olmamı istersiniz")
        nova_flag = False
        command = listen()

        if command is not None:
            if "beni duyuyor musun" in command:
                speak("Evet sizi duyabiliyorum, nasıl yardımcı olabilirim?")
            elif "hava durumu" in command:
                sinir_agları.hava_durumu.sorgu()
            elif "teşekkürler" in command:
                speak("Rica ederim, her zaman buradayım.")
            elif "google'da ara" in command:
                sinir_agları.web_browser.sorgu()
            elif "sistemi kapat" in command:
                speak("Sistem kapanıyor! İyi günler dilerim.")
                break
            elif "yeni kullanıcı oluştur" in command:
                pass
            else:
                speak(command)
    except KeyboardInterrupt:
        speak("İşlem durduruluyor, iyi günler efendim")
        break
