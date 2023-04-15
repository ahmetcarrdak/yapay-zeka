import cv2
import numpy as np
from matplotlib import pyplot as plt

# Resim İşlemleri
'''resim = cv2.imread("img/resim1.jpeg", 0) # Resmi seçer
cv2.imshow("Resim Penceresi", resim) # Resmi Açar

plt.imshow(resim, cmap="gray") 
plt.show()

k = cv2.waitKey(0) # Resmi bir tuşa basıldığında kapatır
print(k)
if k == ord("q"):
    print("q tuşuna basarak resim kaydedildi")
    cv2.imwrite("img/KaraResim.jpeg", resim) # Resmi kaydeder (Yeni resim olarak)
cv2.destroyWindow("Resim Penceresi")'''

# Geometrik Şekil çizme
'''img = np.zeros((512, 512,3), np.uint8)

#cv2.line(img, (0,0), (511,511), (255,0,0), 5)
#cv2.line(img, (50,400), (400,50), (0,255,0), 10)
#cv2.rectangle(img, (20,20), (300,300), (0, 255, 0), 2)
#cv2.rectangle(img, (200,200), (300,300), (0, 255, 0), -1)

font = cv2.FONT_HERSHEY_COMPLEX
cv2.putText(img, "Resim", (40,200), font, 4, (250, 0, 5), 4, cv2.LINE_AA)

cv2.imshow("Resim", img)
cv2.waitKey(0)
'''

# Fare Olayları

def draw(event, x, y, flags, param):
    if event == cv2.EVENT_LBUTTONDBLCLK:
        cv2.circle(img, (x, y), 50, (255, 0, 0), -1)



img = np.ones((512, 512, 3), np.uint8)

cv2.namedWindow("Paint")
cv2.setMouseCallback("Paint", draw)

while (1):
    cv2.imshow("Paint", img)
    if cv2.waitKey(1) & 0xFF == ord("q"):
        break

