import sys
from PyQt5 import QtCore, QtGui, QtWidgets
from configFW import Ui_Dialog
from configSW import Ui_OtherWindow
from configSW_1 import Ui_OtherWindow_2

app = QtWidgets.QApplication(sys.argv)

Dialog = QtWidgets.QDialog()
ui = Ui_Dialog()
ui.setupUi(Dialog)
Dialog.show()


def openOtherWindow():
    global OtherWindow_
    OtherWindow = QtWidgets.QDialog()
    ui = Ui_OtherWindow()
    ui.setupUi(OtherWindow)
    Dialog.close()
    OtherWindow.show()

    def returnToMain():
        OtherWindow.close()
        Dialog.show()

    ui.pushButton.clicked.connect(returnToMain)

ui.pushButton.clicked.connect(openOtherWindow)


def openOtherWindow_1():
    global OtherWindow_2
    OtherWindow_2 = QtWidgets.QDialog()
    ui = Ui_OtherWindow_2()
    ui.setupUi(OtherWindow_2)
    Dialog.close()
    OtherWindow_2.show()

    def returnToMain_1():
        OtherWindow_2.close()
        Dialog.show()

    ui.pushButton.clicked.connect(returnToMain_1)


ui.pushButton_2.clicked.connect(openOtherWindow_1)

def openOtherWindow_2():
    global OtherWindow_3
    OtherWindow_3 = QtWidgets.QDialog()
    file = open('new.txt', 'w')
    file.close()

def returnToMain_2():
    OtherWindow_2.close()
    Dialog.show()

    ui.pushButton.clicked.connect(returnToMain_2)


ui.pushButton_4.clicked.connect(openOtherWindow_2)


def openOtherWindow_3():
    global OtherWindow_4
    OtherWindow_4 = QtWidgets.QDialog()
    file = open('new.xlsx', 'w')
    file.close()

def returnToMain_3():
    OtherWindow_3.close()
    Dialog.show()

    ui.pushButton.clicked.connect(returnToMain_3)


ui.pushButton_6.clicked.connect(openOtherWindow_3)

def openOtherWindow_4():
    global OtherWindow_5
    OtherWindow_5 = QtWidgets.QDialog()
    file = open('new.json', 'w')
    file.close()

def returnToMain_4():
    OtherWindow_3.close()
    Dialog.show()

    ui.pushButton.clicked.connect(returnToMain_4)


ui.pushButton_5.clicked.connect(openOtherWindow_4)
        

def exits():
    Dialog.close()

ui.pushButton_3.clicked.connect(exits)

sys.exit(app.exec_())