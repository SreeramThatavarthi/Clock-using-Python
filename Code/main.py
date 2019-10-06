# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'untitled.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets
import os
from pathlib import Path

class Ui_mainpage_home(object):
    def open_timer(self):
        pat_timer=str(Path(__file__).parent.absolute())+"\\Final_build\\show_timer.exe"
        os.startfile(pat_timer)
    def open_time(self):
        pat_time=str(Path(__file__).parent.absolute())+"\\Final_build\\show_time.exe"
        os.startfile(pat_time)
        print(str(Path(__file__).parent.absolute()))
        

    def setupUi(self, mainpage_home):
        mainpage_home.setObjectName("mainpage_home")
        mainpage_home.resize(359, 314)
        self.centralwidget = QtWidgets.QWidget(mainpage_home)
        self.centralwidget.setObjectName("centralwidget")
        self.time_button = QtWidgets.QPushButton(self.centralwidget)
        self.time_button.setGeometry(QtCore.QRect(90, 110, 181, 51))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.time_button.setFont(font)
        self.time_button.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"color: rgb(255, 0, 0);")
        self.time_button.setObjectName("time_button")
        self.time_button.clicked.connect(self.open_time)
        self.timer_button = QtWidgets.QPushButton(self.centralwidget)
        self.timer_button.setGeometry(QtCore.QRect(90, 180, 181, 51))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.timer_button.setFont(font)
        self.timer_button.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"color: rgb(255, 0, 0);")
        self.timer_button.setObjectName("timer_button")
        self.timer_button.clicked.connect(self.open_timer)
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(-4, -8, 361, 81))
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
        mainpage_home.setCentralWidget(self.centralwidget)

        self.retranslateUi(mainpage_home)
        QtCore.QMetaObject.connectSlotsByName(mainpage_home)

    def retranslateUi(self, mainpage_home):
        _translate = QtCore.QCoreApplication.translate
        mainpage_home.setWindowTitle(_translate("mainpage_home", "MainWindow"))
        self.time_button.setText(_translate("mainpage_home", "Show Time"))
        self.timer_button.setText(_translate("mainpage_home", "Set Timer"))
        self.label.setText(_translate("mainpage_home", "TIME APP"))
        self.label_2.setText(_translate("mainpage_home", "@Sreeram"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    mainpage_home = QtWidgets.QMainWindow()
    ui = Ui_mainpage_home()
    ui.setupUi(mainpage_home)
    mainpage_home.show()
    sys.exit(app.exec_())
