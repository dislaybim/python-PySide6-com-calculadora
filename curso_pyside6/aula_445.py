#TRABALHANDO COM CLASSES E HERANÇAS COM O PYSIDE6.
import sys
from PySide6.QtWidgets import (QApplication, QGridLayout, QMainWindow, QPushButton, QWidget)
from PySide6.QtCore import Slot


class MyWindow(QMainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.central_widget = QWidget()
        self.setCentralWidget(self.central_widget)
        self.setWindowTitle('Minha Janela Bonita.')


        self.botao1 = QPushButton('BOTAO 1')
        self.botao1.setStyleSheet('font-size : 40px')
        self.botao1.clicked.connect(self.outro_slot)
        self.botao2 = QPushButton('BOTAO 2')
        self.botao2.setStyleSheet('font-size : 40px')
        self.botao3 = QPushButton('BOTAO 3')
        self.botao3.setStyleSheet('font-size : 40px')
        self.botao4 = QPushButton('BOTAO 4')
        self.botao4.setStyleSheet('font-size : 40px')



        self.grid_layout = QGridLayout()
        self.central_widget.setLayout(self.grid_layout)

        self.grid_layout.addWidget(self.botao1,1,1,1,1)
        self.grid_layout.addWidget(self.botao2,1,2,1,1)
        self.grid_layout.addWidget(self.botao3,3,1,1,1)
        self.grid_layout.addWidget(self.botao4,3,2,1,1)

        # status Bar
        self.status_bar = self.statusBar()
        self.status_bar.showMessage('Mostrar mensagem na barra')

        # menuBar
        self.menu = self.menuBar()
        self.primeiro = self.menu.addMenu('Primeiro Menu')
        self.acao = self.primeiro.addAction('Ação')

        # signal
        self.segundo_acao = self.primeiro.addAction('Deposi')
        self.segundo_acao.setCheckable(True)  # marca e desmarca uma determinada ação
        self.segundo_acao.toggled.connect(self.outro_slot)  # é uma função que observa se desmarcou, e emite uma resposta.
        self.segundo_acao.hovered.connect(self.outro_slot)  # quando eu passar o mouse em cima dessa ação, vai executar outra função.
        # slot é uma ação que ocorre quando um signal é desmarcado.

        @Slot()
        def outro_slot(self):
            print('Está marcado?')

        #@Slot()
        #def terceiro_slot(self, action):
        #    def inner():
          #     outro_slot(action.isChecked())
          #  return inner



if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MyWindow()
    window.show()    #QMain window alem de ter uma menu bar, tem uma status bar
    app.exec()



