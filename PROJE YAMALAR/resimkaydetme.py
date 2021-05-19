import cv2

kamera=cv2.VideoCapture(0)#0 kamera sayısını verir ve 0 webcam numarasıdır.fazla ise ona göre veririz.
#0 yerine deneme.mp4 yazarsak bu videoyu oynatır.


kamera.set(cv2.CAP_PROP_FRAME_WIDTH,850)
kamera.set(cv2.CAP_PROP_FRAME_HEIGHT,720)
#açılan pencerenin çerçeve boyutunu ayarlıyoruz.

a=0
while True:
    ret, goruntu=kamera.read()
    #griton=cv2.cvtColor(goruntu,cv2.COLOR_BGR2GRAY)#görüntüyü gri yapar.
    """
    ret=kamera.set(3,320)
    ret=kamera.set(4,240)
    #yukarıda yaptığmız boyutlandırmanın ikinci yolu  
    """

    cv2.imwrite('kayıt\gpp{}.jpg'.format(a),goruntu)
    a=a+1
    cv2.imshow('Video',goruntu)
    #cv2.imshow('GriTon',griton)
    if cv2.waitKey(200) & 0xFF==ord('q'):
        break

kamera.release()
cv2.destroyAllWindows()