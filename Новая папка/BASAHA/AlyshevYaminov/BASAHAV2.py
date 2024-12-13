from PyQt5 import QtWidgets
import  basaha

class MyWindow(QtWidgets.QWidget):
    def __init__(self):
        QtWidgets.QWidget.__init__(self)
        self.ui = basaha.Ui_Form()
        self.ui.setupUi(self)
        self.ui.pushButton.clicked.connect(self.bb)
        self.ui.pushButton_2.clicked.connect(self.close)
        self.ui.pushButton_3.clicked.connect(self.info)
    def bb(self):
        if self.ui.lineEdit.text() == "" :
            QtWidgets.QMessageBox.information(window,"Текс заголовка", "Текс сообщения" , buttons=QtWidgets.QMessageBox.Ok, defaultButton=QtWidgets.QMessageBox.Ok)
        
        if self.ui.lineEdit.text() == "#":
            a  = QtWidgets.QMessageBox.question(window,"Текст заголовка", "ЫЫЫ",   buttons=QtWidgets.QMessageBox.Yes|QtWidgets.QMessageBox.No,  defaultButton=QtWidgets.QMessageBox.Yes)
            #Дописать
            if a == QtWidgets.QMessageBox.No:
                self.ui.lineEdit.clear()
        if self.ui.lineEdit.text() == "666":
            b = QtWidgets.QMessageBox.critical(window,"Текс заголовка", "Программа выполнила недопустимую ошибку и будет закрыта " , buttons=QtWidgets.QMessageBox.Ok, defaultButton=QtWidgets.QMessageBox.Ok)
            if b == QtWidgets.QMessageBox.Ok:
                sys.exit(app.quit)

    def close(self):
        cl = QtWidgets.QMessageBox.question(window,"Выход из программы", "Вы действительно хотите выйти?",   buttons=QtWidgets.QMessageBox.Yes|QtWidgets.QMessageBox.No,  defaultButton=QtWidgets.QMessageBox.Yes)
        if cl == QtWidgets.QMessageBox.Yes:
            sys.exit(app.quit)
    def info(self):
        information = QtWidgets.QMessageBox.question(window,"Сведение о программе", "Чекра",   buttons=QtWidgets.QMessageBox.Ok,  defaultButton=QtWidgets.QMessageBox.Ok)


        

            


    


    

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    window = MyWindow()
    window.show()
    sys.exit(app.exec_())