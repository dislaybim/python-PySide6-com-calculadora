#QAPPLICATION E qPUSHBUTTON DE PYSIDE6.QWIDGETS.
#APPLICATION -> O WIDGET PRINCIPAL DA APLICAÇÃO.
#QPUSHBUTTON -> UM BOTÃO.
#PySide6.QtWidgets -> Onde estão os Widgets do Pyside6.
#https://doc.qt.io/qtforpython-6/quickstart.html


#vamos aprender a organizar janelas com varias opções.

import sys

from PySide6.QtWidgets import QApplication, QPushButton, QWidget, QVBoxLayout  # widgets -> são janelas na tela.

app = QApplication(sys.argv)

botao = QPushButton('botão 1')                        #define os botões e expõe o texto exibido nele
botao.setStyleSheet('font-size: 40px; color: red')    #faz uma formatação quanto a cor e tamanho
botao2 = QPushButton('Botão 2')
botao2.setStyleSheet('font-size: 40px; color: red')


central_widget = QWidget()              #define a janela onde vamos colocar esses botões
layout = QVBoxLayout()                  #define o Layoute que vamos trabalhar
central_widget.setLayout(layout)        #central widgets a gente adiciona outros elementos como novos botões

layout.addWidget(botao)                 #adiciona os botões as janelas
layout.addWidget(botao2)                #adicionar o outro botão.


central_widget.show()                   #executa a janela
app.exec()                              #executa o looping

#essa janela é na vertical, para exibir na horizontal, poderiamos exibir por meio da função QHBoxLayout, tambem temos o QGridLayout
#na secção de HTML vamos expandir mais nos aspectos de uma Grid.