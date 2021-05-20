import cv2
import datetime
import locale
import sys

from PyQt5 import QtCore, QtGui, QtWidgets


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
                gr()
               #sys.exit.QtWidgets.QApplication(sys.argv)

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

def gr():

     kamera = cv2.VideoCapture(0)  # 0 kamera sayısını verir ve 0 webcam numarasıdır.fazla ise ona göre veririz.
     # 0 yerine deneme.mp4 yazarsak bu videoyu oynatır.
     """
     #kamera.set(cv2.CAP_PROP_FRAME_WIDTH,320)
     #kamera.set(cv2.CAP_PROP_FRAME_HEIGHT,240)
     #açılan pencerenin çerçeve boyutunu ayarlıyoruz.
     """
     kamera.set(cv2.CAP_PROP_FRAME_WIDTH, 850)
     kamera.set(cv2.CAP_PROP_FRAME_HEIGHT, 720)
     a = 0

     while True:
        ret, goruntu = kamera.read()
        # griton=cv2.cvtColor(goruntu,cv2.COLOR_BGR2GRAY)#görüntüyü gri yapar.
        """
        #ret=kamera.set(3,320)
        #ret=kamera.set(4,240)
        #yukarıda yaptığmız boyutlandırmanın ikinci yolu  
        """
        locale.setlocale(locale.LC_ALL, 'turkish')
        an = datetime.datetime.now()
        tarih = datetime.datetime.strftime(an, '%c')
        fontscale = 1.0
        color = (0, 0, 255)
        fontface = cv2.FONT_HERSHEY_COMPLEX_SMALL
        cv2.putText(goruntu, tarih + " \t " + "kk", (25, 40), fontface, fontscale, color)
        cv2.putText(goruntu, "KAMERA 01", (500, 40), fontface, fontscale, color)
        cv2.imshow('Video', goruntu)
        #cv2.imshow('GriTon',griton)
        if cv2.waitKey(100) & 0xFF == ord('q'):
            sys.exit.QtWidgets.QApplication(sys.argv)
            break
     kamera.release()
     cv2.destroyAllWindows()


if __name__ == "__main__":
 panel()
 #gr()
