#Criar A janela da calculadora, personalisar.
import sys
from PySide6.QtWidgets import QApplication, QGridLayout, QMainWindow, QWidget
from PySide6.QtGui import QPalette, QColor


# Criar uma paleta de cores
palette = QPalette()

# Definir a cor de fundo do widget central como azul claro
background_color = QColor(173, 216, 230)  # R, G, B: valores de 0 a 255
palette.setColor(QPalette.Backgroud, background_color)

# Definir a cor do texto do widget central como preto
text_color = QColor(0, 0, 0)  # R, G, B: valores de 0 a 255
palette.setColor(QPalette.Text, text_color)

# Aplicar a paleta de cores ao widget central
central_widget.setAutoFillBackground(True)
central_widget.setPalette(palette)

layout = QGridLayout()    #define o layout
central_widget.setLayout(layout)


#status Bar
#status_bar = window.statusBar()
#status_bar.showMessage('Mostrar mensagem na barra')


#menuBar
menu = window.menuBar()
primeiro = menu.addMenu('Primeiro Menu')
menu.setFixedSize(400, 100)

if __name__ == '__main__':
app = QApplication(sys.argv)  #definir o aplicativo que será executado
window = QMainWindow()  #definir a nossa janela

central_widget = QWidget()   #cria o setCentral
window.setCentralWidget(central_widget) #adiciona o setcentral a nossa janela
central_widget.setFixedSize(400, 500) #definir o tamanho do meu widget central


window.show()
app.exec()


