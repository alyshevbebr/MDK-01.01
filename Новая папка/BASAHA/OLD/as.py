from PyQt5 import QtWidgets
import qwerty

class MyWindow(QtWidgets.QWidget):
    def __init__(self):
        QtWidgets.QWidget.__init__(self)
        self.ui = qwerty.Ui_Form()
        self.ui.setupUi(self)
        self.ui.pushButton.clicked.connect(self.sum)
        self.ui.pushButton_2.clicked.connect(self.clear)

    def sum(self):
        А = float(self.ui.lineEdit.text())
        Н = float(self.ui.lineEdit_2.text())
        s = 0.5 * (А * Н)
        self.ui.label_4.setText(f"s = {str(s)}")

    def clear(self):
        self.ui.lineEdit.clear()
        self.ui.lineEdit_2.clear()
        self.ui.label_4.setText(f"s = ")


if __name__ == "__main__":
    import sys 
    app = QtWidgets.QApplication(sys.argv)
    window = MyWindow()
    window.show()
    sys.exit(app.exec_())