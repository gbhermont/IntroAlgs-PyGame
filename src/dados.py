import random

def salvar_recorde(caminho_arquivo, pontuacao):
    """Salva a pontuação recorde em arquivo texto."""
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
    """Gera as cartas, define suas posições na tela e embaralha"""
    global cartas, cartas_selecionadas
    valores = [1, 1, 2, 2, 3, 3, 4, 4, 5, 5, 6, 6]
    random.shuffle(valores)  
    
    coluna = 0
    linha = 0
    
    for valor in valores:
        """Calcula a posição X e Y de cada carta na tela"""
        x = 100 + coluna * 120
        y = 160 + linha * 120

        """Cria o dicionário com os dados individuais da carta"""
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
        
        """Organiza o desenho em 4 colunas por linha"""
        coluna = coluna + 1
        if coluna == 6:
            coluna = 0
            linha = linha + 1