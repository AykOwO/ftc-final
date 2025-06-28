from ursina import *
import time 

def mostrar_recompensa(nome_da_pocao: str, nome_do_arquivo_modelo: str):
    app = Ursina(
        title="Poção Criada!",
        borderless=False,
        fullscreen=False,
        exit_button=True
    )

    window.always_on_top = True

    caminho_modelo = f'../modelos/{nome_do_arquivo_modelo}'

    premio = Entity(
        model=caminho_modelo,
        scale=0.8,
        position=(0, 0.5, 0) 
    )

    Text(
        text="Poção Criada com Sucesso!",
        scale=2.5,        
        origin=(0, 0),    
        y=0.4,            
        color=color.green,
        background=True
    )
    Text(
        text=f'Você criou a "{nome_da_pocao}"!',
        scale=2,
        origin=(0, 0),    
        y=0.3,            
        background=True
    )

    AmbientLight(color=color.gray)
    DirectionalLight(color=color.white, direction=(0.7, -0.9, 0.5))
    EditorCamera() # EditorCamera permite usar o mouse para girar/dar zoom

    app.run()
