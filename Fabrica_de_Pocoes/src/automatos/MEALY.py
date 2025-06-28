from src.automatos.info_maquinas.info_mealy import INFO_MEALY
from src.utils.impressora import Impressora
import time

class Mealy:
    def __init__(self, info: INFO_MEALY) -> None:
        self.info = info

    def _limpar_tela(self):
        import os
        os.system('cls' if os.name == 'nt' else 'clear')

    def computacao(self) -> bool:
        self.info.print_info()
        palavra_entrada = input("\n🧪 Digite a sequência de ingredientes: ")
        
        estado_atual = self.info.get_estado_inicial()
        funcao_transicao = self.info.get_funcao_transicao()
        palavra_saida = ""

        print("\n✨ Iniciando a computação da Máquina de Mealy...")
        time.sleep(1)

        for i, simbolo_lido in enumerate(palavra_entrada):
            self._limpar_tela()
            print("="*60)
            print(f"📜 Processando a receita: {self.info.get_nome_da_pocao()}")
            print(f"Passo {i+1}/{len(palavra_entrada)}")
            print(f"Estado Atual: [{estado_atual}]")
            print(f"Ingrediente Lido: '{simbolo_lido}'")
            
            chave = (estado_atual, simbolo_lido)
            
            if chave not in funcao_transicao:
                print(f"\n❌ FALHA: A mistura desandou! Transição não definida para o estado [{estado_atual}] com o ingrediente '{simbolo_lido}'.")
                return False

            estado_destino, simbolo_saida = funcao_transicao[chave]
            
            print(f"Resultado da Transição: Vai para o estado [{estado_destino}]")
            print(f"Efeito Mágico (Saída): '{simbolo_saida}'")
            print("="*60)
            
            palavra_saida += simbolo_saida
            estado_atual = estado_destino
            
            print(f"\nPalavra de saída até o momento: {palavra_saida}")
            time.sleep(1.5)

        self._limpar_tela()
        print("\n" + "="*50)
        print(f"✅ SUCESSO: A '{self.info.get_nome_da_pocao()}' foi criada!")
        print(f"Sequência de Ingredientes (Entrada): {palavra_entrada}")
        print(f"Resultado Mágico (Saída): {palavra_saida}")
        print("="*50)

        return True