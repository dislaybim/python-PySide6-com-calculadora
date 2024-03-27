#QAPPLICATION E qPUSHBUTTON DE PYSIDE6.QWIDGETS.
#APPLICATION -> O WIDGET PRINCIPAL DA APLICAÇÃO.
#QPUSHBUTTON -> UM BOTÃO.
#PySide6.QtWidgets -> Onde estão os Widgets do Pyside6.
#https://doc.qt.io/qtforpython-6/quickstart.html

import sys

from PySide6.QtWidgets import QApplication, QPushButton  # widgets -> são janelas na tela.

app = QApplication(sys.argv)

botao = QPushButton('Texto do botão')
botao.setStyleSheet('font-size: 80px; color: red')
botao.show()   #adiciona o widget na hierarquia, e executa a janela

botao2 = QPushButton('Botão 2')
botao2.show()
app.exec()



