from PyQt5 import QtWidgets
import sqlite3
from zad2 import avtoriz,nn,db
conn = sqlite3.connect('avtoriz.db')
cursor = conn.cursor()

cursor.execute('''
CREATE TABLE IF NOT EXISTS users(login CHAR PRIMARY KEY, password TEXT)
''')

conn.commit()

class MyWindow(QtWidgets.QWidget):
    def __init__(self):
        QtWidgets.QWidget.__init__(self)
        self.ui = avtoriz.Ui_Form()
        self.ui.setupUi(self)
        self.ui.pushButton.clicked.connect(self.userx)
        self.ui.pushButton.clicked.connect(self.clear)
        self.vt = VtoroeWindow()
        self.dbs = ThreeWindow()
    def userx(self):
        login = self.ui.lineEdit.text()
        password = self.ui.lineEdit_2.text()
        # cursor.execute('''
        # INSERT OR REPLACE INTO users (login, password) VALUES (?, ?)
        # ''', (login,password))
        # conn.commit()
        cursor.execute('SELECT * FROM users WHERE login=? and password=?', (login,password))
        result = cursor.fetchone()
        # self.dbs.ui.label.setText(f"Добро пожаловать {result[0]}!")

        if not result:
            self.vt.show()
        if result:
            self.dbs.show()
            self.dbs.ui.label.setText(f"Добро пожаловать {result[0]}!")
        
        # else:
        #     # Логин не существует, добавляем его в базу данных
        #     cursor.execute('INSERT INTO users (login, password) VALUES (?, ?)', (login, password))
        #     conn.commit()
            
            
            
    def clear(self):
        self.ui.lineEdit.clear()
        self.ui.lineEdit_2.clear()
class VtoroeWindow(QtWidgets.QWidget):
    def __init__(self):
        QtWidgets.QWidget.__init__(self)
        self.ui = nn.Ui_Form()
        self.ui.setupUi(self)
        self.ui.pushButton.clicked.connect(self.open3)
        
    def open3(self):
        vt.close()
class ThreeWindow(QtWidgets.QWidget):
    def __init__(self):
        QtWidgets.QWidget.__init__(self)
        self.ui = db.Ui_Form()
        self.ui.setupUi(self)
        # self.ui.label.setText("Добро пожаловать {result}!")


   
if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    window = MyWindow()
    vt = VtoroeWindow()
    window.show()
    sys.exit(app.exec_())
