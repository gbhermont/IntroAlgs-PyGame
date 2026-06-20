import pygame

"""
Tamanho de cada carta na tela em pixels.
Se quiser cartas maiores ou menores, muda esses valores aqui.
"""
Largura_Carta = 100
Altura_Carta  = 100
Espaco        = 15


def pegar_sprite(local_arquivo, x, y, width, height):
    """Corta um único elemento de uma spritesheet BMP e remove o fundo."""

    """1. Carrega o BMP e usa .convert() (sem alpha) para otimizar a velocidade"""
    sheet = pygame.image.load(local_arquivo).convert()

    """2. Cria uma superfície padrão para o recorte (não precisa de SRCALPHA aqui)"""
    image = pygame.Surface((width, height))

    """3. Copia o pedaço da folha BMP para a nossa nova imagem"""
    image.blit(sheet, (0, 0), (x, y, width, height))

    """
    4. CONFIGURAÇÃO DA TRANSPARÊNCIA (O segredo para o BMP)
    Pegamos a cor do pixel no canto superior esquerdo (0,0) do recorte,
    assumindo que o fundo do seu sprite começa ali.
    """
    cor_do_fundo = image.get_at((0, 0))

    """Dizemos ao Pygame para ignorar essa cor específica na hora de desenhar"""
    image.set_colorkey(cor_do_fundo)

    return image


class Carta:
    """
    Representa uma carta do jogo.
    Guarda a imagem, a posição na tela e o estado atual dela (virada ou encontrada).
    """

    def __init__(self, id_par, imagem_face, imagem_verso, x, y):
        """
        id_par        : identifica o par — duas cartas com o mesmo id formam um par válido
        imagem_face   : o desenho da frente da carta
        imagem_verso  : o que aparece quando a carta ainda está escondida
        x, y          : posição da carta na tela
        """
        self.id_par       = id_par
        self.imagem_face  = imagem_face
        self.imagem_verso = imagem_verso

        """retangulo guarda a posição e o tamanho da carta, usado pra desenhar e futuramente pra detectar clique"""
        self.retangulo = pygame.Rect(x, y, Largura_Carta, Altura_Carta)

        self.virada     = False  # True quando o jogador clicou nessa carta
        self.encontrada = False  # True quando o par dela já foi descoberto

    def desenhar(self, tela):
        """
        Decide qual lado da carta mostrar.
        Se foi clicada ou o par foi encontrado, mostra a face. Caso contrário, mantém o verso.
        """
        if self.virada or self.encontrada:
            tela.blit(self.imagem_face, self.retangulo)   # exibe a face na posição da carta
        else:
            tela.blit(self.imagem_verso, self.retangulo)  # exibe o verso na posição da carta
