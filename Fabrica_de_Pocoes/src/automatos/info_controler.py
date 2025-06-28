from src.utils.arquivo import Arquivo 

class Info_Controler:

    def inicializar(self, escolha_maquina:int):
            arq = Arquivo()
            caminho_arquivo = arq.escolher_entrada(escolha_maquina)

            if not caminho_arquivo:
                return None

            match escolha_maquina:

                case 1:
                    #afd
                    return arq.parse_afd(caminho_arquivo)
                case 2:
                    #apn
                    return None
                case 3:
                    #Moore
                    return None
                case 4:
                    #Mealy
                    return arq.parse_mealy(caminho_arquivo)
                case 5:
                    #Turing
                    return arq.parse_turing(caminho_arquivo)
                case _:
                    return None
