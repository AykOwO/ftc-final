class INFO_TURING:
    def __init__(self, conjunto_estados, EI, EF, simbolo_branco, FT, LS, NP):
        """
        Inicializa o objeto de informações para a Máquina de Turing.
        """
        self.conjunto_estados = conjunto_estados
        self.estado_inicial = EI
        self.estados_finais = EF
        self.simbolo_branco = simbolo_branco
        self.funcao_transicao = FT
        self.lista_simbolos = LS
        self.nome_da_pocao = NP


    def get_lista_simbolos(self) -> list:
        return self.lista_simbolos

    def get_conjunto_estados(self) -> list:
        return self.conjunto_estados

    def get_funcao_transicao(self) -> dict:
        return self.funcao_transicao
    
    def get_estado_inicial(self) -> str:
        return self.estado_inicial

    def get_estados_finais(self) -> set:
        return self.estados_finais
    
    def get_simbolo_branco(self) -> str:
        return self.simbolo_branco

    def get_nome_da_pocao(self) -> str:
        return self.nome_da_pocao 


    def print_info(self) -> None:
        """
        Imprime uma visualização formatada de toda a configuração da Máquina de Turing.
        """
        print("\n" + "="*50)
        print("⚙️  CONFIGURAÇÃO DA MÁQUINA DE TURING ⚙️")
        print("="*50)
        print(f"✨ Poção a ser criada: {self.nome_da_pocao}")
        print(f"🔢 Conjunto de estados [{len(self.conjunto_estados)}]: {self.conjunto_estados}")
        print(f"🏁 Estado Inicial: {self.estado_inicial}")
        print(f"🏆 Estados Finais: {self.estados_finais}")
        print(f"⬜ Símbolo Branco (usado para espaços vazios): '{self.simbolo_branco}'")
        print(f"🔡 Alfabeto da Fita (símbolos válidos): {self.lista_simbolos}")
        print("\n📜 Função de Transição (Regras da Receita):")
        print("-"*50)

        for (estado_origem, simbolo_lido), (estado_destino, simbolo_escrito, direcao) in self.funcao_transicao.items():
            movimento = "DIREITA" if direcao == 'R' else "ESQUERDA"
            
            transicao = (
                f"  - Se no estado [{estado_origem}] e lendo '{simbolo_lido}':\n"
                f"    ↳ Vá para o estado [{estado_destino}], escreva '{simbolo_escrito}' e mova para a {movimento}.\n"
            )
            print(transicao)
        
        print("="*50)
        input("\nPressione Enter para iniciar a computação...")

