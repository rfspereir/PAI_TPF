from PIL import Image #Carregar e salvar os arquivos
from os import path #Salvar os arquivos - ajustar o caminho de saida da imagem final

def carregar_imagem_com_pillow(caminho_arquivo):
    """
    Carrega uma imagem, converte em 8 bits em escala de cinza ('L') se necessário e converte em uma Matriz de pixels

    Argumentos:
    caminho_arquivo (str): Caminho para o arquivo da imagem.

    Retorna:
    list of list of int: Matriz de pixels.

    Lança:
    ValueError se a imagem não estiver em modo 'L' (Escala de cinza 8bits).
    """
    imagem = Image.open(caminho_arquivo)

    if imagem.mode != 'L':
        imagem = imagem.convert('L')

    imagem = redimensionar_proporcional(imagem, (640, 480))

    largura, altura = imagem.size

    pixels = list(imagem.getdata())
    matriz = []
    for i in range(altura):
        linha = []
        for j in range(largura):
            linha.append(pixels[i * largura + j])
        matriz.append(linha)

    return matriz

def redimensionar_proporcional(imagem, tamanho_maximo):
    """
    Redimensiona a imagem mantendo a proporção (aspect ratio),
    adaptando-a ao tamanho máximo fornecido.

    Parâmetros:
    - imagem (PIL.Image): imagem original.
    - tamanho_maximo (tuple): (largura_max, altura_max).

    Retorna:
    - imagem_redimensionada (PIL.Image)
    """
    largura_original, altura_original = imagem.size
    largura_max, altura_max = tamanho_maximo

    proporcao_largura = largura_max / largura_original
    proporcao_altura = altura_max / altura_original
    escala = min(proporcao_largura, proporcao_altura)

    nova_largura = int(largura_original * escala)
    nova_altura = int(altura_original * escala)

    return imagem.resize((nova_largura, nova_altura))

def filtro_mediana(matriz):
    """
    Aplica filtro de mediana 3x3 em uma matriz de pixels.

    Parâmetros:
    - matriz: list[list[int]] — imagem em tons de cinza.

    Retorna:
    - nova_matriz: list[list[int]] — imagem suavizada.
    """
    altura = len(matriz)
    largura = len(matriz[0])
    
    nova_matriz = [[0 for _ in range(largura)] for _ in range(altura)]

    for i in range(1, altura - 1):
        for j in range(1, largura - 1):
            vizinhos = [
                matriz[i-1][j-1], matriz[i-1][j], matriz[i-1][j+1],
                matriz[i][j-1],   matriz[i][j],   matriz[i][j+1],
                matriz[i+1][j-1], matriz[i+1][j], matriz[i+1][j+1]
            ]
            vizinhos.sort()
            mediana = vizinhos[4]  # elemento central da lista ordenada (índice 4)
            nova_matriz[i][j] = mediana

    return nova_matriz


def calcular_limiar_otsu(matriz):
    """
    Calcula o limiar ótimo usando o método de Otsu para uma matriz de pixels em tons de cinza.

    Parâmetros:
    - matriz (list[list[int]]): matriz da imagem em escala de cinza (0-255)

    Retorna:
    - limiar (int): valor ótimo de limiar
    """
    # Calcula o histograma
    histograma = [0] * 256
    total = 0
    for linha in matriz:
        for pixel in linha:
            histograma[pixel] += 1
            total += 1

    soma_total = sum(i * histograma[i] for i in range(256))

    soma_background = 0
    peso_background = 0
    var_max = 0
    limiar_otimo = 0

    for t in range(256):
        peso_background += histograma[t]
        if peso_background == 0:
            continue

        peso_foreground = total - peso_background
        if peso_foreground == 0:
            break

        soma_background += t * histograma[t]
        media_background = soma_background / peso_background
        media_foreground = (soma_total - soma_background) / peso_foreground

        variancia_entre_classes = peso_background * peso_foreground * ((media_background - media_foreground) ** 2)

        if variancia_entre_classes > var_max:
            var_max = variancia_entre_classes
            limiar_otimo = t

    return limiar_otimo


#Funcao implementada - responsavel pelo processo de limiarizacao basico. similar ao exercicio 5 da lista 3 - Relacoes entre pixels e Tarefas
def aplicar_limiar_basico(imagem_matriz, limiar):
    """
    Aplica limiarização básica a uma imagem representada como matriz de pixels.
        - Maior do que o limiar: intensidade convertida em 255.
        - Menor ou igual ao limiar: intensidade convertida em 0.

    Argumentos:
    imagem_matriz (list of list of int): A imagem de entrada como uma matriz de pixels.
    limiar (int): O valor de limiar. Utilizado para definir a partir de qual itensidade os pixels serão alterados.

    Retorna:
    list of list of int: A nova imagem binarizada.

    Referencia:
    Exercicio 5 da lista 3 - Relacoes entre pixels e Tarefas
    """
    altura = len(imagem_matriz)

    # Retorna lista vazia caso acontreca de receber uma imagem vazia
    if altura == 0:
        return []
    
    largura = len(imagem_matriz[0])

    # Cria uma nova matriz para a imagem de saída com as mesmas dimensões
    nova_imagem_matriz = []
    for i in range(altura):
        # Adiciona uma nova linha inicializada
        nova_imagem_matriz.append( [0] * largura)

    # Percorre cada pixel da matriz (linha por linha, coluna por coluna)
    for i in range(altura): # i representa a linha
        for j in range(largura): # j representa a coluna
            intensidade_original = imagem_matriz[i][j] # Acessa o valor do pixel original

            # Aplica a condição lógica: se a intensidade for maior que o limiar(altera para 255) ou se não(Altera para 0).
            if intensidade_original > limiar:
                nova_imagem_matriz[i][j] = 255
            else:
                nova_imagem_matriz[i][j] = 0

    return nova_imagem_matriz

def salvar_imagem_pillow(matriz, caminho_saida, limiar):
    """
    Salva uma matriz de pixels (lista de listas) como uma imagem em escala de cinza (8 bits).
    Se o arquivo já existir, adiciona um número no final (ex: _1, _2, etc.) até encontrar um nome disponível.

    Argumentos:
    matriz (list of list of int): Matriz de pixels (valores 0 ou 255).
    caminho_saida (str): Caminho onde a imagem será salva.
    
    Retorna:
    str: O caminho final onde a imagem foi salva.
    """
    altura = len(matriz)
    if altura == 0:
        raise ValueError("A matriz fornecida está vazia.")

    largura = len(matriz[0])

    # Gera o nome utilizando o nome original da imagem + '_binarizada'+limiar+extensao
    base, extensao = path.splitext(caminho_saida)
    caminho_final = f"{base}_binarizada{limiar}{extensao}"

    # Cria e salva a imagem
    imagem = Image.new('L', (largura, altura))
    pixels = []
    for linha in matriz:
        pixels.extend(linha)

    imagem.putdata(pixels)
    imagem.save(caminho_final)
    
    return caminho_final  # Retorna o caminho onde foi salvo