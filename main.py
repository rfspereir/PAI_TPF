"""
ENGENHARIA DE COMPUTAÇÃO - PUCMINAS - 2025  
PROCESSAMENTO E ANÁLISE DE IMAGENS  
Professora: Ana Carolina Conceição de Jesus  
Aluno: Rafael Felipe Silva Pereira

Este trabalho implementa um classificador de fissuras em imagens RGB de estruturas de concreto, utilizando técnicas de pré-processamento, limiarização automática e análise binária.

**IMPORTANTE** >> A entrada esperada é uma imagem RGB de estruturas de concreto.

Fluxo geral do processamento:
1. A imagem é carregada e convertida para escala de cinza 8 bits.
2. É redimensionada proporcionalmente para padronizar a entrada.
3. Um filtro de mediana 3x3 é aplicado para remoção de ruídos sem comprometer as fissuras.
4. O limiar de binarização é calculado automaticamente com o método de Otsu.
5. Aplica-se a limiarização, gerando uma imagem binária (0 para fundo, 255 para possível fissura).
6. A imagem binarizada é salva no disco, no mesmo caminho da imagem original.
7. Um critério heurístico (com base na proporção de pixels brancos) é usado para classificar a imagem:
    - Se mais de 1% dos pixels forem brancos, considera-se que há fissura.
    - Caso contrário, considera-se que não há fissura.

A interface gráfica, desenvolvida com Qt (PySide6), permite:
- Selecionar uma imagem RGB.
- Visualizar a imagem original e a imagem com o resultado da detecção lado a lado.
- Exibir dinamicamente o resultado do classificador (“Fissura detectada” ou “Sem fissura detectada”).

O projeto foi desenvolvido com o mínimo uso de bibliotecas externas, priorizando a implementação direta dos algoritmos sempre que possível.
"""

import sys
import os
sys.path.append(os.path.join(os.path.dirname(__file__), 'assets'))
from PySide6.QtWidgets import QApplication, QMainWindow, QFileDialog #Interface grafica
from PySide6.QtGui import QPixmap #Interface grafica
from PySide6.QtCore import Qt, Signal, QThread #Interface grafica
from interface import Ui_MainWindow #arquivo com a Interface grafica gerado a partir do interface.ui
from PIL import Image #Carregar e salvar os arquivos
from processamento import (
    carregar_imagem_com_pillow,
    filtro_mediana,
    calcular_limiar_otsu,
    aplicar_limiar_basico,
    salvar_imagem_pillow
) # arquivo com as funções de processamento criadas

#Funcionamento da GUI do programa:
class Worker(QThread):
    finished = Signal(str, bool)  # Caminho da imagem + resultado

    def __init__(self, caminho_imagem):
        super().__init__()
        self.caminho_imagem = caminho_imagem

    def run(self):
        # Pipeline completo
        matriz = carregar_imagem_com_pillow(self.caminho_imagem)
        matriz_filtrada = filtro_mediana(matriz)
        limiar = calcular_limiar_otsu(matriz_filtrada)
        matriz_binaria = aplicar_limiar_basico(matriz_filtrada, limiar)
        caminho_saida = salvar_imagem_pillow(matriz_binaria, self.caminho_imagem, limiar)

        # Classificação simples por proporção de pixels brancos
        total_pixels = sum(len(linha) for linha in matriz_binaria)
        brancos = sum(pixel == 255 for linha in matriz_binaria for pixel in linha)
        proporcao = brancos / total_pixels
        com_fissura = proporcao > 0.01  # Exemplo: 1% de pixels brancos

        self.finished.emit(caminho_saida, com_fissura)


class JanelaPrincipal(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.caminho_imagem_original = ""

        self.ui.btnCarregarImagem.clicked.connect(self.abrir_imagem)
        self.ui.btnProcessar.clicked.connect(self.processar_imagem)

    def selecionar_arquivo(self):
        caminho, _ = QFileDialog.getOpenFileName(self, "Abrir Imagem", "", "Imagens (*.png *.jpg *.bmp *.tiff *.jpeg)")
        return caminho

    def abrir_imagem(self):
        caminho = self.selecionar_arquivo()
        if caminho:
            self.caminho_imagem_original = caminho

            pixmap = QPixmap(caminho)
            self.ui.labelImagemOriginal.setPixmap(pixmap.scaled(
                self.ui.labelImagemOriginal.width(),
                self.ui.labelImagemOriginal.height(),
                Qt.AspectRatioMode.KeepAspectRatio
            ))

            self.ui.labelImagemProcessada.clear()
            self.ui.labelImagemProcessada.setText("Imagem com Detecção")
            self.ui.labelResultado.setText("Resultado: (Aguardando processamento)")
            self.ui.labelResultado.setStyleSheet("")

    def processar_imagem(self):
        if not self.caminho_imagem_original:
            return

        self.ui.btnProcessar.setEnabled(False)
        self.ui.btnProcessar.setText("Processando...")

        self.worker = Worker(self.caminho_imagem_original)
        self.worker.finished.connect(self.atualizar_interface)
        self.worker.start()

    def atualizar_interface(self, caminho_saida, com_fissura):
        pixmap = QPixmap(caminho_saida)
        self.ui.labelImagemProcessada.setPixmap(pixmap.scaled(
            self.ui.labelImagemProcessada.width(),
            self.ui.labelImagemProcessada.height(),
            Qt.AspectRatioMode.KeepAspectRatio
        ))

        if com_fissura:
            self.ui.labelResultado.setText("Resultado: Fissura detectada")
            self.ui.labelResultado.setStyleSheet("color: red; font-weight: bold;")
        else:
            self.ui.labelResultado.setText("Resultado: Sem fissura detectada")
            self.ui.labelResultado.setStyleSheet("color: green; font-weight: bold;")

        self.ui.btnProcessar.setEnabled(True)
        self.ui.btnProcessar.setText("Processar")
        self.worker = None


if __name__ == "__main__":
    app = QApplication()
    janela = JanelaPrincipal()
    janela.setWindowTitle("Classificador de Fissuras - Rafael Felipe")
    janela.show()
    exit(app.exec())