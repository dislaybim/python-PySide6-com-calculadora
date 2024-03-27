# Aqui será criado o modelo de display para a nossa calculadora
from PySide6.QtWidgets import QLineEdit
# criaremos essa classe
class Display(QLineEdit):  #nosso display será criada da bibliteca QLineEdit, que seve para editar linhas
    def __init__(self,*args,**kwargs):
        super().__init__(*args,**kwargs)
