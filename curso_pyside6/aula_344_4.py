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



def outro_slot(checked):
    print('Está marcado?',checked)

def terceiro_slot(action):
    def inner():
        outro_slot(action.isChecked())
    return inner

#status Bar
status_bar = window.statusBar()
status_bar.showMessage('Mostrar mensagem na barra')

#menuBar
menu = window.menuBar()
primeiro = menu.addMenu('Primeiro Menu')
acao = primeiro.addAction('Ação')

#signal
segundo_acao = primeiro.addAction('Deposi')
segundo_acao.setCheckable(True)                 #marca e desmarca uma determinada ação
segundo_acao.toggled.connect(outro_slot)        #é uma função que observa se desmarcou, e emite uma resposta.
segundo_acao.hovered.connect(terceiro_slot(segundo_acao))         #quando eu passar o mouse em cima dessa ação, vai executar outra função.
#slot é uma ação que ocorre quando um signal é desmarcado.

#outro signal bastante importante é o do botão, pois quando a gente aperta o botão tem como analisar a resposta dele.

botao1.clicked.connect(terceiro_slot(segundo_acao))

window.show()    #QMain window alem de ter uma menu bar, tem uma status bar
app.exec()



