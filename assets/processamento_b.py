from PIL import Image #Carregar e salvar os arquivos
from os import path #Salvar os arquivos - ajustar o caminho de saida da imagem final
from processamento import redimensionar_proporcional

#TODO: CRIAR UMA FUNÇÃO PARA FAZER O PROCESSO COMPLETO, ABRIR, APLICAR CANNY E SALVAR PARA TESTAR O FUNCIONAMENTO DO CANNY.

def processamento_all_in_one(caminho_arquivo):

    imagem = Image.open(caminho_arquivo)

    if imagem.mode != 'L':
        imagem = imagem.convert('L')

    imagem = redimensionar_proporcional(imagem, (640, 480))

    # Gera o nome utilizando o nome original da imagem + '_binarizada'+limiar+extensao
    base, extensao = path.splitext(caminho_arquivo)
    caminho_final = f"{base}_canny{extensao}"
    imagem.save(caminho_final)
    
    return caminho_final  # Retorna o caminho onde foi salvo