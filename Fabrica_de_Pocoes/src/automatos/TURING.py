from src.automatos.info_maquinas.info_turing import INFO_TURING
import time
import os

class Turing:
    def __init__(self, info: INFO_TURING) -> None:
        self.info = info
        self.fita = {}
        self.posicao_cabecote = 0
        self.estado_atual = self.info.get_estado_inicial()

    def _limpar_tela(self):
        os.system('cls' if os.name == 'nt' else 'clear')

    def _imprimir_fita(self):
        self._limpar_tela()
        print("="*60)
        print(f"🧪 Preparando: {self.info.get_nome_da_pocao()}")
        print(f"⚙️  Estado Atual: [{self.estado_atual}]")
        print("="*60)
        
        min_idx = min(self.fita.keys()) if self.fita else 0
        max_idx = max(self.fita.keys()) if self.fita else 0
        
        range_min = min(min_idx, self.posicao_cabecote) - 5
        range_max = max(max_idx, self.posicao_cabecote) + 5
        
        fita_str = ""
        cabecote_str = ""
        indices_str = ""
        
        for i in range(range_min, range_max + 1):
            simbolo = self.fita.get(i, self.info.get_simbolo_branco())
            fita_str += f"| {simbolo} "
            indices_str += f" {str(i):^3}"
            
            if i == self.posicao_cabecote:
                cabecote_str += "  ^  "
            else:
                cabecote_str += "    "
        
        fita_str += "|"
        print("Fita:")
        print(fita_str)
        print(cabecote_str)
        print(indices_str)
        print("\n")


    def computacao(self) -> bool:
        palavra = input("\n🧪 Digite a sequência inicial de ingredientes na fita: ")
        
        for i, simbolo in enumerate(palavra):
            self.fita[i] = simbolo

        print("\n✨ Iniciando a computação da Máquina de Turing...")
        time.sleep(1)

        max_passos = 1000
        passos = 0

        while self.estado_atual not in self.info.get_estados_finais() and passos < max_passos:
            self._imprimir_fita()

            simbolo_atual = self.fita.get(self.posicao_cabecote, self.info.get_simbolo_branco())
            chave_transicao = (self.estado_atual, simbolo_atual)

            if chave_transicao not in self.info.get_funcao_transicao():
                print(f"❌ Transição não definida para o estado [{self.estado_atual}] com o símbolo '{simbolo_atual}'. Computação falhou.")
                return False

            novo_estado, novo_simbolo, direcao = self.info.get_funcao_transicao()[chave_transicao]
            
            print(f"Lendo '{simbolo_atual}', Escrevendo '{novo_simbolo}', Movendo '{direcao}'")

            self.fita[self.posicao_cabecote] = novo_simbolo
            self.estado_atual = novo_estado
            
            if direcao == 'R': self.posicao_cabecote += 1
            elif direcao == 'L': self.posicao_cabecote -= 1
            
            passos += 1
            time.sleep(0.3)

        self._imprimir_fita()

        if self.estado_atual in self.info.get_estados_finais():
            print(f"\n✅ SUCESSO: A máquina parou no estado final [{self.estado_atual}].")
            return True
        else:
            print(f"\n❌ FALHA: A máquina parou no estado [{self.estado_atual}] (não final) ou excedeu o número de passos.")
            return False
