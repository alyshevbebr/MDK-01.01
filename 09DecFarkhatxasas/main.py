# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'tablewid.ui'
#
# Created by: PyQt5 UI code generator 5.15.11
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(548, 407)
        self.tableWidget = QtWidgets.QTableWidget(Form)
        self.tableWidget.setGeometry(QtCore.QRect(10, 100, 521, 231))
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(4)
        self.tableWidget.setRowCount(2)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(3, item)
        self.knopka_add = QtWidgets.QPushButton(Form)
        self.knopka_add.setGeometry(QtCore.QRect(60, 360, 91, 23))
        self.knopka_add.setObjectName("knopka_add")
        self.knopka_delete = QtWidgets.QPushButton(Form)
        self.knopka_delete.setGeometry(QtCore.QRect(210, 360, 101, 23))
        self.knopka_delete.setObjectName("knopka_delete")
        self.knopka_upd = QtWidgets.QPushButton(Form)
        self.knopka_upd.setGeometry(QtCore.QRect(380, 360, 101, 23))
        self.knopka_upd.setObjectName("knopka_upd")
        self.label = QtWidgets.QLabel(Form)
        self.label.setGeometry(QtCore.QRect(150, 50, 221, 31))
        self.label.setMouseTracking(False)
        self.label.setTabletTracking(False)
        self.label.setStyleSheet("font: 75 16pt \"Times New Roman\";")
        self.label.setObjectName("label")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Главное окно"))
        item = self.tableWidget.verticalHeaderItem(0)
        item.setText(_translate("Form", "1"))
        item = self.tableWidget.verticalHeaderItem(1)
        item.setText(_translate("Form", "2"))
        item = self.tableWidget.horizontalHeaderItem(0)
        item.setText(_translate("Form", "Фамилия"))
        item = self.tableWidget.horizontalHeaderItem(1)
        item.setText(_translate("Form", "Имя"))
        item = self.tableWidget.horizontalHeaderItem(2)
        item.setText(_translate("Form", "Логин"))
        item = self.tableWidget.horizontalHeaderItem(3)
        item.setText(_translate("Form", "Пароль"))
        self.knopka_add.setText(_translate("Form", "Добавить"))
        self.knopka_delete.setText(_translate("Form", "Удалить"))
        self.knopka_upd.setText(_translate("Form", "Обновить"))
        self.label.setText(_translate("Form", "              Пользователи"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())