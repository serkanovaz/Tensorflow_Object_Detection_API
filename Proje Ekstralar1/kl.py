import cv2
liste=[45,90,135,180,-45,-90,-135]
t=1210
for i in range(1,41):
    for k in range(0, 7):
      image=cv2.imread('a1\{}.jpg'.format(i)) #döndürmek istediğim görüntünün bilgisayarımda ki konumunu belirtiyorum.
      height,width=image.shape[:2] #Görüntüyü merkezin etrafında döndürmek için ikiye bölün.
      rotation_matrix=cv2.getRotationMatrix2D((width/2,height/2),liste[k],.5)
      rotated_image=cv2.warpAffine(image,rotation_matrix,(width,height))
      cv2.imwrite('a2\kp{}.jpg'.format(t),rotated_image)
      t=t+1