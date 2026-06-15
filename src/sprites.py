import pygame
import random

# Puxa as medidas da tela que ficam guardadas no config.py
from src.config import LARGURA_TELA, ALTURA_TELA

# Aqui definimos como o tabuleiro vai ser montado.
Colunas = 4
Linhas  = 4

# Tamanho visual de cada carta na tela (em pixels), carta maior ou menor
Largura_Carta = 100
Altura_Carta  = 100
Espaco        = 15

# Onde está o arquivo com todas as imagens das cartas
Caminho_Spritesheet = "assets/imagens/spritesheet.bmp"

# Posições de cada carta na imagem (x, y, largura, altura)
Sprites_Faces = [
    (0,   0,   100, 100), (100, 0,   100, 100), (200, 0,   100, 100), (300, 0,   100, 100),
    (0,   100, 100, 100), (100, 100, 100, 100), (200, 100, 100, 100), (300, 100, 100, 100)
]

# O verso é a imagem que aparece quando a carta ainda não foi virada
Sprite_Verso = (400, 0, 100, 100)


#Recorta só o pedaço que a gente quer.
def pegar_sprite(local_arquivo, x, y, width, height):
    """Corta um único elemento de uma spritesheet BMP e remove o fundo."""

    #Carrega o BMP e usa .convert() (sem alpha) para otimizar a velocidade
    sheet = pygame.image.load(local_arquivo).convert()

    #Cria uma superfície padrão para o recorte (não precisa de SRCALPHA aqui)
    image = pygame.Surface((width, height))

    #Copia o pedaço da folha BMP para a nossa nova imagem
    image.blit(sheet, (0, 0), (x, y, width, height))

    # Remove o fundo da imagem para que fique transparente na hora de desenhar
    cor_do_fundo = image.get_at((0, 0))

    # Dizemos ao Pygame para ignorar essa cor específica na hora de desenhar
    image.set_colorkey(cor_do_fundo)

    return image


#Cartas do jogo(posição, imagem, estado)
class Carta:
    def __init__(self, id_par, imagem_face, imagem_verso, x, y):
        # id_par identifica qual par essa carta pertence (id igual significa que são do mesmo par)
        self.id_par = id_par

        self.imagem_face  = imagem_face   # imagem da frente (o desenho da carta)
        self.imagem_verso = imagem_verso  # imagem do verso (o que aparece escondido)

        # retangulo define onde a carta vai aparecer na tela e qual o seu tamanho
        self.retangulo = pygame.Rect(x, y, Largura_Carta, Altura_Carta)

        self.virada    = False  # vira pra True quando o jogador clica na carta
        self.encontrada = False  # vira pra True quando o par é descoberto

    def desenhar(self, tela):
        # se a carta foi clicada ou o par já foi encontrado, mostra a face
        if self.virada or self.encontrada:
            tela.blit(self.imagem_face, self.retangulo)   # exibe a face na posição da carta
        else:
            tela.blit(self.imagem_verso, self.retangulo)  # exibe o verso na posição da carta

        # TODO: borda e detecção de clique serão adicionadas ao integrar com jogo.py


# Monta o tabuleiro completo: cria os pares, embaralha e distribui as cartas na tela.
def criar_tabuleiro():

    # divide por 2 porque cada par tem 2 cartas
    total_pares = (Colunas * Linhas) // 2

    # carrega o verso uma vez só e reutiliza pra todas as cartas
    imagem_verso = pegar_sprite(
        Caminho_Spritesheet,
        Sprite_Verso[0], Sprite_Verso[1],
        Sprite_Verso[2], Sprite_Verso[3]
    )

    # para cada par, cria duas entradas na lista (uma pra cada carta do par)
    pares = []
    for id_par in range(total_pares):
        sx, sy, sw, sh = Sprites_Faces[id_par]
        imagem_face = pegar_sprite(Caminho_Spritesheet, sx, sy, sw, sh)
        pares.append((id_par, imagem_face))  # primeira carta do par
        pares.append((id_par, imagem_face))  # segunda carta do par (igual)

    # embaralha pra que as cartas apareçam em posições diferentes a cada partida
    random.shuffle(pares)

    # calcula o tamanho total que o tabuleiro vai ocupar na tela
    largura_total = Colunas * Largura_Carta + (Colunas - 1) * Espaco
    altura_total  = Linhas  * Altura_Carta  + (Linhas  - 1) * Espaco

    # descobre quanto deslocar pra deixar o tabuleiro centralizado na tela
    offset_x = (LARGURA_TELA - largura_total) // 2
    offset_y  = (ALTURA_TELA  - altura_total)  // 2

    # posiciona cada carta na sua linha e coluna dentro do grid
    cartas = []
    for indice, (id_par, imagem_face) in enumerate(pares):
        coluna_atual = indice % Colunas  # ex: índice 5 → coluna 1 (5 % 4 = 1)
        linha_atual  = indice // Colunas  # ex: índice 5 → linha 1  (5 // 4 = 1)

        # calcula a posição x e y final da carta na tela
        x = offset_x + coluna_atual * (Largura_Carta + Espaco)
        y = offset_y  + linha_atual  * (Altura_Carta  + Espaco)

        cartas.append(Carta(id_par, imagem_face, imagem_verso, x, y))

    return cartas


# Passa por todas as cartas e manda cada uma se desenhar na tela
def desenhar_cartas(tela, cartas):
    """Desenha todas as cartas na tela."""
    for carta in cartas:
        carta.desenhar(tela)
