# SOBE
 Canlı görüntü üzerinden tanımlı tehlikeli nesne takibi ve otomatik çağrı oluşturma.
 
## Özet
Tanımlı nesnelerin canlı görüntüler üzerinden taraması yapılır ve tespit edilmesi durumunda otomatik çağrı oluşturulur. Bu projede çağrılar e-posta üzerinden yapılmaktadır. Google tarafından geliştirilmiş Tensorflow Object Detection API ile kendi nesne sınıfımız oluşturulmuştur. Görüntü üzerindeki taramalarda Faster R-CNN algoritması kullanılmıştır. Üniversite bitirme projesi olarak geliştirilmiştir. Github 1000 dosya limitinden dolayı eğitim ve test kümelerinde kullanılan resimler images.rar içerisindedir. 

## Kullanılan Teknolojiler
 * Tensorflow-Tensorflow API
 * Faster R-CNN
 * OpenCV
 * SMTP
 * OS
 * Numpy
 * PyQt5
 * CUDA
 * cuDNN
 
## Özellikler
 * Bıçak, tabanca, el bombası olmak üzere 3 nesne takibi yapar.
 * Eğitim, 70131 adımda gerçekleşti.
 * 8238 öğrenme, 2745 test aşamasında olmak üzere 10983 resim kullanıldı(Paylaşılan veri setindeki resim sayısı 8373).
 * Canlı görüntü üzerinden nesne tespit edilmesi durumunda o anki görüntüler fotoğraf olarak kayıt altına alınır.
 * Nesne tespiti durumunda anlık olarak otomatik e-posta oluşturur ve gönderimi sağlar.
 * Oluşturulan e-posta içeriğine o anki durumun görüntüleri fotoğraf olarak aktarılır.
 * Geliştirme Tarihi : 2020
