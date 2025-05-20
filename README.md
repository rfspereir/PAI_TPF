# Classificador de Fissuras em Concreto — Trabalho Final

Projeto desenvolvido para a disciplina de **Processamento e Análise de Imagens** do curso de **Engenharia de Computação - PUC Minas (2025)**.

## 🎯 Objetivo

Criar um sistema de **classificação automática de fissuras em estruturas de concreto**, a partir de imagens RGB reais, utilizando técnicas de pré-processamento, limiarização automática e análise binária.

O sistema determina se uma imagem apresenta fissura ou não, com base na proporção de pixels após binarização.

## 🧠 Metodologia

Fluxo de processamento:
1. **Carregamento da imagem RGB**.
2. **Conversão para escala de cinza (8 bits)**.
3. **Redimensionamento proporcional para padronização**.
4. **Aplicação de filtro de mediana 3x3 para remoção de ruídos**.
5. **Cálculo automático do limiar usando o método de Otsu**.
6. **Limiarização (binarização) da imagem**.
7. **Classificação com base na proporção de pixels brancos**:
   - Mais de 1% → **Fissura detectada**.
   - Até 1% → **Sem fissura detectada**.

A imagem binarizada é salva no disco com nome derivado do original.

## 💻 Interface Gráfica

A interface, desenvolvida com PySide6 (Qt), permite:
- Selecionar uma imagem RGB.
- Visualizar lado a lado:
  - Imagem original.
  - Imagem processada (binarizada).
- Exibir dinamicamente o diagnóstico de presença ou ausência de fissura.

## 🗂️ Estrutura de Pastas

```
TPF/
├── assets/
│   ├── interface.ui           # Interface Qt (editável)
│   ├── interface.py           # Interface convertida pelo PySide6
│   └── processamento.py       # Funções de processamento de imagem
├── images/
│   ├── image1.jpg             # Exemplos de entrada
│   └── image1_binarizada107.jpg  # Saídas geradas
├── main.py                    # Script principal da aplicação
├── requirements.txt           # Dependências do projeto
└── LICENSE
```

## 🧪 Como Executar

1. Instale as dependências:

```bash
pip install -r requirements.txt
```

2. Execute o arquivo principal:

```bash
python main.py
```

3. A interface será aberta para seleção da imagem e visualização do resultado.

## 📦 Requisitos

- Python 3.8 ou superior
- Pillow
- PySide6

## 👨‍💻 Autor

**Rafael Felipe Silva Pereira**  
Engenharia de Computação — PUC Minas