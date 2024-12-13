from PyQt5 import QtWidgets,QtCore
import time
from Dec2  import Dec02,xaxad
class MyWindow(QtWidgets.QWidget):
    def __init__(self):
        QtWidgets.QWidget.__init__(self)
        self.ui = xaxad.Ui_Form()
        self.ui.setupUi(self)
        

class Zastavka(QtWidgets.QWidget):
    def __init__(self):
        QtWidgets.QWidget.__init__(self)
        self.ui = Dec02.Ui_Form()
        self.ui.setupUi(self)
        self.ui.pushButton.clicked.connect(self.doAction)
        self.ui.progressBar.setValue(0)
    def doAction(self):
        a = 0 
        while a < 100:
            a += 20
            time.sleep(0.1)
            self.ui.progressBar.setValue(a)
        else:
            zas.close()
            window.show()
    

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    window = MyWindow()
    zas = Zastavka()
    zas.setWindowFlag(QtCore.Qt.SplashScreen)
    zas.show()
    sys.exit(app.exec_())


