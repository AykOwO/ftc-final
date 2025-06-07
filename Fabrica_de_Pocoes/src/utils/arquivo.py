import re

class Arquivo:

    def read_arquivo(self,caminho_arquivo:str) -> list:

        with open(caminho_arquivo, 'r') as arq:
            linhas = [linha.strip() for linha in arq if linha.strip()]#lista de linhas

        arq.close()
        return linhas

    def get_data(self,caminho_arquivo:str):

        linhas = self.read_arquivo(caminho_arquivo)
        conjunto_estados = []
        estado_inicial = ""  
        estado_final = ""
        funcao_transicao = {}

        i = 0
        if linhas[i].startswith("Q:"): #Se a primeira linha começa com Q
            conjunto_estados = linhas[i][2:].strip().split()
            i += 1 #Avança para a proxima linha
        else:
            raise ValueError("Arquivo com formato invalideo")

        estado_inicial = linhas[i][2:].strip()
        i += 1

        estado_final = linhas[i][2:].strip()
        i += 1

        while i < len(linhas) and linhas[i] != "---":

            linha_atual = linhas[i]
            partes = re.findall(r'(\w+)\s+->\s+(\w+)\s+\|\s+([a-zA-Z0-9 ]+)', linha_atual)

            for estado_origem, estado_destino, chars_entrada in partes:
                simbolos = chars_entrada.strip().split()
                for simbolo in simbolos:
                    chave = (estado_origem, simbolo)
                    funcao_transicao[chave] = estado_destino
            i += 1

        return conjunto_estados, estado_inicial, estado_final, funcao_transicao

    def mostrar_entradas(self,escolha_maquina:int) -> None:
        if(escolha_maquina == 1):
            pass
        if(escolha_maquina == 2):
            pass
        if(escolha_maquina == 3):
            pass
        if(escolha_maquina == 4):
            pass
        if(escolha_maquina == 5):
            pass

    #
    def escolher_entrada(self,escolha_maquina:int) -> str:
        self.mostrar_entradas(escolha_maquina)
        
        pass
