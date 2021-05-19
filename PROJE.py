import os
import numpy as np
import tensorflow as tf
import sys
import cv2
import datetime
import locale
import smtplib
from email.message import EmailMessage
import imghdr

sys.path.append("..")

from utils import label_map_util
from utils import visualization_utils as vis_util

"""
def tomail ():
    mesaj=EmailMessage()
    mesaj["Subject"]="KARABÜK MERKEZ HALKBANK"
    mesaj["From"]="#gönderici e-posta adresi"
    mesaj["To"]="#alıcı e-posta adresi"
    mesaj.set_content("KIRMIZI ALARM")
    
    with smtplib.SMTP_SSL("smtp.gmail.com",465) as smtp:
        smtp.login("#gönderici e-posta adresi", "#şifre")
        smtp.send_message(mesaj)
"""

"""
def ktomail():
    mesaj = EmailMessage()
    mesaj["Subject"] = "BURSA MERKEZ HALKBANK KIRMIZI ALARM"
    mesaj["From"] = "#gönderici e-posta adresi"
    mesaj["To"] = "#alıcı e-posta adresi"
    mesaj.set_content("BIÇAKLI ALARM")

    with open("utest\knife3.jpg", "rb") as f:
        image_data = f.read()
        image_name = f.name
        image_type = imghdr.what(f.name)
    mesaj.add_attachment(image_data, maintype="image", subtype=image_type, filename=image_name)
    with smtplib.SMTP_SSL("smtp.gmail.com", 465) as smtp:
        smtp.login("#gönderici e-posta adresi", "#şifre")
        smtp.send_message(mesaj)
"""

def tomail (il,nesne,gr):
    mesaj=EmailMessage()
    mesaj["Subject"]=il+" MERKEZ HALKBANK KIRMIZI ALARM"
    mesaj["From"]="#gönderici olan e-posta adresi"
    mesaj["To"]="#alıcı e-posta adresi"
    mesaj.set_content(gr+" SOYGUN")
    with open("utest/"+nesne+"3.jpg","rb") as f:
             image_data=f.read()
             image_name=f.name
             image_type=imghdr.what(f.name)

    mesaj.add_attachment(image_data,maintype="image",subtype=image_type,filename=image_name)
    with smtplib.SMTP_SSL("smtp.gmail.com",465) as smtp:
             smtp.login("#gönderici e-posta adresi", "#e-posta adresin şifresi")
             smtp.send_message(mesaj)

MODEL_NAME = 'inference_graph'
CWD_PATH = os.getcwd()
PATH_TO_CKPT = os.path.join(CWD_PATH,MODEL_NAME,'frozen_inference_graph.pb')
PATH_TO_LABELS = os.path.join(CWD_PATH,'training','labelmap.pbtxt')
NUM_CLASSES = 3

label_map = label_map_util.load_labelmap(PATH_TO_LABELS)
categories = label_map_util.convert_label_map_to_categories(label_map, max_num_classes=NUM_CLASSES, use_display_name=True)
category_index = label_map_util.create_category_index(categories)

detection_graph = tf.Graph()
with detection_graph.as_default():
    od_graph_def = tf.GraphDef()
    with tf.gfile.GFile(PATH_TO_CKPT, 'rb') as fid:
        serialized_graph = fid.read()
        od_graph_def.ParseFromString(serialized_graph)
        tf.import_graph_def(od_graph_def, name='')

    sess = tf.Session(graph=detection_graph)

image_tensor = detection_graph.get_tensor_by_name('image_tensor:0')
detection_boxes = detection_graph.get_tensor_by_name('detection_boxes:0')
detection_scores = detection_graph.get_tensor_by_name('detection_scores:0')
detection_classes = detection_graph.get_tensor_by_name('detection_classes:0')
num_detections = detection_graph.get_tensor_by_name('num_detections:0')

video = cv2.VideoCapture(0)
ret = video.set(3,1280)
ret = video.set(4,720)

#k=bıçak
#g=silah
#e=bomba
g=1
k=1
e=1
sayac=0
while(True):

    ret, frame = video.read()
    frame_expanded = np.expand_dims(frame, axis=0)
    (boxes, scores, classes, num) = sess.run(
        [detection_boxes, detection_scores, detection_classes, num_detections],
        feed_dict={image_tensor: frame_expanded})
    vis_util.visualize_boxes_and_labels_on_image_array(
        frame,
        np.squeeze(boxes),
        np.squeeze(classes).astype(np.int32),
        np.squeeze(scores),
        category_index,
        use_normalized_coordinates=True,
        line_thickness=8,

        )

    locale.setlocale(locale.LC_ALL, 'turkish')
    an = datetime.datetime.now()
    tarih = datetime.datetime.strftime(an, '%c')
    fontscale = 1.0
    color = (0, 0, 255)
    a=str(sayac)
    fontface = cv2.FONT_HERSHEY_COMPLEX_SMALL
    cv2.putText(frame, tarih, (250, 40), fontface, fontscale, color)
    cv2.putText(frame, "KAMERA 01", (900, 40), fontface, fontscale, color)
    cv2.putText(frame, "T.E.N.S:"+a, (600, 40), fontface, fontscale, color)

    cv2.imshow('SOBE GUVENLIK', frame)

    if np.squeeze(classes).astype(np.int32)[0]==1 and np.squeeze(scores)[0]*100>90 and e<6 :
        cv2.imwrite("utest\e{}.jpg".format(e), frame)
        e=e+1
        if e==5:
            sayac += 1
            il = "İSTANBUL"
            nesne = "e"
            gr = "BOMBALI"
            tomail(il,nesne,gr)

    if  np.squeeze(classes).astype(np.int32)[0]==2 and np.squeeze(scores)[0]*100>90 and g<6 :
        cv2.imwrite("utest\gun{}.jpg".format(g), frame)
        g=g+1
        if g==5:
            sayac += 1
            il="BURSA"
            nesne="gun"
            gr="SİLAHLI"
            tomail(il,nesne,gr)

    if np.squeeze(classes).astype(np.int32)[0]==3 and np.squeeze(scores)[0]*100>90 and k<6 :
        cv2.imwrite("utest\knife{}.jpg".format(k), frame)
        k=k+1
        if k==5:
            sayac += 1
            il = "KARABÜK"
            nesne = "knife"
            gr = "BIÇAKLI"
            tomail(il,nesne,gr)

    print(np.squeeze(scores)[0]*100)
    if cv2.waitKey(200) == ord('q'):
        break

video.release()
cv2.destroyAllWindows()

