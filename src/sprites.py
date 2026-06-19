# import pygame
# import random

# from src.config import LARGURA_TELA, ALTURA_TELA

# """
# Configurações do tabuleiro.
# Muda Colunas e Linhas pra ajustar o tamanho do grid.
# Muda Largura_Carta e Altura_Carta pra deixar as cartas maiores ou menores.
# """
# Colunas = 4
# Linhas  = 4

# Largura_Carta = 100  
# Altura_Carta  = 100  
# Espaco        = 15   

# """
# Caminho para a spritesheet, que é a imagem única
# que contém todos os sprites das cartas juntos.
# """
# Caminho_Spritesheet = "assets/imagens/spritesheet.bmp"

# """
# Cada linha aqui diz onde está um sprite dentro da spritesheet.
# O formato é (x, y, largura, altura), como se fosse recortar com uma tesoura.
# A primeira começa no pixel (0,0), a segunda em (100,0), e assim por diante.
# """
# Sprites_Faces = [
#     (0,   0,   100, 100),  # carta 1
#     (100, 0,   100, 100),  # carta 2
#     (200, 0,   100, 100),  # carta 3
#     (300, 0,   100, 100),  # carta 4
#     (0,   100, 100, 100),  # carta 5
#     (100, 100, 100, 100),  # carta 6
#     (200, 100, 100, 100),  # carta 7
#     (300, 100, 100, 100),  # carta 8
# ]

# """
# Posição do verso dentro da spritesheet.
# É a imagem que aparece quando a carta ainda não foi virada pelo jogador.
# """
# Sprite_Verso = (400, 0, 100, 100)


# def pegar_sprite(local_arquivo, x, y, width, height):
#     """Corta um único elemento de uma spritesheet BMP e remove o fundo."""

#     """1. Carrega o BMP e usa .convert() (sem alpha) para otimizar a velocidade"""
#     sheet = pygame.image.load(local_arquivo).convert()

#     """2. Cria uma superfície padrão para o recorte (não precisa de SRCALPHA aqui)"""
#     image = pygame.Surface((width, height))

#     """3. Copia o pedaço da folha BMP para a nossa nova imagem"""
#     image.blit(sheet, (0, 0), (x, y, width, height))

#     """
#     4. CONFIGURAÇÃO DA TRANSPARÊNCIA (O segredo para o BMP)
#     Pegamos a cor do pixel no canto superior esquerdo (0,0) do recorte,
#     assumindo que o fundo do seu sprite começa ali.
#     """
#     cor_do_fundo = image.get_at((0, 0))

#     """Dizemos ao Pygame para ignorar essa cor específica na hora de desenhar"""
#     image.set_colorkey(cor_do_fundo)

#     return image


# class Carta:
#     """
#     Representa uma carta do jogo.
#     Guarda a imagem, a posição na tela e o estado atual dela (virada ou encontrada).
#     """

#     def __init__(self, id_par, imagem_face, imagem_verso, x, y):
#         """
#         id_par        : identifica o par — duas cartas com o mesmo id formam um par válido
#         imagem_face   : o desenho da frente da carta
#         imagem_verso  : o que aparece quando a carta ainda está escondida
#         x, y          : posição da carta na tela
#         """
#         self.id_par = id_par
#         self.imagem_face  = imagem_face
#         self.imagem_verso = imagem_verso

#         """retangulo guarda a posição e o tamanho da carta, usado pra desenhar e futuramente pra detectar clique"""
#         self.retangulo = pygame.Rect(x, y, Largura_Carta, Altura_Carta)

#         self.virada     = False  # True quando o jogador clicou nessa carta
#         self.encontrada = False  # True quando o par dela já foi descoberto

#     def desenhar(self, tela):
#         """
#         Decide qual lado da carta mostrar.
#         Se foi clicada ou o par foi encontrado, mostra a face. Caso contrário, mantém o verso.
#         """
#         if self.virada or self.encontrada:
#             tela.blit(self.imagem_face, self.retangulo)   # exibe a face na posição da carta
#         else:
#             tela.blit(self.imagem_verso, self.retangulo)  # exibe o verso na posição da carta

#         # TODO: borda e detecção de clique serão adicionadas ao integrar com jogo.py


# def criar_tabuleiro():
#     """
#     Monta o tabuleiro inteiro.
#     Cria os pares de cartas, embaralha e calcula a posição de cada uma na tela.
#     Retorna uma lista com todos os objetos Carta já prontos.
#     """

#     """divide por 2 porque cada par tem 2 cartas"""
#     total_pares = (Colunas * Linhas) // 2

#     """carrega o verso uma vez só e reutiliza pra todas as cartas, sem precisar recarregar"""
#     imagem_verso = pegar_sprite(
#         Caminho_Spritesheet,
#         Sprite_Verso[0], Sprite_Verso[1],
#         Sprite_Verso[2], Sprite_Verso[3]
#     )

#     """pra cada par, adiciona duas cartas iguais na lista — uma pra cada metade do par"""
#     pares = []
#     for id_par in range(total_pares):
#         sx, sy, sw, sh = Sprites_Faces[id_par]
#         imagem_face = pegar_sprite(Caminho_Spritesheet, sx, sy, sw, sh)
#         pares.append((id_par, imagem_face))  # primeira carta do par
#         pares.append((id_par, imagem_face))  # segunda carta do par

#     """embaralha pra que as posições sejam diferentes a cada partida"""
#     random.shuffle(pares)

#     """calcula o tamanho total do tabuleiro somando cartas e espaços"""
#     largura_total = Colunas * Largura_Carta + (Colunas - 1) * Espaco
#     altura_total  = Linhas  * Altura_Carta  + (Linhas  - 1) * Espaco

#     """descobre o deslocamento necessário pra centralizar o tabuleiro na tela"""
#     offset_x = (LARGURA_TELA - largura_total) // 2
#     offset_y  = (ALTURA_TELA  - altura_total)  // 2

#     """posiciona cada carta na sua linha e coluna dentro do grid"""
#     cartas = []
#     for indice, (id_par, imagem_face) in enumerate(pares):
#         coluna_atual = indice % Colunas  # ex: índice 5 → coluna 1 (5 % 4 = 1)
#         linha_atual  = indice // Colunas  # ex: índice 5 → linha 1  (5 // 4 = 1)

#         x = offset_x + coluna_atual * (Largura_Carta + Espaco)
#         y = offset_y  + linha_atual  * (Altura_Carta  + Espaco)

#         cartas.append(Carta(id_par, imagem_face, imagem_verso, x, y))

#     return cartas


# def desenhar_cartas(tela, cartas):
#     """Passa por todas as cartas e manda cada uma se desenhar na tela."""
#     for carta in cartas:
#         carta.desenhar(tela)
