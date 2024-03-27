# QMainWindow e centralWidget
# -> QApplication (App)
#   ->QMainWindow (window -> setCentralWidget)
#      -> CentralWidget (central_widget)
#          -> Layout (layout)
#              -> Widget 1 (botão1)
#              -> Widget 2 (botão2)
#              -> Widget 3 (botão3)
#   ->show
# ->exec
# dava para a gente criar uma barra de status.
# essa é a indentação do nosso programa anterior.

import sys
from PySide6.QtWidgets import (QApplication, QGridLayout, QMainWindow, QPushButton, QWidget)

app = QApplication(sys.argv)
window = QMainWindow()
central_widget = QWidget()
window.setCentralWidget(central_widget)

# criação e formatação dos botões
botao1 = QPushButton('Botão 1')
botao1.setStyleSheet('font-size: 40px; cor: green')
botao2 = QPushButton('Botão 2')
botao2.setStyleSheet('font-size: 40px; cor: green')
botao3 = QPushButton('Botão 3')
botao3.setStyleSheet('font-size: 40px; cor: green')

# definir a configuração do Layout
layout = QGridLayout()
# centralizar o layout na janela
central_widget.setLayout(layout)

layout.addWidget(botao1, 1, 1, 1, 1)
layout.addWidget(botao2, 1, 2, 1, 1)
layout.addWidget(botao3, 3, 1, 1, 2)


# statusBar

def slot_example():
    status_bar.showMessage('Dislaybson Clicou')


status_bar = window.statusBar()
status_bar.showMessage('Universidade Federal do Piauí - UFPI  |    SIGAA - UFRN')
# status_bar.setStyleSheet('font-size: 12px; color : blue')


# dentro de cada ação dessa se eu clicar alguma coisa é para executar alguma ação.
# menuBar
menu = window.menuBar()
primeiro_menu = menu.addMenu('Ensino')
menu.setStyleSheet('font-size: 30px; color : red')
primeira_acao = primeiro_menu.addAction('Avaliação Docente')
primeira_acao.triggered.connect(slot_example(status_bar))

segunda_acao = primeiro_menu.addAction('Minhas Notas')
terceira_acao = primeiro_menu.addAction('Atestado de Matrícula')
quarta_acao = primeiro_menu.addAction('Consultar Histórico')
quinta_acao = primeiro_menu.addAction('Projeto de Ensino')

segundo_menu = menu.addMenu('Pesquisa')
menu.setStyleSheet('font-size: 30px; color : red')
primeira_acao = segundo_menu.addAction('Plano de Trabalho')
segunda_acao = segundo_menu.addAction('Relatório de iniciação ciêntífica')
terceira_acao = segundo_menu.addAction('Congresso de Iniciação Científica')

terceiro_menu = menu.addMenu('Extensão')
menu.setStyleSheet('font-size: 30px; color : red')
primeira_acao = terceiro_menu.addAction('Ações de Extensão')
segunda_acao = terceiro_menu.addAction('Minha ações como menbro da equipe')
terceira_acao = terceiro_menu.addAction('Certificado')
quarta_acao = terceiro_menu.addAction('Visualizar Resultados')
quinta_acao = terceiro_menu.addAction('Curricularização da Extensão')

quarto_menu = menu.addMenu('Monitoria')
menu.setStyleSheet('font-size: 30px; color : red')
primeira_acao = quarto_menu.addAction('Meus Projetos de monitoria')
segunda_acao = quarto_menu.addAction('Meus certificados')
terceira_acao = quarto_menu.addAction('Meus Relatórios')
quarta_acao = quarto_menu.addAction('Atividades do mês')
quinta_acao = quarto_menu.addAction('Inscreva-se na seleção')

quinto_menu = menu.addMenu('Biblioteca')
menu.setStyleSheet('font-size: 30px; color : red')
primeira_acao = quinto_menu.addAction('Pesquisa do Material do Acervo')
segunda_acao = quinto_menu.addAction('Pesquisa de Artigos do Acervo')
terceira_acao = quinto_menu.addAction('Emprestimos')
quarta_acao = quinto_menu.addAction('Reservas de Materiais')
quinta_acao = quinto_menu.addAction('Serviços ao Usuário')

# plotar as janelas
window.show()
app.exec()
