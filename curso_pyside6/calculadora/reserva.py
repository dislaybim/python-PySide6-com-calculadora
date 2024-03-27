import sys
from PySide6.QtGui import QIcon   #precisa do caminho de um arquivo que ele utiliza como icone
from PySide6.QtWidgets import (QApplication, QVBoxLayout, QWidget, QLabel, QLineEdit,QTextEdit)#, QLineEdit,QTextEdit)
from main_window import MainWindow
from variavel import WINDOW_ICON_PATH
from display import Display

if __name__ == '__main__':
    # snake_case
    # pascal_case
    #camelcase

    app = QApplication(sys.argv)
    window = MainWindow()

    texto1 = QLabel('O meu texto')  # criei um texto com a função QLabel
    texto1.setStyleSheet('font-size: 80px; color: red')
    window.addWidgetToVLayout(texto1)  # Adicionei ao meu Layout
    window.setWindowTitle('DISLAYBSON CALCULATION')
    window.adjustFixedSize()
    window.show()

    # define o ícone
    icon = QIcon(str(WINDOW_ICON_PATH))
    window.setWindowIcon(icon)
    app.setWindowIcon(icon)

    # criar display:
    display = Display()
    window.addToVLayout(display)

    #executa tudo


    app.exec()

