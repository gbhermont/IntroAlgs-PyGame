import random
import pygame

# Caminhos dos arquivos de recorde e ranking
Caminho_Recorde = "data/recorde.txt"
Caminho_Ranking = "data/ranking.txt"

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


# Verifica se o jogador bateu o recorde e salva se sim
def verificar_e_salvar_recorde(tempo_segundos):
    recorde_atual = carregar_recorde(Caminho_Recorde)
    novo_recorde = recorde_atual == 0 or tempo_segundos < recorde_atual
    if novo_recorde:
        salvar_recorde(Caminho_Recorde, tempo_segundos)
    return novo_recorde


# Adiciona o tempo da partida no ranking
def salvar_no_ranking(tempo_segundos):
    with open(Caminho_Ranking, "a", encoding="utf-8") as arquivo:
        arquivo.write(str(tempo_segundos) + "\n")


def imagem_com_bordas_arredondadas(imagem, raio):
    """Cria uma cópia da imagem com as bordas arredondadas usando o raio definido."""
    # Cria uma superfície do mesmo tamanho com suporte a transparência
    rect = imagem.get_rect()
    superficie_alvo = pygame.Surface(rect.size, pygame.SRCALPHA)
    
    # Desenha um retângulo com cantos arredondados na nova superfície (cor branca total)
    pygame.draw.rect(superficie_alvo, (255, 255, 255, 255), rect, border_radius=raio)
    
    # Aplica a imagem original por cima, cortando apenas onde o retângulo foi desenhado
    superficie_alvo.blit(imagem, (0, 0), special_flags=pygame.BLEND_RGBA_MIN)
    
    return superficie_alvo

def carregar_recursos_imagens():
    """Carrega as imagens da pasta assets e arredonda suas bordas"""
    global imagens_frente, imagens_verso
    
    tamanho_carta = (180, 180)
    raio_borda = 10 
    
    try:
        # 1. Carrega, redimensiona e arredonda o VERSO
        img_verso_crua = pygame.image.load("assets/imagens/verso.jpg")
        img_verso_redimensionada = pygame.transform.scale(img_verso_crua, tamanho_carta)
        imagens_verso = imagem_com_bordas_arredondadas(img_verso_redimensionada, raio_borda)
        
        # 2. Carrega, redimensiona e arredonda as FRENTES
        for i in range(1, 7):
            img_crua = pygame.image.load(f"assets/imagens/img{i}.jpg")
            img_redimensionada = pygame.transform.scale(img_crua, tamanho_carta)
            
            # Guarda no dicionário já com a borda cortada arredondada!
            imagens_frente[i] = imagem_com_bordas_arredondadas(img_redimensionada, raio_borda)
            
    except pygame.error as e:
        print(f"Erro ao carregar imagens: {e}")
        
def inicializar_tabuleiro(nivel=1):
    """
    Gera as cartas do tabuleiro de acordo com o nivel escolhido.
    Nivel 1 (facil)  : 4x3 = 12 cartas, cartas de 180x180
    Nivel 2 (medio)  : 4x4 = 16 cartas, cartas de 140x140
    Nivel 3 (dificil): 5x4 = 20 cartas, cartas de 120x120
    """
    global cartas, cartas_selecionadas

    cartas = []
    cartas_selecionadas = []

    carregar_recursos_imagens()

    # define as configuracoes do grid baseado no nivel
    if nivel == 1:
        colunas, linhas, tamanho, margem_x, margem_y = 4, 3, 180, 320, 160
        espacamento = 12
    elif nivel == 2:
        colunas, linhas, tamanho, margem_x, margem_y = 4, 4, 140, 380, 100
        espacamento = 60
    else:
        colunas, linhas, tamanho, margem_x, margem_y = 5, 4, 120, 270, 100
        espacamento = 70

    total_cartas = colunas * linhas
    total_pares  = total_cartas // 2

    # cria os pares de ids — repete cada id duas vezes
    ids = []
    for i in range(total_pares):
        id_carta = (i % 6) + 1  # reaproveita as 6 imagens ciclicamente
        ids.append(id_carta)
        ids.append(id_carta)
    random.shuffle(ids)

    coluna = 0
    linha  = 0

    for valor in ids:
        x = margem_x + coluna * (tamanho + espacamento)
        y = margem_y + linha  * (tamanho + espacamento)

        carta = {
            'id'        : valor,
            'x'         : x,
            'y'         : y,
            'largura'   : tamanho,
            'altura'    : tamanho,
            'virada'    : False,
            'descoberta': False
        }
        cartas.append(carta)

        coluna += 1
        if coluna == colunas:
            coluna = 0
            linha += 1