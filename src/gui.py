'''**************************************************************************************************
*   Project: IVS project 2 (Calculator)
*
*   File:           gui.py
*   Description:    This file contains the implementation of our calculator GUI and also the backend
*
*   Last change:    23.04.2024
*   Date:           23.04.2024
*   Author:         Martin Vaculik (xvaculm00)
**************************************************************************************************'''
##
# @file gui.py
# @author Martin Vaculik (xvaculm00)
# @brief Implementation of gui for calculator and connecting it with backend








import sys
import calc as c 
import mathlib as ml
import decimal
import buttons as b 



from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow, QAction, QVBoxLayout, QWidget, QLabel, QSpinBox, QPushButton, QDialog
##
# @brief Class that sets up the UI of the calculator
class Ui_MainWindow(object):
    ##
    # @brief Function that sets up the UI of the calculator
    # @param self: self parameter
    # @param MainWindow: The main window of the calculator
    # @return None
    def setupUi(self, MainWindow):
        #Icon defined
        icon = QtGui.QIcon("/usr/share/pictures/kure112.png")
        MainWindow.setWindowIcon(icon)



        #Variables
        self.operation_buffer = ""
        self.argumentA = 0.0
        self.argumentB = 0.0
        self.isArgumentASet = False
        self.isArgumentBSet = False
        self.show_notification = ""
        self.floatnumCounter = "{:.6f}"





        #QTDesigner windows, buttons, labels etc.
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
        self.pushButton_24 = QtWidgets.QPushButton(self.centralwidget, clicked = lambda: self.arithmeticButtonPress("xⁿ"))
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
        self.allButons = [self.pushButton_3, self.pushButton_4, self.pushButton_5, self.pushButton_6, self.pushButton_7, self.pushButton_8,
                          self.pushButton_9, self.pushButton_10, self.pushButton_13, self.pushButton_14, self.pushButton_15, self.pushButton_16,
                            self.pushButton_17, self.pushButton_18, self.pushButton_19, self.pushButton_20, self.pushButton_21, self.pushButton_22,
                            self.pushButton_23, self.pushButton_24, self.pushButton_25, self.pushButton_26, self.pushButton_27]
                          










        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(6, -18, 451, 711))
        self.label.setText("")
        #Base wallpaper set 
        self.label.setPixmap(QtGui.QPixmap("/usr/share/pictures/wallpaperbasic.jpg"))
        self.label.setScaledContents(True)
        self.label.setObjectName("label")
        self.label.raise_()
        self.historieVysledku = QtWidgets.QLabel(self.centralwidget)
        self.historieVysledku.setGeometry(QtCore.QRect(20, 20, 411, 20))
        self.historieVysledku.setObjectName("historieVysledku")
        self.historieVysledku.setText("")
        self.historieVysledku.setAlignment(QtCore.Qt.AlignRight)
        self.historieVysledku.setStyleSheet("font-size: 12px; ")
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
        #Bar setup, menu etc.
        self.menubar.setObjectName("menubar")
        self.menu = QtWidgets.QMenu(self.menubar)
        self.menu.setObjectName("menuSkins")
        self.menuSkins = QtWidgets.QMenu(self.menubar)
        self.menuSkins.setObjectName("menuSkins_2")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.actionBasic = QtWidgets.QAction(MainWindow, triggered = lambda: self.changeSkin("Basic"))
        self.actionBasic.setObjectName("actionBasic")
        self.actionDarkMode = QtWidgets.QAction(MainWindow, triggered = lambda: self.changeSkin("Dark Mode"))
        self.actionDarkMode.setObjectName("actionDarkMode")
        self.actionNastaveni = QtWidgets.QAction(MainWindow)
        self.actionNastaveni.setObjectName("actionNastaveni")
        self.actionNastaveni.triggered.connect(self.openSettings)
        self.actionPurpleBlue = QtWidgets.QAction(MainWindow, triggered = lambda: self.changeSkin("Purple Blue"))
        self.actionPurpleBlue.setObjectName("actionPurpleBlue")
        self.actionDarkGreen = QtWidgets.QAction(MainWindow, triggered = lambda: self.changeSkin("Dark Green"))
        self.actionDarkGreen.setObjectName("actionDarkGreen")
        self.actionHelp = QtWidgets.QAction(MainWindow, triggered=self.openHelp)
        self.actionHelp.setObjectName("actionHelp")


        #Adding actions to menus
        self.menuSkins.addAction(self.actionBasic)
        self.menuSkins.addAction(self.actionDarkMode)
        self.menuSkins.addAction(self.actionPurpleBlue)
        self.menuSkins.addAction(self.actionDarkGreen)
        self.menu.addAction(self.actionHelp)
        self.menu.addAction(self.actionNastaveni)
        
        self.menubar.addAction(self.menu.menuAction())
        self.menubar.addAction(self.menuSkins.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
    ##
    # @brief Function that sets up buttons, labels etc.
    # @param self: self parameter
    # @param MainWindow: The main window of the calculator
    # @return None
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
        self.pushButton_24.setText(_translate("MainWindow", "xⁿ"))
        self.pushButton_25.setText(_translate("MainWindow", "!"))
        self.pushButton_26.setText(_translate("MainWindow", "⌫"))
        self.pushButton_27.setText(_translate("MainWindow", "+/-"))
        self.menu.setTitle(_translate("MainWindow", "Menu"))
        self.menuSkins.setTitle(_translate("MainWindow", "Skins"))
        self.actionBasic.setText(_translate("MainWindow", "Basic"))
        self.actionDarkMode.setText(_translate("MainWindow", "Dark Mode"))
        self.actionNastaveni.setText(_translate("MainWindow", "Set Floating Point Precision"))
        self.actionPurpleBlue.setText(_translate("MainWindow", "Purple Blue"))
        self.actionDarkGreen.setText(_translate("MainWindow", "Dark Green"))
        self.actionHelp.setText(_translate("MainWindow", "Help"))

        #Default Skin Set
        self.changeSkin("Basic")
        

    ##
    # @brief Function that reacts to button press and changes our variables and displayed variable
    # @param self: self parameter
    # @param pressed: The button that was pressed
    # @return None 
    def pressButton(self, pressed):
        
            if self.vysledekPole.text() == "0":
                self.vysledekPole.setText(pressed)
            elif pressed == ".":
                if "." in self.vysledekPole.text():
                    return
                else:
                    self.vysledekPole.setText(self.vysledekPole.text() + pressed)
            else:
                self.vysledekPole.setText(self.vysledekPole.text() + pressed)
       
    ##
    # @brief Function that reacts to arithmetic button press, calculates result if necessary
    # @param self: self parameter
    # @param pressed: The button that was pressed
    # @return None 
                

    #We have 3 variables used for operations, argumentA, argumentB and operation_buffer
    def arithmeticButtonPress(self, pressed):
        #Fixes History after error
        errorMessages = ["Cannot divide by zero", "Invalid Power Input", "Invalid Factorial Input", "Cannot root negative number"] 
        for i in errorMessages:
            if self.historieVysledku == "i":
                self.historieVysledku.setText("")
                self.vysledekPole.setText("0")
            


            else:
                self.operation_buffer = pressed
                if self.isArgumentASet == False:
                    self.argumentA = self.vysledekPole.text()
                    self.isArgumentASet = True
                    self.vysledekPole.setText("0")
                    self.historieVysledku.setText(self.argumentA +  self.operation_buffer)
                elif self.isArgumentBSet == False:
                    self.vysledekPole.setText("0")
                    self.historieVysledku.setText(str(self.argumentA) + self.operation_buffer)
                
            
    
    ##
    # @brief Function that gets the result of the operation 
    # @param self: self parameter
    # @return None           
    def getResult(self):
        

        operations = ["+", "-", "×", "÷", "xⁿ", "ⁿ√x", "mod"]
        if self.operation_buffer == "":
            return
        if self.isArgumentBSet == False:
            self.argumentB = self.vysledekPole.text()
            self.isArgumentBSet = True
            self.historieVysledku.setText(self.historieVysledku.text() + self.argumentB)
        print(self.argumentA)
        print(self.argumentB)
        if self.operation_buffer not in operations:
            self.show_notification("Invalid operation selected")
            return
        
        else:
            if self.operation_buffer == "+":
                res = ml.add(float(self.argumentA), float(self.argumentB))
            elif self.operation_buffer == "-":
                res = ml.sub(float(self.argumentA), float(self.argumentB))
            elif self.operation_buffer == "×":
                res = ml.mul(float(self.argumentA), float(self.argumentB))
            elif self.operation_buffer == "÷":
                try:
                    res = ml.div(float(self.argumentA), float(self.argumentB))
                except ZeroDivisionError:
                    self.historieVysledku.setText("Cannot divide by zero")
                    self.resetBuffersNoHistChange()
                    return
            elif self.operation_buffer == "mod":
                try:
                    res = ml.modulo(float(self.argumentA), float(self.argumentB))
                except ZeroDivisionError:
                    self.historieVysledku.setText("Cannot divide by zero")
                    self.resetBuffersNoHistChange()
                    return
            elif self.operation_buffer == "xⁿ":
                    try:
                        res = ml.pow(float(self.argumentA), float(self.argumentB))
                    except ValueError:
                        self.historieVysledku.setText("Invalid Power Input")
                        self.resetBuffersNoHistChange()
                        return
            elif self.operation_buffer == "ⁿ√x":
                try:
                    res = ml.root(float(self.argumentA), float(self.argumentB))
                except ValueError:
                    self.historieVysledku.setText("Cannot root negative number")
                    self.resetBuffersNoHistChange()
                    return
            resShown = str(res)
            if decimal.Decimal(res).as_tuple().exponent < -5:
                resShown = self.floatnumCounter.format(res)
            self.vysledekPole.setText(str(resShown))
            if len(str(resShown)) > 12:
                print("Here")
                resShown = decimal.Decimal(resShown)
                resShown = format(resShown, '.6e')
                self.vysledekPole.setText(str(resShown))
            resShown = 0.0
            self.argumentA = res
            self.isArgumentASet = True
            self.operation_buffer = ""
            self.argumentB = 0.0
            self.isArgumentBSet = False
            self.historieVysledku.setText(self.historieVysledku.text() + " = " + self.vysledekPole.text())

    ##
    # @brief Function that calculates result of unary operations and changes variables accordingly
    # @param self: self parameter
    # @param pressed: The button that was pressed
    # @return None
    def getResultUnary(self, pressed):
        
        
            
        
        if pressed == "⌫":
            res = c.backspace(str(self.vysledekPole.text()))
            self.vysledekPole.setText(str(res))
            print(res)
            return
        if self.isArgumentASet == False:
            self.argumentA = self.vysledekPole.text()
            self.isArgumentASet = True
        if pressed == "":
            self.show_notification("No operation selected")
        elif pressed == "!":
            try:
                res = ml.fact(float(self.argumentA))
            except ValueError:
                self.historieVysledku.setText("Invalid Factorial Input")
                self.resetBuffersNoHistChange()
                return
        elif pressed == "+/-":
            res = ml.return_opposite(float(self.argumentA))
            self.vysledekPole.setText(str(res))

        
        resShown = str(res)
        if decimal.Decimal(res).as_tuple().exponent < -5:
            resShown = self.floatnumCounter.format(res)
        self.vysledekPole.setText(str(resShown))
        if len(str(resShown)) > 12:
                print("Here")
                resShown = decimal.Decimal(resShown)
                resShown = format(resShown, '.5e')
                self.vysledekPole.setText(str(resShown))
        if pressed =="!":
            self.historieVysledku.setText(str(self.argumentA) + "! =" + self.vysledekPole.text())


        
        resShown = 0.0
        self.argumentA = res
        self.isArgumentASet = True
        self.operation_buffer = ""
        self.argumentB = 0.0
        self.isArgumentBSet = False
        

    ##
    # @brief Function that resets buffers and displayed variables
    # @param self: self parameter
    # @return None
    
    def resetBuffers(self):
        self.vysledekPole.setText("0")
        self.operation_buffer = ""
        self.argumentA = 0.0
        self.argumentB = 0.0
        self.isArgumentASet = False
        self.isArgumentBSet = False
        self.historieVysledku.setText("")
        

    ##
    # @brief Function that resets buffers and displayed variables without changing history
    # @param self: self parameter
    # @return None
    def resetBuffersNoHistChange(self):
        self.vysledekPole.setText("0")
        self.operation_buffer = ""
        self.argumentA = 0.0
        self.argumentB = 0.0
        self.isArgumentASet = False
        self.isArgumentBSet = False
    ##
    # @brief Function that shows notification
    # @param self: self parameter
    # @param skin: name of the skin/theme
    def changeSkin(self, skin):
        if skin == "Basic":
            self.label.setPixmap(QtGui.QPixmap("/usr/share/pictures/basicwallpaper.png"))
            self.label.setScaledContents(True)
            self.vysledekPole.setStyleSheet("color: white")
            self.historieVysledku.setStyleSheet("color: white")
            button_style = b.buttonBasic
            
            self.label.pixmap()
            for i in self.allButons:
                    
                     i.setStyleSheet(button_style)

        elif skin == "Dark Mode":
            self.label.setPixmap(QtGui.QPixmap("/usr/share/pictures/blackwallpaper.jpeg"))
            self.label.setScaledContents(True)
            self.vysledekPole.setStyleSheet("color: white")
            self.historieVysledku.setStyleSheet("color: white")
            button_style = b.buttonBasic
            for i in self.allButons:
                
                 i.setStyleSheet(button_style)
               

        elif skin == "Purple Blue":
            self.label.setPixmap(QtGui.QPixmap("/usr/share/pictures/wallpaperpurpleblue.PNG"))
            self.label.setScaledContents(True)
            self.vysledekPole.setStyleSheet("color: white")
            self.historieVysledku.setStyleSheet("color: white")
            button_style = b.buttonPurple
            for i in self.allButons:
                
                 i.setStyleSheet(button_style)


        elif skin == "Dark Green":
            self.label.setPixmap(QtGui.QPixmap("/usr/share/pictures/wallpaperdarkgreen.PNG"))
            self.label.setScaledContents(True)
            self.vysledekPole.setStyleSheet("color: white")
            self.historieVysledku.setStyleSheet("color: white")
            button_style = b.buttonDarkGreen
            for i in self.allButons:
                
                 i.setStyleSheet(button_style)
    def openSettings(self, QDialog):
        dialog = SettingsDialog()
        dialog.exec_()
        decimal_places = dialog.getDecimalPlaces()
        self.floatnumCounter = "{:." + str(decimal_places) + "f}"
    def openHelp(self):
        dialog = HelpDialog()
        dialog.exec_()
        

    
##
# @brief Class that sets up the settings dialog     
class SettingsDialog(QDialog):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Set Floating Point Precision")
        self.initUI()
    ##
    # @brief Function that sets up the UI of the settings dialog
    # @param self: self parameter
    # @return None
    def initUI(self):
        layout = QVBoxLayout()

        self.label = QLabel("Set the number of decimal places:")
        layout.addWidget(self.label)

        self.decimalSpinBox = QSpinBox()
        self.decimalSpinBox.setMinimum(0)
        self.decimalSpinBox.setMaximum(10)
        self.decimalSpinBox.setValue(6)  
        layout.addWidget(self.decimalSpinBox)

        self.okButton = QPushButton("OK")
        self.okButton.clicked.connect(self.accept)
        layout.addWidget(self.okButton)

        self.setLayout(layout)
    ##
    # @brief Function that returns the number of decimal places
    # @param self: self parameter
    # @return int: number of decimal places
    def getDecimalPlaces(self):
        return self.decimalSpinBox.value()







##
# @brief Class that sets up the help dialog
class HelpDialog(QDialog):
    ##
    # @brief init and superinnit of the class
    # @param self: self parameter
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Help")
        self.initUI()
    ##
    # @brief Function that sets up the UI of the help dialog
    # @param self: self parameter
    def initUI(self):
        layout = QVBoxLayout()

        self.label = QLabel()
        self.label.setText("""
        To use the calculator, you can use a keyboard for basic functions or press the available buttons with a mouse.
        The calculator takes in one number at a time.

        The following arithmetic operations are available:
        - Addition
        - Subtraction
        - Multiplication
        - Division
        - Modulo
        - Factorial
        - Square root of a number
        - Number to the power of x

        Binary operations can be used like this:
        - Enter the 1st number
        - Select the binary operation
        - Enter the 2nd number

        Unary operations can be used like this:
        - Enter a number
        - Select the unary operation
        """)
        
        self.label.setStyleSheet("border: 1px solid black; padding: 10px;")
        layout.addWidget(self.label)

        self.okButton = QPushButton("OK")
        self.okButton.clicked.connect(self.accept)
        layout.addWidget(self.okButton)

        self.setLayout(layout)
\
















#This is the main function that runs the calculator
##
# @brief Main function that runs the calculator
class CalculatorWindow(QMainWindow):
    ##
    # @brief init and superinnit of the class
    # @param self: self parameter
    # @return None
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

    ##
    # @brief Function that reacts to key press events
    # @param self: self parameter
    # @param e: the key that was pressed
    def keyPressEvent(self, e):
        events_dict = { "+": "+",
                        "-": "-",
                        "*": "×",
                        "/": "÷"
                       }
        unary = ["!"]
        numbers = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9", "."]

        if(e.key() == QtCore.Qt.Key_Backspace):
            self.ui.getResultUnary("⌫")
            return
        for i in events_dict:
            if(e.text() == i):
                i = events_dict[i]
                self.ui.arithmeticButtonPress(i)
        for i in numbers:
            if(e.text() == i):
                self.ui.pressButton(i)
        for i in unary:
            if(e.text() == i):
                self.ui.getResultUnary(i)
        if(e.text() == "=" or e.key() == QtCore.Qt.Key_Return):
            self.ui.getResult()
if __name__ == "__main__":
    #Main function that runs the calculator
    app = QApplication(sys.argv)
    window = CalculatorWindow()
    window.show()
    sys.exit(app.exec_())