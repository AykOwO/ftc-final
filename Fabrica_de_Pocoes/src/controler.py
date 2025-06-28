from src.utils.menu import Menu
from src.automatos.info_controler import Info_Controler
from src.automatos.AFD import AFD
from src.automatos.TURING import Turing
from src.automatos.MEALY import Mealy
from src.utils.cena_pocoes import mostrar_recompensa

class Controler:

    def __init__(self):
        self.menu = Menu()
        self.info_controler = Info_Controler()
        self.mapeamento_modelos = {
            "Pocao Citrica": "pocao_citrica.glb",
            "Pocao Invisibilidade": "pocao_de_invisibilidade.glb",
            "Pocao De Restauracao Comum": "pocao_de_restauracao.glb",
            "Pocao de Duplicacao": "pocao_de_duplicacao.glb"
        }

    def inicializar(self):
        escolha = self.menu.show()
        info = self.info_controler.inicializar(escolha)
        return escolha, info

    def controler_maquina(self):
        escolha, info = self.inicializar()
        
        if not info:
            return

        match int(escolha):
            case 1:
                afd = AFD(info)
                sucesso = afd.computacao()
                
                if sucesso:
                    nome_pocao_criada = info.get_nome_da_pocao()
                    nome_arquivo = self.mapeamento_modelos.get(nome_pocao_criada)
                    
                    if nome_arquivo:
                        mostrar_recompensa(
                            nome_da_pocao=nome_pocao_criada,
                            nome_do_arquivo_modelo=nome_arquivo
                        )
                    else:
                        print(f"ERRO: A poção '{nome_pocao_criada}' foi criada, mas não há um modelo 3D mapeado para ela.")
                
            case 2:
                print("APD")
            case 3:
                print("Moore")
            case 4:
                mealy = Mealy(info)
                mealy.computacao()
            case 5:
                turing = Turing(info)
                sucesso = turing.computacao()

                if sucesso:
                    nome_pocao_criada = info.get_nome_da_pocao()
                    nome_arquivo = self.mapeamento_modelos.get(nome_pocao_criada)
                    
                    if nome_arquivo:
                        mostrar_recompensa(
                            nome_da_pocao=nome_pocao_criada,
                            nome_do_arquivo_modelo=nome_arquivo
                        )
                    else:
                        print(f"ERRO: A poção '{nome_pocao_criada}' foi criada, mas não há um modelo 3D mapeado para ela.")
