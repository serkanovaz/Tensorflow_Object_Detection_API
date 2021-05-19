import smtplib
from email.message import EmailMessage
import cv2
import os
import imghdr

def tomail (a,b):
    mesaj=EmailMessage()
    mesaj["Subject"]="KARABÜK MERKEZ HALKBANK"
    mesaj["From"]="#gönderici e-posta"
    mesaj["To"]="#alıcı e-posta"
    mesaj.set_content("KIRMIZI ALARM"+b+"SOYGUN")
    #for k in range(1,2):
    with open("test/"+a+"3.jpg","rb") as f:
             image_data=f.read()
             image_name=f.name
             image_type=imghdr.what(f.name)
    mesaj.add_attachment(image_data,maintype="image",subtype=image_type,filename=image_name)
    with smtplib.SMTP_SSL("smtp.gmail.com",465) as smtp:
             smtp.login("#gönderici e-posta", "#şifre")
             smtp.send_message(mesaj)

kamera=cv2.VideoCapture(0)
i=1
while True:
 ret, goruntu = kamera.read()
 cv2.imshow('Video', goruntu)
 if i<5:
  cv2.imwrite("test\silah{}.jpg".format(i),goruntu)

 if i==4:
     a="silah"
     b="SİLAHLI"
     tomail(a,b)

 i = i + 1
 if cv2.waitKey(200) & 0xFF == ord('q'):
     break

kamera.release()
cv2.destroyAllWindows()
