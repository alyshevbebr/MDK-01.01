from PyQt5 import QtWidgets
import ComboBox

capitals = {}
capitals[0] = 'Москва'
capitals[1] = 'Киев'
capitals[2] = 'Вашингтон'
capitals[3] = 'Стамбул'
capitals[4] = 'Пекин'
capitals[5] = 'Токио'



class MyWindow(QtWidgets.QWidget):
    def __init__(self):
        QtWidgets.QWidget.__init__(self)
        self.ui = ComboBox.Ui_Form()
        self.ui.setupUi(self)
        self.ui.comboBox.currentIndexChanged.connect(self.box)
        self.ui.comboBox_2.currentIndexChanged.connect(self.box2)
    def box(self):
        self.ui.label.setText("Число = "  + str(self.ui.comboBox.currentText()))
    def box2(self):
        try:
            self.ui.label_2.setText(str(capitals[self.ui.comboBox_2.currentIndex()]))
        except KeyError:
            self.ui.label_2.setText("Index doesn't exist")
    def converter(self):
        c = 0 
        
                  c = a 


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    window = MyWindow()
    window.show()
    sys.exit(app.exec_())
