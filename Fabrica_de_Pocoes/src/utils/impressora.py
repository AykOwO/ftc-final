import os

class Impressora:

    def __init__(self, info):
        self.info = info

    def limpar_tela(self):
        """Limpa a tela do terminal."""
        os.system('cls' if os.name == 'nt' else 'clear')

    def imprimir_cabecalho(self, texto: str, largura: int = 50):
        """Imprime um cabeçalho estilizado em uma caixa."""
        print("╔" + "═" * largura + "╗")
        print(f"║{texto.center(largura)}║")
        print("╚" + "═" * largura + "╝")

    def imprimir_sucesso(self, texto: str):
        """Imprime uma mensagem de sucesso com um símbolo."""
        print(f"\n✅ SUCESSO: {texto}\n")

    def imprimir_erro(self, texto: str):
        """Imprime uma mensagem de erro com um símbolo."""
        print(f"\n❌ FALHA: {texto}\n")

    def imprimir_info(self, rotulo: str, valor: str):
        """Imprime uma informação formatada."""
        print(f"   🧪 {rotulo}: [{valor}]")

    def escolher_ingrediente(self, estado_atual: str) -> str:
        """Orquestra a impressão da tela de escolha e captura a entrada."""
        self.limpar_tela()

        nome_pocao = self.info.get_nome_da_pocao()
        self.imprimir_cabecalho(f"Preparando: {nome_pocao}")
        
        print("\nINFORMAÇÕES DA MISTURA:")
        self.imprimir_info("Estado Atual", estado_atual)
        
        print("\nINGREDIENTES DISPONÍVEIS:")
        lista_simbolos = sorted(list(self.info.get_lista_simbolos()))
        for simbolo in lista_simbolos:
            print(f"   ➤ {simbolo}")
        
        print("\n" + ("-" * 52))
        print("Digite o símbolo do ingrediente ou 'exit' para finalizar.")
        
        try:
            escolha = input("> ").strip()
            if escolha in lista_simbolos or escolha == "exit":
                return escolha
            else:
                print("\nOpção inválida! Pressione Enter para tentar novamente.")
                input()
                return self.escolher_ingrediente(estado_atual)
        except Exception:
            print("\nOcorreu um erro! Pressione Enter para tentar novamente.")
            input()
            return self.escolher_ingrediente(estado_atual)
