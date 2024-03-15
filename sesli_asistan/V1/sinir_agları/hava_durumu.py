from urllib.parse import quote
import requests
from noronlar.speakAndListen import speak, listen


def translate(weather_desc):
    if weather_desc == "clear sky":
        hava_durumu = "Temiz"
    elif weather_desc == "few clouds":
        hava_durumu = "Az bulutlu"
    elif weather_desc == "scattered clouds":
        hava_durumu = "Parçalı bulutlu"
    elif weather_desc == "broken clouds":
        hava_durumu = "Ağır bulutlu"
    elif weather_desc == "shower rain":
        hava_durumu = "Yağmur"
    elif weather_desc == "rain":
        hava_durumu = "Yağmur"
    elif weather_desc == "thunderstorm":
        hava_durumu = "Fırtına"
    elif weather_desc == "snow":
        hava_durumu = "Kar"
    elif weather_desc == "mist":
        hava_durumu = "Sis"
    elif weather_desc == "smoke":
        hava_durumu = "Duman"
    elif weather_desc == "haze":
        hava_durumu = "Parlak bulutlu"
    elif weather_desc == "dust":
        hava_durumu = "Toz"
    elif weather_desc == "fog":
        hava_durumu = "Sis"
    elif weather_desc == "sand":
        hava_durumu = "Kum"
    elif weather_desc == "ash":
        hava_durumu = "Kül"
    elif weather_desc == "squalls":
        hava_durumu = "Rüzgarlar"
    elif weather_desc == "tornado":
        hava_durumu = "Tornado"
    elif weather_desc == "overcast clouds":
        hava_durumu = "Bulutlu"
    else:
        hava_durumu = "Bilinmeyen"

    return hava_durumu


def turkce_karakterleri_duzelt(girdi):
    duzeltilmis = girdi.replace('i̇', 'i').replace('İ', 'I').replace('ş', 's').replace('Ş', 'S').replace('ğ',
                                                                                                          'g').replace(
        'Ğ', 'G').replace('ü', 'u').replace('Ü', 'U').replace('ö', 'o').replace('Ö', 'O').replace('ç', 'c').replace('Ç',
                                                                                                                    'C')
    return duzeltilmis


def hava_durumu_bilgisi_al(il):
    api_key = '55d13334a97bf844fa02930944ced23d'
    encoded_il = turkce_karakterleri_duzelt(il)
    url = f'http://api.openweathermap.org/data/2.5/weather?q={encoded_il}&appid={api_key}&units=metric'
    response = requests.get(url)
    print(encoded_il)
    print(response.status_code)
    print(url)
    if response.status_code == 200:
        data = response.json()
        temp = data['main']['temp']
        weather_desc = data['weather'][0]['description']
        return f"{il} şu an {weather_desc}. Sıcaklık: {temp} derece."
    else:
        return "Hava durumu bilgisi alınamadı."


def sorgu():
    speak("Hangi ilin hava durumu bilgisini istersiniz?")
    il = listen()
    if il is not None:
        hava_durumu_bilgisi = hava_durumu_bilgisi_al(il)
        speak(hava_durumu_bilgisi)
        print(hava_durumu_bilgisi)
    else:
        speak("Anlaşılamadı. Lütfen tekrar deneyin.")