from utils.menu import Menu
from automatos.info import Info

#Fazer: ler e retornar nome dos arquivos presentes em cada um e printar o nome para o usuario escolher

class Controler:

    def __init__(self):
        self.menu = Menu()
        self.info = Info()

    def inicializar(self):
        escolha = self.menu.show()
        self.info.inicializar(caminho_arquivo)
        pass
