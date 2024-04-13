import sys
import calc as c 
import mathlib as ml

# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'calcc.ui'
#
# Created by: PyQt5 UI code generator 5.14.1
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow, QMessageBox

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        self.operation_buffer = ""
        self.argumentA = 0.0
        self.argumentB = 0.0
        self.isArgumentASet = False
        self.isArgumentBSet = False
        self.show_notification = ""
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(465, 718)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.vysledekPole = QtWidgets.QLabel(self.centralwidget)
        self.vysledekPole.setGeometry(QtCore.QRect(10, 10, 441, 101))
        font = QtGui.QFont()
        font.setPointSize(40)
        self.vysledekPole.setFont(font)
        self.vysledekPole.setFrameShape(QtWidgets.QFrame.Box)
        self.vysledekPole.setFrameShadow(QtWidgets.QFrame.Plain)
        self.vysledekPole.setLineWidth(3)
        self.vysledekPole.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.vysledekPole.setObjectName("vysledekPole")
        self.pushButton_3 = QtWidgets.QPushButton(self.centralwidget, clicked = lambda: self.pressButton("0"))
        self.pushButton_3.setGeometry(QtCore.QRect(110, 610, 71, 61))
        font = QtGui.QFont()
        font.setPointSize(35)
        self.pushButton_3.setFont(font)
        self.pushButton_3.setObjectName("pushButton_3")
        self.pushButton_4 = QtWidgets.QPushButton(self.centralwidget, clicked = lambda: self.pressButton("."))
        self.pushButton_4.setGeometry(QtCore.QRect(200, 610, 71, 61))
        font = QtGui.QFont()
        font.setPointSize(35)
        self.pushButton_4.setFont(font)
        self.pushButton_4.setObjectName("pushButton_4")
        self.pushButton_5 = QtWidgets.QPushButton(self.centralwidget, clicked = lambda: self.arithmeticButtonPress("mod"))
        self.pushButton_5.setGeometry(QtCore.QRect(20, 610, 71, 61))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.pushButton_5.setFont(font)
        self.pushButton_5.setObjectName("pushButton_5")
        self.pushButton_6 = QtWidgets.QPushButton(self.centralwidget, clicked = lambda: self.resetBuffers())
        self.pushButton_6.setGeometry(QtCore.QRect(290, 370, 71, 61))
        font = QtGui.QFont()
        font.setPointSize(35)
        self.pushButton_6.setFont(font)
        self.pushButton_6.setObjectName("pushButton_6")
        self.pushButton_7 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_7.clicked.connect(self.getResult)
        self.pushButton_7.setGeometry(QtCore.QRect(380, 610, 71, 61))
        font = QtGui.QFont()
        font.setPointSize(35)
        self.pushButton_7.setFont(font)
        self.pushButton_7.setObjectName("pushButton_7")
        self.pushButton_8 = QtWidgets.QPushButton(self.centralwidget, clicked = lambda: self.pressButton("1"))
        self.pushButton_8.setGeometry(QtCore.QRect(20, 530, 71, 61))
        font = QtGui.QFont()
        font.setPointSize(35)
        self.pushButton_8.setFont(font)
        self.pushButton_8.setObjectName("pushButton_8")
        self.pushButton_9 = QtWidgets.QPushButton(self.centralwidget, clicked = lambda: self.pressButton("2"))
        self.pushButton_9.setGeometry(QtCore.QRect(110, 530, 71, 61))
        font = QtGui.QFont()
        font.setPointSize(35)
        self.pushButton_9.setFont(font)
        self.pushButton_9.setObjectName("pushButton_9")
        self.pushButton_10 = QtWidgets.QPushButton(self.centralwidget, clicked = lambda: self.pressButton("3"))
        self.pushButton_10.setGeometry(QtCore.QRect(200, 530, 71, 61))
        font = QtGui.QFont()
        font.setPointSize(35)
        self.pushButton_10.setFont(font)
        self.pushButton_10.setObjectName("pushButton_10")
        self.pushButton_13 = QtWidgets.QPushButton(self.centralwidget, clicked = lambda: self.pressButton("4"))
        self.pushButton_13.setGeometry(QtCore.QRect(20, 450, 71, 61))
        font = QtGui.QFont()
        font.setPointSize(35)
        self.pushButton_13.setFont(font)
        self.pushButton_13.setObjectName("pushButton_13")
        self.pushButton_14 = QtWidgets.QPushButton(self.centralwidget, clicked = lambda: self.pressButton("5"))
        self.pushButton_14.setGeometry(QtCore.QRect(110, 450, 71, 61))
        font = QtGui.QFont()
        font.setPointSize(35)
        self.pushButton_14.setFont(font)
        self.pushButton_14.setObjectName("pushButton_14")
        self.pushButton_15 = QtWidgets.QPushButton(self.centralwidget, clicked = lambda: self.pressButton("6"))
        self.pushButton_15.setGeometry(QtCore.QRect(200, 450, 71, 61))
        font = QtGui.QFont()
        font.setPointSize(35)
        self.pushButton_15.setFont(font)
        self.pushButton_15.setObjectName("pushButton_15")
        self.pushButton_16 = QtWidgets.QPushButton(self.centralwidget, clicked = lambda: self.pressButton("7"))
        self.pushButton_16.setGeometry(QtCore.QRect(20, 370, 71, 61))
        font = QtGui.QFont()
        font.setPointSize(35)
        self.pushButton_16.setFont(font)
        self.pushButton_16.setObjectName("pushButton_16")
        self.pushButton_17 = QtWidgets.QPushButton(self.centralwidget, clicked = lambda: self.pressButton("8"))
        self.pushButton_17.setGeometry(QtCore.QRect(110, 370, 71, 61))
        font = QtGui.QFont()
        font.setPointSize(35)
        self.pushButton_17.setFont(font)
        self.pushButton_17.setObjectName("pushButton_17")
        self.pushButton_18 = QtWidgets.QPushButton(self.centralwidget, clicked = lambda: self.pressButton("9"))
        self.pushButton_18.setGeometry(QtCore.QRect(200, 370, 71, 61))
        font = QtGui.QFont()
        font.setPointSize(35)
        self.pushButton_18.setFont(font)
        self.pushButton_18.setObjectName("pushButton_18")
        self.pushButton_19 = QtWidgets.QPushButton(self.centralwidget, clicked = lambda: self.arithmeticButtonPress("+"))
        self.pushButton_19.setGeometry(QtCore.QRect(380, 450, 71, 61))
        font = QtGui.QFont()
        font.setPointSize(35)
        self.pushButton_19.setFont(font)
        self.pushButton_19.setObjectName("pushButton_19")
        self.pushButton_20 = QtWidgets.QPushButton(self.centralwidget, clicked = lambda: self.arithmeticButtonPress("-"))
        self.pushButton_20.setGeometry(QtCore.QRect(380, 530, 71, 61))
        font = QtGui.QFont()
        font.setPointSize(35)
        self.pushButton_20.setFont(font)
        self.pushButton_20.setObjectName("pushButton_20")
        self.pushButton_21 = QtWidgets.QPushButton(self.centralwidget, clicked = lambda: self.arithmeticButtonPress("×"))
        self.pushButton_21.setGeometry(QtCore.QRect(290, 450, 71, 61))
        font = QtGui.QFont()
        font.setPointSize(35)
        self.pushButton_21.setFont(font)
        self.pushButton_21.setObjectName("pushButton_21")
        self.pushButton_22 = QtWidgets.QPushButton(self.centralwidget, clicked = lambda: self.arithmeticButtonPress("÷"))
        self.pushButton_22.setGeometry(QtCore.QRect(290, 530, 71, 61))
        font = QtGui.QFont()
        font.setPointSize(35)
        self.pushButton_22.setFont(font)
        self.pushButton_22.setObjectName("pushButton_22")
        self.pushButton_23 = QtWidgets.QPushButton(self.centralwidget, clicked = lambda: self.arithmeticButtonPress("ⁿ√x"))
        self.pushButton_23.setGeometry(QtCore.QRect(20, 290, 71, 61))
        font = QtGui.QFont()
        font.setPointSize(30)
        self.pushButton_23.setFont(font)
        self.pushButton_23.setObjectName("pushButton_23")
        self.pushButton_24 = QtWidgets.QPushButton(self.centralwidget, clicked = lambda: self.arithmeticButtonPress("x²"))
        self.pushButton_24.setGeometry(QtCore.QRect(110, 290, 71, 61))
        font = QtGui.QFont()
        font.setPointSize(30)
        self.pushButton_24.setFont(font)
        self.pushButton_24.setObjectName("pushButton_24")
        self.pushButton_25 = QtWidgets.QPushButton(self.centralwidget, clicked = lambda: self.getResultUnary("!"))
        self.pushButton_25.setGeometry(QtCore.QRect(290, 610, 71, 61))
        font = QtGui.QFont()
        font.setPointSize(30)
        self.pushButton_25.setFont(font)
        self.pushButton_25.setObjectName("pushButton_25")
        self.pushButton_26 = QtWidgets.QPushButton(self.centralwidget, clicked = lambda: self.getResultUnary("⌫"))
        self.pushButton_26.setGeometry(QtCore.QRect(380, 370, 71, 61))
        font = QtGui.QFont()
        font.setPointSize(30)
        self.pushButton_26.setFont(font)
        self.pushButton_26.setObjectName("pushButton_26")
        self.pushButton_27 = QtWidgets.QPushButton(self.centralwidget, clicked = lambda: self.getResultUnary("+/-"))
        self.pushButton_27.setGeometry(QtCore.QRect(200, 290, 71, 61))
        font = QtGui.QFont()
        font.setPointSize(30)
        self.pushButton_27.setFont(font)
        self.pushButton_27.setObjectName("pushButton_27")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(6, -8, 451, 681))
        self.label.setText("")
        self.label.setPixmap(QtGui.QPixmap("pictures/testwallpaper.jpg"))
        self.label.setScaledContents(True)
        self.label.setObjectName("label")
        self.label.raise_()
        self.vysledekPole.raise_()
        self.pushButton_3.raise_()
        self.pushButton_4.raise_()
        self.pushButton_5.raise_()
        self.pushButton_6.raise_()
        self.pushButton_7.raise_()
        self.pushButton_8.raise_()
        self.pushButton_9.raise_()
        self.pushButton_10.raise_()
        self.pushButton_13.raise_()
        self.pushButton_14.raise_()
        self.pushButton_15.raise_()
        self.pushButton_16.raise_()
        self.pushButton_17.raise_()
        self.pushButton_18.raise_()
        self.pushButton_19.raise_()
        self.pushButton_20.raise_()
        self.pushButton_21.raise_()
        self.pushButton_22.raise_()
        self.pushButton_23.raise_()
        self.pushButton_24.raise_()
        self.pushButton_25.raise_()
        self.pushButton_26.raise_()
        self.pushButton_27.raise_()
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 465, 21))
        self.menubar.setObjectName("menubar")
        self.menuSkins = QtWidgets.QMenu(self.menubar)
        self.menuSkins.setObjectName("menuSkins")
        self.menuSkins_2 = QtWidgets.QMenu(self.menubar)
        self.menuSkins_2.setObjectName("menuSkins_2")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.actionBasic = QtWidgets.QAction(MainWindow)
        self.actionBasic.setObjectName("actionBasic")
        self.menuSkins.addAction(self.actionBasic)
        self.menubar.addAction(self.menuSkins.menuAction())
        self.menubar.addAction(self.menuSkins_2.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "SwagAnimeDripCalculator 1.0"))
        self.vysledekPole.setText(_translate("MainWindow", "0"))
        self.pushButton_3.setText(_translate("MainWindow", "0"))
        self.pushButton_4.setText(_translate("MainWindow", ","))
        self.pushButton_5.setText(_translate("MainWindow", "mod"))
        self.pushButton_6.setText(_translate("MainWindow", "C"))
        self.pushButton_7.setText(_translate("MainWindow", "="))
        self.pushButton_8.setText(_translate("MainWindow", "1"))
        self.pushButton_9.setText(_translate("MainWindow", "2"))
        self.pushButton_10.setText(_translate("MainWindow", "3"))
        self.pushButton_13.setText(_translate("MainWindow", "4"))
        self.pushButton_14.setText(_translate("MainWindow", "5"))
        self.pushButton_15.setText(_translate("MainWindow", "6"))
        self.pushButton_16.setText(_translate("MainWindow", "7"))
        self.pushButton_17.setText(_translate("MainWindow", "8"))
        self.pushButton_18.setText(_translate("MainWindow", "9"))
        self.pushButton_19.setText(_translate("MainWindow", "+"))
        self.pushButton_20.setText(_translate("MainWindow", "-"))
        self.pushButton_21.setText(_translate("MainWindow", "×"))
        self.pushButton_22.setText(_translate("MainWindow", "÷"))
        self.pushButton_23.setText(_translate("MainWindow", "ⁿ√x"))
        self.pushButton_24.setText(_translate("MainWindow", "x²"))
        self.pushButton_25.setText(_translate("MainWindow", "!"))
        self.pushButton_26.setText(_translate("MainWindow", "⌫"))
        self.pushButton_27.setText(_translate("MainWindow", "+/-"))
        self.menuSkins.setTitle(_translate("MainWindow", "Menu"))
        self.menuSkins_2.setTitle(_translate("MainWindow", "Skins"))
        self.actionBasic.setText(_translate("MainWindow", "Basic"))

    def pressButton(self, pressed):
        
            if self.vysledekPole.text() == "0":
                self.vysledekPole.setText(pressed)
            else:
                self.vysledekPole.setText(self.vysledekPole.text() + pressed)
       

    def arithmeticButtonPress(self, pressed):

        if self.operation_buffer != "":
            self.show_notification("Can't have more than one operation selected at a time")
        

        else:
            self.operation_buffer = pressed
            if self.isArgumentASet == False:
                self.argumentA = self.vysledekPole.text()
                self.isArgumentASet = True
                self.vysledekPole.setText("0")
            elif self.isArgumentBSet == False:
                self.vysledekPole.setText("0")
                
            
    
                
    def getResult(self):
        
        if self.isArgumentBSet == False:
            self.argumentB = self.vysledekPole.text()
            self.isArgumentBSet = True
        print(self.argumentA)
        print(self.argumentB)
        if self.operation_buffer == "":
            self.show_notification("No operation selected")
        elif self.operation_buffer == "+":
            res = ml.add(float(self.argumentA), float(self.argumentB))
            self.vysledekPole.setText(str(res))
        elif self.operation_buffer == "-":
            res = ml.sub(float(self.argumentA), float(self.argumentB))
            self.vysledekPole.setText(str(res))
        elif self.operation_buffer == "×":
            res = ml.mul(float(self.argumentA), float(self.argumentB))
            self.vysledekPole.setText(str(res))
        elif self.operation_buffer == "÷":
            res = ml.div(float(self.argumentA), float(self.argumentB))
            self.vysledekPole.setText(str(res))
        elif self.operation_buffer == "x²":
            res = ml.pow(float(self.argumentA), float(self.argumentB))
            self.vysledekPole.setText(str(res)) 
        elif self.operation_buffer == "ⁿ√x":
            res = ml.root(float(self.argumentA), float(self.argumentB))
            self.vysledekPole.setText(str(res))
        elif self.operation_buffer == "mod":
            res = ml.modulo(float(self.argumentA), float(self.argumentB))
            self.vysledekPole.setText(str(res))
        else:
            self.show_notification("Invalid operation selected")
        self.argumentA = res
        self.isArgumentASet = True
        self.operation_buffer = ""
        self.argumentB = 0.0
        self.isArgumentBSet = False

        
    def getResultUnary(self, pressed):
        if pressed == "⌫":
            res = ml.backspace(float(self.vysledekPole.text()))
            self.vysledekPole.setText(str(res))
            return
        if self.isArgumentASet == False:
            self.argumentA = self.vysledekPole.text()
            self.isArgumentASet = True
        if pressed == "":
            self.show_notification("No operation selected")
        elif pressed == "!":
            res = ml.fact(float(self.argumentA))
            self.vysledekPole.setText(str(res))
        elif pressed == "+/-":
            res = ml.return_opposite(int(self.argumentA))
            self.vysledekPole.setText(str(res))
        self.argumentA = res
        self.isArgumentASet = True
        self.operation_buffer = ""
        self.argumentB = 0.0
        self.isArgumentBSet = False
        
    def resetBuffers(self):
        self.vysledekPole.setText("0")
        self.operation_buffer = ""
        self.argumentA = 0.0
        self.argumentB = 0.0
        self.isArgumentASet = False
        self.isArgumentBSet = False
        

class CalculatorWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = CalculatorWindow()
    window.show()
    sys.exit(app.exec_())