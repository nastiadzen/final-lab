from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("ЗАВДАННЯ 4")
        Dialog.resize(300, 300)
        Dialog.setStyleSheet("background-color: rgb(6, 13, 48);")
        self.label = QtWidgets.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(10, 10, 280, 71))
        font = QtGui.QFont()
        font.setPointSize(18)
        self.label.setFont(font)
        self.label.setStyleSheet("color: rgb(161, 161, 161);")
        self.label.setFrameShape(QtWidgets.QFrame.Box)
        self.label.setLineWidth(5)
        self.label.setObjectName("label")
        self.pushButton = QtWidgets.QPushButton(Dialog)
        self.pushButton.setGeometry(QtCore.QRect(100, 120, 101, 23))
        self.pushButton.setStyleSheet("\n"
"background-color:  rgb(161, 161, 161)")
        self.pushButton.setObjectName("pushButton")
        self.pushButton_2 = QtWidgets.QPushButton(Dialog)
        self.pushButton_2.setGeometry(QtCore.QRect(100, 160, 101, 23))
        self.pushButton_2.setStyleSheet("\n"
"background-color:  rgb(161, 161, 161)")
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_3 = QtWidgets.QPushButton(Dialog)
        self.pushButton_3.setGeometry(QtCore.QRect(110, 240, 75, 23))
        self.pushButton_3.setStyleSheet("\n"
"background-color:  rgb(161, 161, 161)")
        self.pushButton_3.setObjectName("pushButton_3")
        self.pushButton_4 = QtWidgets.QPushButton(Dialog)
        self.pushButton_4.setGeometry(QtCore.QRect(105, 190, 90, 23))
        self.pushButton_4.setStyleSheet("\n"
"background-color:  rgb(161, 161, 161)")
        self.pushButton_4.setObjectName("pushButton_4")
        self.pushButton_5 = QtWidgets.QPushButton(Dialog)
        self.pushButton_5.setGeometry(QtCore.QRect(11, 190, 82, 23))
        self.pushButton_5.setStyleSheet("\n"
"background-color:  rgb(161, 161, 161)")
        self.pushButton_5.setObjectName("pushButton_5")
        self.pushButton_6 = QtWidgets.QPushButton(Dialog)
        self.pushButton_6.setGeometry(QtCore.QRect(210, 190, 77, 23))
        self.pushButton_6.setStyleSheet("\n"
"background-color:  rgb(161, 161, 161)")
        self.pushButton_6.setObjectName("pushButton_6")
        self.label_2 = QtWidgets.QLabel(Dialog)
        self.label_2.setGeometry(QtCore.QRect(10, 270, 221, 20))
        self.label_2.setStyleSheet("color: rgb(161, 161, 161)")
        self.label_2.setObjectName("label_2")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("1", "Завдання 4"))
        self.label.setText(_translate("Dialog", "             Menu"))
        self.pushButton.setText(_translate("Dialog", "Курс гривні "))
        self.pushButton_2.setText(_translate("Dialog", "Аналіз зміни курсу "))
        self.pushButton_4.setText(_translate("Dialog", " Створити .txt "))
        self.pushButton_5.setText(_translate("Dialog", " Створити JSON "))
        self.pushButton_6.setText(_translate("Dialog", " Створити Exel "))
        self.pushButton_3.setText(_translate("Dialog", "Вихід"))
        self.label_2.setText(_translate("Dialog", "Автор: Дзендзелівська Анастасія ФІТ 1-7"))



