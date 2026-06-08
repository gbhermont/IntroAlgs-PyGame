import random

def salvar_recorde(caminho_arquivo, pontuacao):
    with open(caminho_arquivo, "w", encoding="utf-8") as arquivo:
        arquivo.write(str(pontuacao))


def carregar_recorde(caminho_arquivo):
    try:
        with open(caminho_arquivo, "r", encoding="utf-8") as arquivo:
            conteudo = arquivo.read().strip()

            if conteudo == "":
                return 0

            return int(conteudo)

    except FileNotFoundError:
        return 0

cartas = []
cartas_selecionadas = [] 

def inicializar_tabuleiro():
    global cartas, cartas_selecionadas
    valores = [1, 1, 2, 2, 3, 3, 4, 4]
    random.shuffle(valores)  
    
    coluna = 0
    linha = 0
    
    for valor in valores:
        x = 70 + coluna * 120
        y = 120 + linha * 120

        carta = {
            'id': valor,
            'x': x,
            'y': y,
            'largura': 100,
            'altura': 100,
            'virada': False,    
            'descoberta': False   
        }
        cartas.append(carta)
        
        coluna = coluna + 1
        if coluna == 4:
            coluna = 0
            linha = linha + 1