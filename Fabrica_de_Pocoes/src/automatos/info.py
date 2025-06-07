from src.utils.arquivo import Arquivo 

class Info:
    def __init__(self) -> None:
        self.conjunto_estados = []
        self.estado_inicial:str  
        self.estado_final:str
        self.funcao_transicao = {}

    def inicializar(self,caminho_arquivo:str) -> None:
        self.conjunto_estados, self.estado_inicial, self.estado_final, self.funcao_transicao = Arquivo().get_data(caminho_arquivo)
    
    def print_info(self) -> None:
        print(f"Conjunto de estados[{len(self.conjunto_estados)}]: {self.conjunto_estados}")
        print(f"Estado Inicial: {self.estado_inicial}")
        print(f"Estado Final: {self.estado_final}")
        print("Função de transicao: \n")
        for (estado_origem, simbolo_lido), estado_destino in self.funcao_transicao.items():

            transicao =f""" Do estado [{estado_origem}]\n Le o simbolo [{simbolo_lido}]\n Vai para o estado [{estado_destino}]\n"""
            print(f"{transicao}")

               
