import sys
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QLabel, QPushButton, QLineEdit
from PyQt5.QtGui import QFont, QColor, QPalette
from PyQt5.QtCore import Qt

class MaterialDesignApp(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()
        
    def initUI(self):
        # Настройка основного окна
        self.setWindowTitle('Material Design Interface')
        self.setGeometry(100, 100, 800, 600)

        # Создание макета
        layout = QVBoxLayout()

        # Создание ярлыка заголовка
        title = QLabel('Привет, это интерфейс Material Design!')
        title.setFont(QFont('Helvetica', 16))
        title.setStyleSheet('color: #0d6efd')
        
        # Создание ярлыка подзаголовка
        subtitle = QLabel('Выберите параметры и нажмите кнопку')
        subtitle.setFont(QFont('Helvetica', 12))
        subtitle.setStyleSheet('color: #0d6efd')

        # Создание текстового поля
        text_input = QLineEdit()
        text_input.setPlaceholderText('Введите текст здесь...')
        text_input.setStyleSheet("""
            QLineEdit {
                border: 1px solid #d0e3ff;
                padding: 10px;
                border-radius: 4px;
            }
            QLineEdit:focus {
                border-color: #0d6efd;
                box-shadow: 0 0 5px rgba(13, 110, 253, 0.5);
            }
        """)
        
        # Создание кнопки
        button = QPushButton('Отправить')
        button.setStyleSheet("""
            QPushButton {
                background-color: #0d6efd;
                color: white;
                border: none;
                padding: 10px 20px;
                border-radius: 4px;
            }
            QPushButton:hover {
                background-color: #0b5ed7;
            }
        """)
        
        # Добавление виджетов в макет
        layout.addWidget(title)
        layout.addWidget(subtitle)
        layout.addWidget(text_input)
        layout.addWidget(button)

        # Установка макета в главное окно
        self.setLayout(layout)

        # Настройка палитры для фона
        self.setAutoFillBackground(True)
        palette = self.palette()
        palette.setColor(QPalette.Window, QColor('#ffffff'))
        self.setPalette(palette)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MaterialDesignApp()
    ex.show()
    sys.exit(app.exec_())
