import re
import os
from pathlib import Path
from src.automatos.info_maquinas.info_afd import INFO_AFD
from src.automatos.info_maquinas.info_turing import INFO_TURING
from src.automatos.info_maquinas.info_mealy import INFO_MEALY

class Arquivo:

    def read_arquivo(self,caminho_arquivo:str) -> list:

        with open(caminho_arquivo, 'r') as arq:
            linhas = [linha.strip() for linha in arq if linha.strip()]#lista de linhas

        arq.close()
        return linhas

    def mostrar_entradas(self, escolha_maquina: int) -> list:
        pastas = {1: "AFD", 2: "APD", 3: "Moore", 4: "Mealy", 5: "Turing"}
        pasta = pastas.get(escolha_maquina)
        caminho_base = f"arquivos/{pasta}" 

        if not os.path.exists(caminho_base):
            print(f"❌ Diretório não encontrado: {caminho_base}")
            return []

        arquivos = [
            arq for arq in os.listdir(caminho_base)
            if arq.endswith(".txt")
        ]

        if not arquivos:
            print(f"⚠️ Nenhum arquivo .txt encontrado na pasta {caminho_base}")
            return [] 

        print(f"\n📂 Arquivos em {caminho_base}/:\n")
        for i, nome in enumerate(arquivos):
            print(f"[{i}] {nome}")
        return arquivos

    def escolher_entrada(self, escolha_maquina: int) -> str:
        arquivos = self.mostrar_entradas(escolha_maquina)
        if not arquivos:
            return ""

        try:
            escolha = int(input("\nEscolha o arquivo desejado (pelo número): "))
            if 0 <= escolha < len(arquivos):
                pasta = {1: "AFD", 2: "APD", 3: "Moore", 4: "Mealy", 5: "Turing"}[escolha_maquina]
                caminho = os.path.join("arquivos", pasta, arquivos[escolha])
                return caminho
            else:
                print("❌ Escolha inválida.")
                return self.escolher_entrada(escolha_maquina)
        except ValueError:
            print("❌ Entrada inválida.")
            return self.escolher_entrada(escolha_maquina) 

    def _extrair_nome_pocao(self, caminho_arquivo: str) -> str:
        """Função auxiliar para extrair e formatar o nome da poção."""
        nome_base = Path(caminho_arquivo).stem
        return nome_base.replace('_', ' ').title()

#Parsers
    def parse_afd(self, caminho_arquivo: str) -> INFO_AFD:
        """
        Lê e interpreta um arquivo de AFD, coletando todos os dados
        e retornando um objeto INFO_AFD completo e válido de uma só vez.
        """
        linhas = self.read_arquivo(caminho_arquivo)

        nome_pocao = self._extrair_nome_pocao(caminho_arquivo)
        
        conjunto_estados = []
        estado_inicial = ""
        estado_final = ""
        funcao_transicao = {}
        alfabeto = set()

        i = 0
        if linhas[i].startswith("Q:"):
            conjunto_estados = linhas[i][2:].strip().split()
            i += 1
        else:
            raise ValueError("Arquivo AFD com formato inválido")

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
                    alfabeto.add(simbolo)
            i += 1
        
        lista_simbolos = sorted(list(alfabeto))

        return INFO_AFD(conjunto_estados,estado_inicial,estado_final,funcao_transicao,lista_simbolos,nome_pocao)



    def parse_turing(self, caminho_arquivo: str) -> INFO_TURING:
        linhas = [ln for ln in self.read_arquivo(caminho_arquivo) if not ln.startswith('#')]
        nome_pocao = self._extrair_nome_pocao(caminho_arquivo)
        
        conjunto_estados = linhas[0][2:].strip().split()
        estado_inicial = linhas[1][2:].strip()
        estados_finais = set(linhas[2][2:].strip().split())
        simbolo_branco = linhas[3][2:].strip()
        
        funcao_transicao = {}
        alfabeto = set()

        padrao = re.compile(r'(\w+)\s+([a-zA-Z0-9_])\s+->\s+(\w+)\s+([a-zA-Z0-9_])\s+([RL])')

        for linha in linhas[4:]:
            match = padrao.match(linha)
            if match:
                e_origem, s_lido, e_destino, s_escrito, direcao = match.groups()
                chave = (e_origem, s_lido)
                valor = (e_destino, s_escrito, direcao)
                funcao_transicao[chave] = valor
                alfabeto.add(s_lido)
                alfabeto.add(s_escrito)
        
        alfabeto.discard(simbolo_branco)
        lista_simbolos = sorted(list(alfabeto))

        return INFO_TURING(conjunto_estados, estado_inicial, estados_finais, simbolo_branco, funcao_transicao, lista_simbolos, nome_pocao)
    
    
    def parse_mealy(self, caminho_arquivo: str) -> INFO_MEALY:
        """
        Lê e interpreta um arquivo de Máquina de Mealy.
        """
        linhas = [ln for ln in self.read_arquivo(caminho_arquivo) if not ln.startswith('#')]
        nome_pocao = self._extrair_nome_pocao(caminho_arquivo)

        conjunto_estados = linhas[0][2:].strip().split()
        estado_inicial = linhas[1][2:].strip()

        funcao_transicao = {}
        alfabeto_entrada = set()
        alfabeto_saida = set()

        # O padrão captura: estado_origem, simbolo_lido, estado_destino, simbolo_saida
        padrao = re.compile(r'(\w+)\s+([a-zA-Z0-9_])\s+->\s+(\w+)\s+([a-zA-Z0-9_])')

        for linha in linhas[2:]:
            match = padrao.match(linha.strip())
            if match:
                e_origem, s_lido, e_destino, s_saida = match.groups()
                chave = (e_origem, s_lido)
                valor = (e_destino, s_saida)
                funcao_transicao[chave] = valor
                alfabeto_entrada.add(s_lido)
                alfabeto_saida.add(s_saida)

        return INFO_MEALY(
            conjunto_estados,
            estado_inicial,
            funcao_transicao,
            sorted(list(alfabeto_entrada)),
            sorted(list(alfabeto_saida)),
            nome_pocao
        )