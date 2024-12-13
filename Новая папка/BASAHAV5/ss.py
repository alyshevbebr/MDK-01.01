

from PyQt5.QtWidgets import QWidget, QApplication, QListWidgetItem, QMessageBox
from PyQt5.uic import loadUi
import sys
import sqlite3
from PyQt5 import QtCore,QtGui


conn = sqlite3.connect('data.db')
cursor = conn.cursor()

cursor.execute('''
CREATE TABLE IF NOT EXISTS tasks(task TEXT , completed TEXT,  date TEXT)
''')
class Window(QWidget):
    def __init__(self):
        super(Window, self).__init__()
        loadUi("jjea.ui", self)
        self.calendarWidget0.selectionChanged.connect(self.calendarDateChanged)
        self.calendarDateChanged()
        self.setWindowTitle("РФ")
        self.setWindowIcon(QtGui.QIcon('ghs.jpg'))
        self.pushButton_2.clicked.connect(self.saveChanges)
        self.pushButton.clicked.connect(self.addNewTask)

    def calendarDateChanged(self):
        print("The calendar date was changed.")
        dateSelected = self.calendarWidget0.selectedDate().toPyDate()
        print("Date selected:", dateSelected)
        self.updateTaskList(dateSelected)

    def updateTaskList(self, date):
        self.listWidget.clear()

        db = sqlite3.connect("data.db")
        cursor = db.cursor()

        query = "SELECT task, completed FROM tasks WHERE date = ?"
        row = (date,)
        results = cursor.execute(query, row).fetchall()
        for result in results:
            item = QListWidgetItem(str(result[0]))
            item.setFlags(item.flags() | QtCore.Qt.ItemIsUserCheckable)
            if result[1] == "YES":
                item.setCheckState(QtCore.Qt.Checked)
            elif result[1] == "NO":
                item.setCheckState(QtCore.Qt.Unchecked)
            self.listWidget.addItem(item)

    def saveChanges(self):
        db = sqlite3.connect("data.db")
        cursor = db.cursor()
        date = self.calendarWidget0.selectedDate().toPyDate()

        for i in range(self.listWidget.count()):
            item = self.listWidget.item(i)
            task = item.text()
            if item.checkState() == QtCore.Qt.Checked:
                query = "UPDATE tasks SET completed = 'YES' WHERE task = ? AND date = ?"
            else:
                query = "UPDATE tasks SET completed = 'NO' WHERE task = ? AND date = ?"
            row = (task, date,)
            cursor.execute(query, row)
        db.commit()

        messageBox = QMessageBox()
        messageBox.setText("Changes saved.")
        messageBox.setStandardButtons(QMessageBox.Ok)
        messageBox.exec()

    def addNewTask(self):
        db = sqlite3.connect("data.db")
        cursor = db.cursor()

        newTask = str(self.lineEdit.text())
        date = self.calendarWidget0.selectedDate().toPyDate()

        query = "INSERT INTO tasks(task, completed, date) VALUES (?, ?, ?)"
        row = (newTask, "NO", date)

        cursor.execute(query, row)
        db.commit()
        self.updateTaskList(date)
        self.lineEdit.clear()
import photo
if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = Window()
    window.show()
    sys.exit(app.exec())