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

from PyQt5 import QtCore, QtGui, QtWidgets

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

def panel():
    class Ui_Form(object):
        def setupUi(self, Form):
            Form.setObjectName("Form")
            Form.resize(601, 453)
            Form.setWindowIcon(QtGui.QIcon("r15.jpg"))
            Form.setStyleSheet("*{\n"
    "    font-size:16px;\n"
    "    font-family:sans-serif;\n"
    "}\n"
    "#Form{\n"
    "    background:url(:/image/qtimage/r15.jpg);\n"
    "}\n"
    "QFrame{\n"
    "    background:rgba(0,0,0,0.8);\n"
    "    border-radius:15px;\n"
    "}\n"
    "QPushButton{\n"
    "    background:#03a9f4;\n"
    "    color:#fff;\n"
    "    border-radius:15px;\n"
    "}\n"
    "QPushButton:hover{\n"
    "    background:rgba(0,0,0,0.6);\n"
    "    border-radius:15px;\n"
    "    color:#white;\n"
    "}\n"
    "QLineEdit{\n"
    "    border-radius:15px;\n"
    "    color:#black;    \n"
    "    font-style:italic bold;    \n"
    "    font-size:15px;    \n"
    "}\n"
    "QLabel{\n"
    "    color:#fff;\n"
    "    background:transparent;\n"
    "    font-size:24px;\n"
    "}\n"
    "")

            self.frame = QtWidgets.QFrame(Form)
            self.frame.setGeometry(QtCore.QRect(90, 60, 401, 301))
            self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
            self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
            self.frame.setObjectName("frame")
            self.pushButton = QtWidgets.QPushButton(self.frame)
            self.pushButton.setGeometry(QtCore.QRect(100, 220, 211, 41))
            self.pushButton.setObjectName("pushButton")
            self.lineEdit = QtWidgets.QLineEdit(self.frame)
            self.lineEdit.setGeometry(QtCore.QRect(80, 100, 241, 31))
            self.lineEdit.setText("")
            self.lineEdit.setObjectName("lineEdit")
            self.lineEdit_2 = QtWidgets.QLineEdit(self.frame)
            self.lineEdit_2.setGeometry(QtCore.QRect(80, 140, 241, 31))
            self.lineEdit_2.setText("")
            self.lineEdit_2.setEchoMode(QtWidgets.QLineEdit.Password)
            self.lineEdit_2.setObjectName("lineEdit_2")
            self.label = QtWidgets.QLabel(self.frame)
            self.label.setGeometry(QtCore.QRect(130, 40, 161, 31))
            self.label.setObjectName("label")

            self.retranslateUi(Form)
            QtCore.QMetaObject.connectSlotsByName(Form)

            self.pushButton.clicked.connect(self.click)




        def retranslateUi(self, Form):
            _translate = QtCore.QCoreApplication.translate
            Form.setWindowTitle(_translate("Form", "SOBE GUVENLIK"))
            self.pushButton.setText(_translate("Form", "GIRIS"))
            self.lineEdit.setPlaceholderText(_translate("Form", "KULLANICI ADI"))
            self.lineEdit_2.setPlaceholderText(_translate("Form", "PAROLA"))
            self.label.setText(_translate("Form", "GIRIS PANELI"))

        def showmes(self,title,mes):
            mb=QtWidgets.QMessageBox()
            mb.setIcon(QtWidgets.QMessageBox.Warning)
            mb.setWindowTitle(title)
            mb.setText(mes)
            mb.setStandardButtons(QtWidgets.QMessageBox.Ok)
            mb.resize(600,600)
            mb.setWindowIcon(QtGui.QIcon("r15.jpg"))
            #mb.setStyleSheet("background:url(qtimage/r6.jpg)")


            """mb.setMinimumHeight(1000)
            mb.setMinimumWidth(1000)
            mb.setSizeIncrement(1,1)
            mb.setSizeGripEnabled(True)"""
            mb.exec()

        def click(self):
            kullanıcı=self.lineEdit.text()
            parola=self.lineEdit_2.text()
            if kullanıcı=="admin" and parola=="admin":
               #sys.exit.QtWidgets.QApplication(sys.argv)
               grnt()


            else:
                self.showmes('SOBE YAZILIM','LUTFEN GIRIS BILGILERINIZI KONTROL EDINIZ')

    import images_rc
    if __name__ == "__main__":
        app = QtWidgets.QApplication(sys.argv)
        Form = QtWidgets.QWidget()
        ui = Ui_Form()
        ui.setupUi(Form)
        Form.show()
        app.exec_()
        #QtWidgets.QApplication(sys.argv).exec_()
        #sys.exit(app.exec_())


def tomail (il,nesne,gr):
    mesaj=EmailMessage()
    mesaj["Subject"]=il+" MERKEZ HALKBANK KIRMIZI ALARM"
    mesaj["From"]="#gönderici e-posta"
    mesaj["To"]="#alıcı e-posta"
    mesaj.set_content(gr+" SOYGUN")
    with open("utest/"+nesne+"3.jpg","rb") as f:
             image_data=f.read()
             image_name=f.name
             image_type=imghdr.what(f.name)

    mesaj.add_attachment(image_data,maintype="image",subtype=image_type,filename=image_name)
    with smtplib.SMTP_SSL("smtp.gmail.com",465) as smtp:
             smtp.login("#gönderici e-posta", "#şifre")
             smtp.send_message(mesaj)

def grnt():
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

    g = 1
    k = 1
    sayac = 0
    ret = video.set(3, 1280)
    ret = video.set(4, 720)
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

            if  np.squeeze(classes).astype(np.int32)[0]==2 and np.squeeze(scores)[0]*100>90 and g<8 :
                cv2.imwrite("utest\gun{}.jpg".format(g), frame)
                g=g+1
                if g==6:
                sayac += 1
                    il="BURSA"
                    nesne="gun"
                    gr="SİLAHLI"
                    tomail(il,nesne,gr)

            if np.squeeze(classes).astype(np.int32)[0]==3 and np.squeeze(scores)[0]*100>90 and k<8 :
                cv2.imwrite("utest\knife{}.jpg".format(k), frame)
                k=k+1
                if k==6:
                sayac += 1
                    il = "KARABÜK"
                    nesne = "knife"
                    gr = "BIÇAKLI"
                    tomail(il,nesne,gr)

            if cv2.waitKey(200) == ord('q'):
                sys.exit.QtWidgets.QApplication(sys.argv)
                break

    video.release()
    cv2.destroyAllWindows()

panel()



