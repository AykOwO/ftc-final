from src.automatos.info_maquinas.info_afd import INFO_AFD
from src.utils.impressora import Impressora

class AFD:
    def __init__(self, info: INFO_AFD) -> None:
        self.info = info
        self.impressora = Impressora(self.info)

    def computacao(self) -> bool:
        estado_atual = self.info.get_estado_inicial()
        estado_final_definido = self.info.get_estado_final()
        funcao_transicao = self.info.get_funcao_transicao()

        while True:
            simbolo_lido = self.impressora.escolher_ingrediente(estado_atual) 
            
            if simbolo_lido == "exit":
                print("\n✨ Verificando a mistura final...")
                break

            chave = (estado_atual, simbolo_lido)
            if chave in funcao_transicao:
                estado_atual = funcao_transicao[chave]
            else:
                estado_atual = 'erro'
                
        if estado_atual == estado_final_definido:
            nome_da_pocao = self.info.get_nome_da_pocao()
            self.impressora.imprimir_sucesso(f'"{nome_da_pocao}" foi criada perfeitamente!')
            return True 
        else:
            self.impressora.imprimir_erro("A mistura não resultou em uma poção válida ao finalizar.")
            return False 