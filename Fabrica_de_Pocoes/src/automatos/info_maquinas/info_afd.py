class INFO_AFD:
    def __init__(self,conjunto_estados,EI,EF,FT,LS,NP):
        self.conjunto_estados = conjunto_estados  
        self.estado_inicial = EI 
        self.estado_final = EF
        self.funcao_transicao = FT 
        self.lista_simbolos = LS 
        self.nome_da_pocao = NP

    def get_lista_simbolos(self)->list:
        return self.lista_simbolos

    def get_conjunto_estados(self)->list:
        return self.conjunto_estados

    def get_funcao_transicao(self)->dict:
        return self.funcao_transicao
    
    def get_estado_inicial(self)->str:
        return self.estado_inicial

    def get_estado_final(self)->str:
        return self.estado_final

    def get_nome_da_pocao(self)->str:
        return self.nome_da_pocao 

    def print_info(self) -> None:
        print(f"Conjunto de estados[{len(self.conjunto_estados)}]: {self.conjunto_estados}")
        print(f"Estado Inicial: {self.estado_inicial}")
        print(f"Estado Final: {self.estado_final}")
        print(f"Lista de simbolos: {self.lista_simbolos}")
        print("Função de transicao: \n")
        for (estado_origem, simbolo_lido), estado_destino in self.funcao_transicao.items():

            transicao =f""" Do estado [{estado_origem}]\n Le o simbolo [{simbolo_lido}]\n Vai para o estado [{estado_destino}]\n"""
            print(f"{transicao}")

