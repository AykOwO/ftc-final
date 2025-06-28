class Menu:

    @staticmethod
    def show():
        print(titulo) 
        return Menu.escolher_maquina()

    @staticmethod
    def escolher_maquina():
        print(opcoes_maquinas)
        try:

            escolha = int(input("> "))
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
______    _          _                 _       ______                         
|  ___|  | |        (_)               | |      | ___ \                        
| |_ __ _| |__  _ __ _  ___ __ _    __| | ___  | |_/ /__   ___ ___   ___  ___ 
|  _/ _` | '_ \| '__| |/ __/ _` |  / _` |/ _ \ |  __/ _ \ / __/ _ \ / _ \/ __|
| || (_| | |_) | |  | | (_| (_| | | (_| |  __/ | | | (_) | (_| (_) |  __/\__ \
\_| \__,_|_.__/|_|  |_|\___\__,_|  \__,_|\___| \_|  \___/ \___\___/ \___||___/
"""

