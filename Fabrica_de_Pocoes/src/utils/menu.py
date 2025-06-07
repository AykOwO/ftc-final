class Menu:

    @staticmethod
    def show():
        print(titulo) 
        return Menu.escolher_maquina()

    @staticmethod
    def escolher_maquina():
        print(opcoes_maquinas)
        try:

            escolha = int(input("\n> "))
            if escolha <= 5 and escolha > 0:
                return escolha
            else:
                print(erro)
                return Menu.escolher_maquina()

        except ValueError:
            print(erro)
            return Menu.escolher_maquina()

opcoes_maquinas = r"""
╔════════════════════════════════════════════════════╗
║           ESCOLHA O TIPO DE MÁQUINA                ║
╚════════════════════════════════════════════════════╝

╭────────────────────────────────────╮
│            PRINCIPAIS              │
├────────────────────────────────────┤
│ [1] - AFD (Autômato Finito         │
│         Determinístico)            │
│ [2] - APD (Autômato com Pilha)     │
╰────────────────────────────────────╯

╭────────────────────────────────────╮
│              EXTRAS                │
├────────────────────────────────────┤
│ [3] - Máquina de Moore             │
│ [4] - Máquina de Mealy             │
│ [5] - Máquina de Turing            │
╰────────────────────────────────────╯
"""

erro = r"""
╔════════════════════════════════════════════════════╗
║        ESCOLHA INVALIDA, TENTE NOVAMENTE !!!       ║
╚════════════════════════════════════════════════════╝
"""

titulo = r"""
 __                      __             
|__ |_  _. _ _    _| _  |__)_  _ _  _ _ 
|(_||_)| |(_(_|  (_|(-  |  (_)(_(_)(-_)
"""

