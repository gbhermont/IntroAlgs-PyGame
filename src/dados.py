import random
import pygame

cartas = []
cartas_selecionadas = []

imagens_frente = {}
imagens_verso = None

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


def carregar_recursos_imagens():
    """Carrega as imagens da pasta assets e armazena em um dicionário utilizando o ID como chave."""
    global imagens_frente, imagens_verso
    
    tamanho_carta = (180, 180)
    
    try:
        imagens_verso = pygame.image.load("assets/imagens/verso.jpg")
        imagens_verso = pygame.transform.scale(imagens_verso, tamanho_carta)
        
        for i in range(1, 7):
            img = pygame.image.load(f"assets/imagens/img{i}.jpg")
            imagens_frente[i] = pygame.transform.scale(img, tamanho_carta)
    except pygame.error as e:
        print(f"Erro ao carregar imagens: {e}")
        
def inicializar_tabuleiro():
    """Gera as cartas para um grid de 4 colunas e 3 linhas centralizado com tamanho 130x130"""
    global cartas, cartas_selecionadas
    
    carregar_recursos_imagens()
    
    # 6 pares de IDs (total de 12 cartas)
    valores = [1, 1, 2, 2, 3, 3, 4, 4, 5, 5, 6, 6]
    random.shuffle(valores)  
    
    coluna = 0
    linha = 0
    
    margem_x = 120
    margem_y = 80 
    espacamento = 12
    
    for valor in valores:
        x = margem_x + coluna * (180 + espacamento)
        y = margem_y + linha * (180 + espacamento)

        carta = {
            'id': valor,
            'x': x,
            'y': y,
            'largura': 180, 
            'altura': 180, 
            'virada': False,    
            'descoberta': False 
        }
        cartas.append(carta)
        
        coluna += 1
        if coluna == 4: # QUEBRA A LINHA A CADA 4 COLUNAS
            coluna = 0
            linha += 1