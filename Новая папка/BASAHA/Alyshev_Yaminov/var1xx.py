from PyQt5 import QtWidgets
import var1 

class MyWindow(QtWidgets.QWidget):
    def __init__(self):
        QtWidgets.QWidget.__init__(self)
        self.ui = var1.Ui_Form()
        self.ui.setupUi(self)
        self.ui.pushButton_2.clicked.connect(self.P)
        self.ui.pushButton.clicked.connect(self.clear)

    def P(self):
        a = float(self.ui.lineEdit_2.text())
        b = float(self.ui.lineEdit.text())
        c = 2*(a+b)
        self.ui.label_4.setText(f"P = {str(c)}")

    def clear(self):
        self.ui.lineEdit.clear()
        self.ui.lineEdit_2.clear()
        self.ui.label_4.setText(f"P = ")


if __name__ == "__main__":
    import sys 
    app = QtWidgets.QApplication(sys.argv)
    window = MyWindow()
    window.show()
    sys.exit(app.exec_())