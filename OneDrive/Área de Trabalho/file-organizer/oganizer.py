import os
import shutil
import json
from datetime import datetime

MAPA_EXTENSOES = {
    'Imagens': ['.jpg', '.jpeg', '.png', '.gif'],
    'Documentos': ['.pdf', '.docx', '.txt', '.xlsx'],
    'Videos': ['.mp4', '.mkv', '.avi'],
    'Musicas': ['.mp3', '.wav'],
    'Compactados': ['.zip', '.rar', '.7z'],
}

def organizar(diretorio):
    if not os.path.isdir(diretorio):
        print(f"Erro: O caminho '{diretorio}' não é válido.")
        return

    arquivos_movidos = []

    for item in os.listdir(diretorio):
        caminho_completo = os.path.join(diretorio, item)

        if os.path.isdir(caminho_completo) or item == 'organizer.py':
            continue

        extensao = os.path.splitext(item)[1].lower()
        destino = 'Outros' 

        for categoria, extensoes_categoria in MAPA_EXTENSOES.items():
            if extensao in extensoes_categoria:
                destino = categoria
                break

        
        pasta_destino = os.path.join(diretorio, destino)
        os.makedirs(pasta_destino, exist_ok=True) 
        
        shutil.move(caminho_completo, os.path.join(pasta_destino, item))
        arquivos_movidos.append({"arquivo": item, "para": destino})

    return arquivos_movidos

if __name__ == "__main__":
    caminho_alvo = input("Digite o caminho da pasta (ex: C:/Users/Downloads): ")
    resultado = organizar(caminho_alvo)
    
    if resultado:
        with open(os.path.join(caminho_alvo, 'log_organizacao.json'), 'w') as f:
            json.dump(resultado, f, indent=4)
        print(f"Sucesso! {len(resultado)} arquivos organizados.")

            