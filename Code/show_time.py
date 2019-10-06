# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'untitle.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets
import datetime
import time as tt



class Ui_time(object):
    def setupUi(self, time):
        time.setObjectName("time")
        time.resize(357, 314)
        self.centralwidget = QtWidgets.QWidget(time)
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
        self.label_3.setGeometry(QtCore.QRect(-10, 50, 371, 231))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(36)
        font.setBold(True)
        font.setWeight(75)
        self.label_3.setFont(font)
        self.label_3.setStyleSheet("color: rgb(255, 0, 0);\n"
"background-color: rgb(255, 255, 255);")
        self.label_3.setTextFormat(QtCore.Qt.PlainText)
        self.label_3.setAlignment(QtCore.Qt.AlignCenter)
        self.label_3.setObjectName("label_3")
        time.setCentralWidget(self.centralwidget)

        self.retranslateUi(time)
        QtCore.QMetaObject.connectSlotsByName(time)

    def retranslateUi(self, time):
        _translate = QtCore.QCoreApplication.translate
        time.setWindowTitle(_translate("time", "Time "))
        self.label.setText(_translate("time", "TIME"))
        self.label_2.setText(_translate("time", "@Sreeram"))
        self.label_3.setText(_translate("time", "00:00:00"))   

    def function(self):
            now = datetime.datetime.now()
            times=str(now.strftime("%H:%M:%S"))
            self.label_3.setText(times)
            


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    time = QtWidgets.QMainWindow()
    ui = Ui_time()
    ui.setupUi(time)
    timer =QtCore.QTimer()
    timer.timeout.connect(ui.function)
    timer.start(1000)
    time.show()
    sys.exit(app.exec_())
   
    
