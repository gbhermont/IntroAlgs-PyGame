import pygame
import random

# Importa as constantes de configuração da tela e cores definidas em config.py
from src.config import LARGURA_TELA, ALTURA_TELA

# --- Configurações do tabuleiro ---
COLUNAS = 4               # Número de colunas de cartas
LINHAS = 4                # Número de linhas de cartas
LARGURA_CARTA = 100       # Largura de cada carta em pixels
ALTURA_CARTA = 100        # Altura de cada carta em pixels
ESPACO_ENTRE_CARTAS = 15  # Espaço entre cada carta em pixels

# Caminho para o arquivo de imagens (spritesheet)
CAMINHO_SPRITESHEET = "assets/imagens/spritesheet.bmp"

# Posições de cada face na spritesheet no formato (x, y, largura, altura)
# Cada tupla representa onde está o sprite de uma carta na imagem
SPRITES_FACES = [
    (0,   0,   100, 100),
    (100, 0,   100, 100),
    (200, 0,   100, 100),
    (300, 0,   100, 100),
    (0,   100, 100, 100),
    (100, 100, 100, 100),
    (200, 100, 100, 100),
    (300, 100, 100, 100),
]

# Posição do verso da carta na spritesheet (x, y, largura, altura)
SPRITE_VERSO = (400, 0, 100, 100)



# FUNÇÃO: pegar_sprite
# Recorta um único sprite de uma spritesheet BMP.
# Parâmetros:
#   local_arquivo: caminho do arquivo BMP
#   x, y: posição do sprite dentro da spritesheet
#   width, height: tamanho do sprite a recortar
#   scale: fator de escala (1 = tamanho original)
# Retorna: Surface do pygame com o sprite recortado

def pegar_sprite(local_arquivo, x, y, width, height):
    """Corta um único elemento de uma spritesheet BMP e remove o fundo."""

    # 1. Carrega o BMP e usa .convert() (sem alpha) para otimizar a velocidade
    sheet = pygame.image.load(local_arquivo).convert()

    # 2. Cria uma superfície padrão para o recorte (não precisa de SRCALPHA aqui)
    image = pygame.Surface((width, height))

    # 3. Copia o pedaço da folha BMP para a nossa nova imagem
    image.blit(sheet, (0, 0), (x, y, width, height))

    # 4. CONFIGURAÇÃO DA TRANSPARÊNCIA (O segredo para o BMP)
    # Pegamos a cor do pixel no canto superior esquerdo (0,0) do recorte,
    # assumindo que o fundo do seu sprite começa ali.
    cor_do_fundo = image.get_at((0, 0))

    # Dizemos ao Pygame para ignorar essa cor específica na hora de desenhar
    image.set_colorkey(cor_do_fundo)

    return image


# CLASSE: Carta
# Representa uma única carta do jogo da memória.

class Carta:
    def __init__(self, id_par, imagem_face, imagem_verso, x, y):
        """
        id_par       : número que identifica o par (cartas com mesmo id_par formam um par)
        imagem_face  : Surface com a imagem da frente da carta
        imagem_verso : Surface com a imagem do verso da carta
        x, y         : posição da carta na tela
        """
        self.id_par = id_par
        self.imagem_face = imagem_face
        self.imagem_verso = imagem_verso

        # Cria o retângulo que define posição e tamanho da carta na tela
        self.retangulo = pygame.Rect(x, y, LARGURA_CARTA, ALTURA_CARTA)

        self.virada = False     # True = carta está mostrando a face
        self.encontrada = False # True = par já foi encontrado pelo jogador

    def desenhar(self, tela):
        """Desenha a carta na tela. Mostra a face se estiver virada ou encontrada,
        caso contrário mostra o verso."""
        if self.virada or self.encontrada:
            tela.blit(self.imagem_face, self.retangulo)
        else:
            tela.blit(self.imagem_verso, self.retangulo)

        # TODO: borda e detecção de clique serão adicionadas ao integrar com jogo.py


# FUNÇÃO: criar_tabuleiro
# Cria todas as cartas, embaralha e posiciona na tela.
# Retorna uma lista de objetos Carta prontos para uso.

def criar_tabuleiro():

    # Total de pares = metade do total de cartas no tabuleiro
    total_pares = (COLUNAS * LINHAS) // 2

    # Carrega a imagem do verso uma única vez para todas as cartas
    imagem_verso = pegar_sprite(
        CAMINHO_SPRITESHEET,
        SPRITE_VERSO[0], SPRITE_VERSO[1],
        SPRITE_VERSO[2], SPRITE_VERSO[3]
    )

    # Cria dois itens por par (cada par precisa de 2 cartas iguais)
    pares = []
    for id_par in range(total_pares):
        sx, sy, sw, sh = SPRITES_FACES[id_par]
        imagem_face = pegar_sprite(CAMINHO_SPRITESHEET, sx, sy, sw, sh)
        pares.append((id_par, imagem_face))  # primeira carta do par
        pares.append((id_par, imagem_face))  # segunda carta do par

    # Embaralha a lista para que as cartas apareçam em posições aleatórias
    random.shuffle(pares)

    # Calcula a largura e altura total do tabuleiro (cartas + espaços)
    largura_total = COLUNAS * LARGURA_CARTA + (COLUNAS - 1) * ESPACO_ENTRE_CARTAS
    altura_total = LINHAS * ALTURA_CARTA + (LINHAS - 1) * ESPACO_ENTRE_CARTAS

    # Calcula o offset para centralizar o tabuleiro na tela
    offset_x = (LARGURA_TELA - largura_total) // 2
    offset_y = (ALTURA_TELA - altura_total) // 2

    # Posiciona cada carta na linha e coluna correta
    cartas = []
    for indice, (id_par, imagem_face) in enumerate(pares):
        coluna_atual = indice % COLUNAS           # qual coluna (0 a 3)
        linha_atual = indice // COLUNAS           # qual linha (0 a 3)
        x = offset_x + coluna_atual * (LARGURA_CARTA + ESPACO_ENTRE_CARTAS)
        y = offset_y + linha_atual * (ALTURA_CARTA + ESPACO_ENTRE_CARTAS)
        cartas.append(Carta(id_par, imagem_face, imagem_verso, x, y))

    return cartas

