import random
import pygame

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

def verificar_e_salvar_recorde(tempo_segundos):
    """Verifica se o jogador bateu o recorde e retorna o valor dele se sim"""
    
    recorde_atual = carregar_recorde(Caminho_Recorde)
    novo_recorde = recorde_atual == 0 or tempo_segundos < recorde_atual
    if novo_recorde:
        salvar_recorde(Caminho_Recorde, tempo_segundos)
    return novo_recorde

def salvar_no_ranking(nome_jogador, tempo_segundos):
    """
    Adiciona o nome do jogador e o tempo da partida no ranking
    Salva uma linha 'nome,tempo' no arquivo de ranking.
    """
    nome_tratado = nome_jogador.strip().replace(",", "") or "Jogador"
    with open(Caminho_Ranking, "a", encoding="utf-8") as arquivo:
        arquivo.write(f"{nome_tratado},{tempo_segundos}\n")


def carregar_ranking(caminho_arquivo=Caminho_Ranking):
    """
    Lê o arquivo de ranking e devolve uma lista de tuplas (nome, tempo)
    ordenada do menor para o maior tempo (melhor tempo primeiro).
    Linhas antigas que só tem o tempo (sem nome) aparecem como 'Anônimo'.
    """
    ranking = []

    with open(caminho_arquivo, "r", encoding="utf-8") as arquivo:
        for linha in arquivo:
            linha = linha.strip()
            if linha == "":
                continue

            if "," in linha:
                nome, tempo_texto = linha.split(",", 1)
                nome = nome.strip() or "Anônimo"
            else:
                nome = "Anônimo"
                tempo_texto = linha

            try:
                tempo = int(tempo_texto.strip())
            except ValueError:
                continue  

            ranking.append((nome, tempo))


    ranking.sort(key=lambda registro: registro[1])
    return ranking

def imagem_com_bordas_arredondadas(imagem, raio):
    """
    Cria uma cópia da imagem com as bordas arredondadas usando o raio definido.
    Cria uma superfície do mesmo tamanho com suporte a transparência
    """
    rect = imagem.get_rect()
    superficie_alvo = pygame.Surface(rect.size, pygame.SRCALPHA)
    
    """Desenha um retângulo com cantos arredondados na nova superfície"""
    pygame.draw.rect(superficie_alvo, (255, 255, 255, 255), rect, border_radius=raio)
    
    """Aplica a imagem original por cima, cortando apenas onde o retângulo foi desenhado"""
    superficie_alvo.blit(imagem, (0, 0), special_flags=pygame.BLEND_RGBA_MIN)
    
    return superficie_alvo

def carregar_recursos_imagens(nivel):
    """
    Carrega as imagens da pasta assets e arredonda suas bordas
    Como temos quantidades diferentes de cartas em cada um dos níveis, elas tiveram que ter tamnhos diferentes em cada um deles:
    nivel 1: 180
    nivel 2: 150
    nivel 3: 150 (pois tem o mesmo número de linhas que o nível 2)
    """
    global imagens_frente, imagens_verso
    
    if nivel == 1:
        tamanho_carta = (180, 180)
    elif nivel == 2:
        tamanho_carta = (150, 150)  
    else:
        tamanho_carta = (150, 150)
        
    raio_borda = 10

    """Limpa as frentes do nível anterior para não misturar dados"""
    imagens_frente = {}
    
    try:
        img_verso_crua = pygame.image.load("assets/imagens/verso.jpg")
        img_verso_redimensionada = pygame.transform.scale(img_verso_crua, tamanho_carta)
        imagens_verso = imagem_com_bordas_arredondadas(img_verso_redimensionada, raio_borda)
        
        """
        Carrega imagens diferentes de acordo com o nível através dos ifs e do iterador do for
        """
        if nivel == 1:
            for i in range(1, 7):
                img_crua = pygame.image.load(f"assets/imagens/divas{i}.jpg")
                img_redimensionada = pygame.transform.scale(img_crua, tamanho_carta)
                imagens_frente[i] = imagem_com_bordas_arredondadas(img_redimensionada, raio_borda)
        elif nivel == 2:
            for i in range(1, 9):
                img_crua = pygame.image.load(f"assets/imagens/casais{i}.jpg")
                img_redimensionada = pygame.transform.scale(img_crua, tamanho_carta)
                imagens_frente[i] = imagem_com_bordas_arredondadas(img_redimensionada, raio_borda)
        else:
            for i in range(1, 11):
                img_crua = pygame.image.load(f"assets/imagens/eles{i}.jpg")
                img_redimensionada = pygame.transform.scale(img_crua, tamanho_carta)
                imagens_frente[i] = imagem_com_bordas_arredondadas(img_redimensionada, raio_borda)
            
    except pygame.error as e:
        print(f"Erro ao carregar imagens: {e}")

def inicializar_tabuleiro(nivel=1):
    """
    Gera as cartas do tabuleiro e define suas posições e quantidade de linhas e colunas de acordo com o nivel escolhido.
    Nivel 1 (facil)  : 4 colunas x 3 linhas = 12 cartas, 
    Nivel 2 (medio)  : 4 colunas x 4 linhas = 16 cartas, 
    Nivel 3 (dificil): 5 colunas x 4 linhas = 20 cartas,
    """
    global cartas, cartas_selecionadas

    cartas = []
    cartas_selecionadas = []

    carregar_recursos_imagens(nivel)
    
    espacamento = 12

    if nivel == 1:
        colunas, linhas = 4, 3
        margem_x, margem_y = 320, 140
        tamanho = 180
    elif nivel == 2:
        colunas, linhas = 4, 4
        margem_x, margem_y = 400, 120
        tamanho = 150
    else:
        colunas, linhas = 5, 4
        margem_x, margem_y = 320, 120
        tamanho = 150

    total_cartas = colunas * linhas
    total_pares  = total_cartas // 2
    
    """
    Gera a estrutura lógica do tabuleiro e calcula o posicionamento geográfico das cartas na tela.
    Cria uma lista de identificadores únicos duplicados para formar os pares obrigatórios
    e aplica um o random para garantir o embaralhamento do jogo.
    Ao atingir o limite estipulado de colunas, colunas fica igual a 0 e avança para a próxima linha.
    """

    ids = []
    for i in range(total_pares):
        id_carta = i + 1  
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