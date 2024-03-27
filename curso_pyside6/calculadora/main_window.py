# Aqui irei criar uma classe para simplificar alguns problemas

from PySide6.QtWidgets import (QApplication, QMainWindow, QVBoxLayout, QWidget, QLabel)

class MainWindow(QMainWindow):
    def __init__(self, parent: QWidget | None = None, *args, **kwargs) -> None:
        super().__init__(parent, *args, **kwargs)

        self.cw = QWidget()  # central Widget
        self.v_layout = QVBoxLayout()  # layout vertical
        self.cw.setLayout(self.v_layout)
        self.setCentralWidget(self.cw)

        #Título da janela
        self.setWindowTitle('COLOQUE TÍTULO')



    def adjustFixedSize(self):
        self.adjustSize()
        self.setFixedSize(self.width(), self.height())

    def addWidgetToVLayout(self, widget: QWidget):
        self.v_layout.addWidget(widget)
