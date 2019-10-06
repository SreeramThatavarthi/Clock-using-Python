# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ntitle.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets
import time as tt
import winsound
f=500
d=100

class Ui_homepage(object):

        def timer_code(self):
                hour=self.spinBox.value()
                minu=self.spinBox_2.value()
                sec=self.spinBox_3.value()
                self.when_to_stop=(hour*60*60)+(minu*60)+(sec)
                m, s = divmod(self.when_to_stop, 60)
                h, m = divmod(m, 60)
                time_left = str(h).zfill(2) + ":" + str(m).zfill(2) + ":" + str(s).zfill(2)
                timer.start(1000)
                

        def timer_start(self):
                m, s = divmod(self.when_to_stop, 60)
                h, m = divmod(m, 60)
                time_left = str(h).zfill(2) + ":" + str(m).zfill(2) + ":" + str(s).zfill(2)
                self.label_6.setText(time_left)
                self.when_to_stop -= 1
                if(time_left=="00:00:00"):
                        timer.stop()
                        for i in range(5):
                                winsound.Beep(f,d)
                else:
                        pass
                        
                
                
        def setupUi(self, homepage):
                homepage.setObjectName("homepage")
                homepage.resize(357, 314)
                self.centralwidget = QtWidgets.QWidget(homepage)
                self.centralwidget.setObjectName("centralwidget")
                self.label = QtWidgets.QLabel(self.centralwidget)
                self.label.setGeometry(QtCore.QRect(-4, -8, 361, 61))
                font = QtGui.QFont()
                font.setFamily("Segoe UI")
                font.setPointSize(20)
                font.setBold(True)
                font.setWeight(75)
                self.label.setFont(font)
                self.label.setStyleSheet("background-color: rgb(255, 0, 0);\n"
        "color: rgb(255, 255, 255);")
                self.label.setAlignment(QtCore.Qt.AlignCenter)
                self.label.setObjectName("label")
                self.label_2 = QtWidgets.QLabel(self.centralwidget)
                self.label_2.setGeometry(QtCore.QRect(-4, 290, 371, 31))
                self.label_2.setStyleSheet("background-color: rgb(255, 0, 0);\n"
        "color: rgb(255, 255, 255);")
                self.label_2.setAlignment(QtCore.Qt.AlignCenter)
                self.label_2.setObjectName("label_2")
                self.label_3 = QtWidgets.QLabel(self.centralwidget)
                self.label_3.setGeometry(QtCore.QRect(6, 60, 121, 21))
                font = QtGui.QFont()
                font.setFamily("Segoe UI")
                font.setPointSize(18)
                self.label_3.setFont(font)
                self.label_3.setStyleSheet("background-color: rgb(255, 255, 255);\n"
        "color: rgb(255, 0, 0);")
                self.label_3.setAlignment(QtCore.Qt.AlignCenter)
                self.label_3.setObjectName("label_3")
                self.label_4 = QtWidgets.QLabel(self.centralwidget)
                self.label_4.setGeometry(QtCore.QRect(120, 60, 121, 21))
                font = QtGui.QFont()
                font.setFamily("Segoe UI")
                font.setPointSize(18)
                self.label_4.setFont(font)
                self.label_4.setStyleSheet("background-color: rgb(255, 255, 255);\n"
        "color: rgb(255, 0, 0);")
                self.label_4.setAlignment(QtCore.Qt.AlignCenter)
                self.label_4.setObjectName("label_4")
                self.label_5 = QtWidgets.QLabel(self.centralwidget)
                self.label_5.setGeometry(QtCore.QRect(240, 60, 111, 21))
                font = QtGui.QFont()
                font.setFamily("Segoe UI")
                font.setPointSize(18)
                self.label_5.setFont(font)
                self.label_5.setStyleSheet("background-color: rgb(255, 255, 255);\n"
        "color: rgb(255, 0, 0);")
                self.label_5.setAlignment(QtCore.Qt.AlignCenter)
                self.label_5.setObjectName("label_5")
                self.spinBox = QtWidgets.QSpinBox(self.centralwidget)
                self.spinBox.setGeometry(QtCore.QRect(10, 90, 101, 31))
                font = QtGui.QFont()
                font.setFamily("Segoe UI")
                font.setPointSize(14)
                font.setBold(True)
                font.setWeight(75)
                self.spinBox.setFont(font)
                self.spinBox.setCursor(QtGui.QCursor(QtCore.Qt.IBeamCursor))
                self.spinBox.setObjectName("spinBox")
                self.spinBox_2 = QtWidgets.QSpinBox(self.centralwidget)
                self.spinBox_2.setGeometry(QtCore.QRect(130, 90, 101, 31))
                font = QtGui.QFont()
                font.setFamily("Segoe UI")
                font.setPointSize(14)
                font.setBold(True)
                font.setWeight(75)
                self.spinBox_2.setFont(font)
                self.spinBox_2.setCursor(QtGui.QCursor(QtCore.Qt.IBeamCursor))
                self.spinBox_2.setObjectName("spinBox_2")
                self.spinBox_3 = QtWidgets.QSpinBox(self.centralwidget)
                self.spinBox_3.setGeometry(QtCore.QRect(250, 90, 101, 31))
                font = QtGui.QFont()
                font.setFamily("Segoe UI")
                font.setPointSize(14)
                font.setBold(True)
                font.setWeight(75)
                self.spinBox_3.setFont(font)
                self.spinBox_3.setCursor(QtGui.QCursor(QtCore.Qt.IBeamCursor))
                self.spinBox_3.setObjectName("spinBox_3")
                self.pushButton = QtWidgets.QPushButton(self.centralwidget)
                self.pushButton.setGeometry(QtCore.QRect(130, 130, 101, 31))
                font = QtGui.QFont()
                font.setFamily("Segoe UI")
                font.setPointSize(16)
                font.setBold(True)
                font.setItalic(False)
                font.setWeight(75)
                self.pushButton.setFont(font)
                self.pushButton.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
                self.pushButton.setStyleSheet("background-color: rgb(0, 0, 0);\n"
        "color: rgb(255, 255, 255);")
                self.pushButton.setObjectName("pushButton")
                self.pushButton.clicked.connect(self.timer_code)
                self.label_6 = QtWidgets.QLabel(self.centralwidget)
                self.label_6.setGeometry(QtCore.QRect(10, 170, 331, 61))
                font = QtGui.QFont()
                font.setFamily("Segoe UI")
                font.setPointSize(26)
                font.setBold(True)
                font.setWeight(75)
                self.label_6.setFont(font)
                self.label_6.setStyleSheet("color: rgb(255, 0, 0);\n"
        "background-color: rgb(255, 255, 255);")
                self.label_6.setAlignment(QtCore.Qt.AlignCenter)
                self.label_6.setObjectName("label_6")
                self.label_7 = QtWidgets.QLabel(self.centralwidget)
                self.label_7.setGeometry(QtCore.QRect(10, 240, 331, 41))
                font = QtGui.QFont()
                font.setFamily("Segoe UI")
                font.setPointSize(26)
                font.setBold(False)
                font.setWeight(50)
                self.label_7.setFont(font)
                self.label_7.setStyleSheet("color: rgb(255, 0, 0);\n"
        "background-color: rgb(255, 255, 255);")
                self.label_7.setAlignment(QtCore.Qt.AlignCenter)
                self.label_7.setObjectName("label_7")
                self.frame = QtWidgets.QFrame(self.centralwidget)
                self.frame.setGeometry(QtCore.QRect(-1, 49, 361, 241))
                self.frame.setStyleSheet("color: rgb(255, 255, 255);\n"
        "background-color: rgb(255, 255, 255);")
                self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
                self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
                self.frame.setObjectName("frame")
                self.frame.raise_()
                self.label.raise_()
                self.label_2.raise_()
                self.label_3.raise_()
                self.label_4.raise_()
                self.label_5.raise_()
                self.spinBox.raise_()
                self.spinBox_2.raise_()
                self.spinBox_3.raise_()
                self.pushButton.raise_()
                self.label_6.raise_()
                self.label_7.raise_()
                homepage.setCentralWidget(self.centralwidget)

                self.retranslateUi(homepage)
                QtCore.QMetaObject.connectSlotsByName(homepage)

        def retranslateUi(self, homepage):
                _translate = QtCore.QCoreApplication.translate
                homepage.setWindowTitle(_translate("homepage", "MainWindow"))
                self.label.setText(_translate("homepage", "SET  TIMER"))
                self.label_2.setText(_translate("homepage", "@Sreeram"))
                self.label_3.setText(_translate("homepage", "Hours"))
                self.label_4.setText(_translate("homepage", "Minutes"))
                self.label_5.setText(_translate("homepage", "Seconds"))
                self.pushButton.setText(_translate("homepage", "Start"))
                self.label_6.setText(_translate("homepage", "00:00:00"))
                self.label_7.setText(_translate("homepage", " "))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    homepage = QtWidgets.QMainWindow()
    ui = Ui_homepage()
    ui.setupUi(homepage)
    timer =QtCore.QTimer()
    timer.timeout.connect(ui.timer_start)
    homepage.show()
    sys.exit(app.exec_())
