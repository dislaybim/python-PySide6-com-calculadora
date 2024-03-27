import sys
from PySide6.QtWidgets import (QApplication, QGridLayout, QMainWindow, QPushButton, QWidget)

app = QApplication(sys.argv)
window = QMainWindow()
central_widget = QWidget()
window.setCentralWidget(central_widget)

botao1 = QPushButton('BOTAO 1')
botao1.setStyleSheet('font-size : 40px')

botao2 = QPushButton('BOTAO 2')
botao2.setStyleSheet('font-size : 40px')

botao3 = QPushButton('BOTAO 3')
botao3.setStyleSheet('font-size : 40px')

botao4 = QPushButton('BOTAO 4')
botao4.setStyleSheet('font-size : 40px')

layout = QGridLayout()
central_widget.setLayout(layout)

layout.addWidget(botao1,1,1,1,1)
layout.addWidget(botao2,1,2,1,1)
layout.addWidget(botao3,3,1,1,1)
layout.addWidget(botao4,3,2,1,1)

def style(status_bar):
    status_bar.showMessage('Loucuraaa Demais')

#status Bar
status_bar = window.statusBar()
status_bar.showMessage('Mostrar mensagem na barra')

#menuBar
menu = window.menuBar()
primeiro = menu.addMenu('Primeiro Menu')
acao = primeiro.addAction('Ação')
acao.triggered.connect(style(status_bar))


window.show()    #QMain window alem de ter uma menu bar, tem uma status bar
app.exec()



