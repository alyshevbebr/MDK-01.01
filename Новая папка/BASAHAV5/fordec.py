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
            time.sleep(1)
            self.ui.progressBar.setValue(a)
            if a == 20:
                self.ui.label.setStyleSheet("image:url(:/da/audi.jpg)")
            
            if a == 40:
                self.ui.label.setStyleSheet("image:url(:/da/trump-1290494851.jpg)")
            if a == 60:
                self.ui.label.setStyleSheet("image:url(:/da/audi.jpg)")
            if a == 80:
                self.ui.label.setStyleSheet("image:url(:/da/trump-1290494851.jpg)")
            if a == 80:
                self.ui.label.setStyleSheet("image:url(:/da/backiee-308662-landscape.jpg)")
        else:
            zas.close()
            window.show()
        # if a == 20:
        #     self.ui.label.setStyleSheet("image:url(:/da/audi.jpg)")

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    window = MyWindow()
    zas = Zastavka()
    zas.setWindowFlag(QtCore.Qt.SplashScreen)
    zas.show()
    sys.exit(app.exec_())


