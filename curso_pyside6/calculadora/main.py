import sys
from PySide6.QtGui import QIcon
from PySide6.QtWidgets import QApplication, QWidget, QVBoxLayout, QLabel
from main_window import MainWindow
from variavel import WINDOW_ICON_PATH
from display import Display

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MainWindow()

    texto1 = QLabel('O meu texto')  # Cria um QLabel para exibir texto
    texto1.setStyleSheet('font-size: 80px; color: red')
    window.addWidgetToVLayout(texto1)  # Adiciona o QLabel ao layout vertical

    window.setWindowTitle('DISLAYBSON CALCULATION')
    window.adjustFixedSize()
    window.show()

    # Define o ícone
    icon = QIcon(str(WINDOW_ICON_PATH))
    window.setWindowIcon(icon)
    app.setWindowIcon(icon)

    # Cria o display e o adiciona ao layout vertical
    display = Display()
    window.addWidgetToVLayout(display)

    app.exec()
