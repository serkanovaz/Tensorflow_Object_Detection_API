import cv2
"""image = cv2.imread('logo.jpg')  #Tercihen ‘image’ yerine istediğiniz herhangi bir değer verebilirsiniz.
rotated_image = cv2.transpose(image)
cv2.imshow('Rotated Image – Method 2', rotated_image)
cv2.waitKey(0)
cv2.destroyAllWindows()"""

#image=cv2.imread('02.jpg')   #döndürmek istediğim görüntünün bilgisayarımda ki konumunu belirtiyorum.

"""im2=image.rotate(90)
cv2.imshow('Rotated Image – Method 2', im2)
cv2.waitKey(0)
cv2.destroyAllWindows()"""
liste=[45,90,135,180,-45,-90,-135]
t=20
for i in range(1,2):
  for k in range(0, 7):
      image=cv2.imread('a1\{}.jpg'.format(i)) #döndürmek istediğim görüntünün bilgisayarımda ki konumunu belirtiyorum.
      height,width=image.shape[:2] #Görüntüyü merkezin etrafında döndürmek için ikiye bölün.
      rotation_matrix=cv2.getRotationMatrix2D((width/2,height/2),liste[k],.3)
      rotated_image=cv2.warpAffine(image,rotation_matrix,(width,height))
      cv2.imwrite('a2\{}.jpg'.format(t),rotated_image)
      t=t+1
