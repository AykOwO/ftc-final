class INFO_MEALY:
    def __init__(self, conjunto_estados, estado_inicial, funcao_transicao, lista_simbolos_entrada, lista_simbolos_saida, nome_da_pocao):
        """
        Inicializa o objeto de informações para a Máquina de Mealy.
        """
        self.conjunto_estados = conjunto_estados
        self.estado_inicial = estado_inicial
        self.funcao_transicao = funcao_transicao
        self.lista_simbolos_entrada = lista_simbolos_entrada
        self.lista_simbolos_saida = lista_simbolos_saida
        self.nome_da_pocao = nome_da_pocao

    def get_lista_simbolos(self) -> list:
        return self.lista_simbolos_entrada

    def get_conjunto_estados(self) -> list:
        return self.conjunto_estados

    def get_funcao_transicao(self) -> dict:
        return self.funcao_transicao
    
    def get_estado_inicial(self) -> str:
        return self.estado_inicial

    def get_nome_da_pocao(self) -> str:
        return self.nome_da_pocao

    def print_info(self) -> None:
        """
        Imprime uma visualização formatada da configuração da Máquina de Mealy.
        """
        print("\n" + "="*50)
        print("⚙️  CONFIGURAÇÃO DA MÁQUINA DE MEALY ⚙️")
        print("="*50)
        print(f"✨ Poção a ser criada: {self.nome_da_pocao}")
        print(f"🔢 Conjunto de estados [{len(self.conjunto_estados)}]: {self.conjunto_estados}")
        print(f"🏁 Estado Inicial: {self.estado_inicial}")
        print(f"🔡 Alfabeto de Entrada: {self.lista_simbolos_entrada}")
        print(f"ട്ടു Alfabeto de Saída: {self.lista_simbolos_saida}")
        print("\n📜 Função de Transição (Estado Atual, Símbolo Lido -> Novo Estado, Símbolo Escrito):")
        print("-"*50)

        for (estado_origem, simbolo_lido), (estado_destino, simbolo_saida) in self.funcao_transicao.items():
            transicao = (
                f"  - Se no estado [{estado_origem}] e lendo '{simbolo_lido}':\n"
                f"    ↳ Vá para o estado [{estado_destino}] e escreva '{simbolo_saida}'.\n"
            )
            print(transicao)
        
        print("="*50)
        input("\nPressione Enter para iniciar a computação...")
