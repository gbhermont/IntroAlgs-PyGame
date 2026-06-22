import pygame
import src.dados as dados
import src.config as config
from src.config import FUNDO, TEXTO


def desenhar_botao(tela):
    fonte = pygame.font.SysFont("Arial", 25, True, False)
    
    retangulo_botao = pygame.Rect(820, 30, 150, 38) 
    pygame.draw.rect(tela, (config.BOTAO), retangulo_botao, border_radius=8)
    
    texto_botao = fonte.render("Reiniciar", True, (255, 255, 255))
    texto_posicao = texto_botao.get_rect(center=retangulo_botao.center)
    tela.blit(texto_botao, texto_posicao)
    return retangulo_botao

def desenhar_tentativas(tela,tentativas):
    fonte_hud = pygame.font.SysFont("Arial", 28, True, False)
    texto = fonte_hud.render(f"Tentativas: {tentativas}", True, config.TEXTO) 
    posicao_texto = texto.get_rect(topright=(1340, 34)) #pega o retângulo do texto e posiciona ele no canto superior direito da tela
    tela.blit(texto, posicao_texto) #desenha o texto na tela usando a posição definida

def desenhar_texto(tela,texto,x,y,cor,fonte): 
    '''Essa função é uma função genérica para desenhar o texto em qualquer lugar da tela através dos parametros.
    tela: janela do jogo
    texto: o que deve ser escrito
    x e y: posicoes (largura e altura respectivamente)
    cor: cor em rgb
    fonte: fonte desejada'''
    caixa_texto = fonte.render(texto, True, cor) #renderiza o texto usando a fonte e a cor passados como parametro
    tela.blit(caixa_texto, (x,y)) #desenha o texto na tela usando as coordenadas x e y passadas como parametro

def somar_tentativa(cartas_selecionadas, tentativas):
    if cartas_selecionadas == 2:
        tentativas +=1

    return tentativas
    
def reiniciar_jogo(tentativas):
    "zera as tentativas e redefine o tabuleiro"
    "a funcao usa tentativas como parametro para resetar o contador de tentativas e retorna ele zerado"
    dados.cartas.clear() 
    dados.cartas_selecionadas.clear() 
    dados.inicializar_tabuleiro() 
    return 0 

def condicao_vitoria(): #macla
    """Verifica se todas as cartas estão com os pares encontrados"""
    if len(dados.cartas) == 0:
        return False
    for carta in dados.cartas:
        if not carta["descoberta"]:
            return False
    return True

def passar_fase(venceu, fase_atual):
    "A função recebe venceu como parâmetro e, se for True, aumenta 1 na fase e retorna ela"
    if venceu:
        fase_atual +=1
    return fase_atual

def detectar_clique_reiniciar(pos_mouse, nivel):
    """Detecta se o clique foi no botão reiniciar. Se sim, reinicia o nivel atual e retorna True."""
    retangulo_botao = pygame.Rect(820, 30, 160, 38)
    if retangulo_botao.collidepoint(pos_mouse):
        dados.cartas.clear()
        dados.cartas_selecionadas.clear()
        dados.inicializar_tabuleiro(nivel)
        return True
    return False

def menu_inicio(tela):
    """
    Exibe a tela de menu inicial em formato de card.
    Gera um loop próprio para capturar o nome do jogador antes de iniciar o jogo.
    Retorna uma string com o nome digitado.
    """
    # --- Configurações de Fontes ---
    # Define os tamanhos e estilos das fontes para o título, subtítulo e campos de texto
    fonte_titulo = pygame.font.SysFont("Arial", 42, bold=True)
    fonte_subtitulo = pygame.font.SysFont("Arial", 24, bold=True)
    fonte_input = pygame.font.SysFont("Arial", 28)
    fonte_rodape = pygame.font.SysFont("Arial", 16)
    
    # --- Variáveis de Controle ---
    nome = ""                # Armazena o texto que o jogador está digitando
    rodando_menu = True      # Controla o loop da janela do menu
    relogio = pygame.time.Clock()

    # --- Paleta de Cores do Card ---
    # Cores no formato RGB utilizadas para estilizar a interface do menu
    COR_CARD = (240, 244, 248)          # Cor de fundo do card (branco azulado)
    COR_TEXTO_CARD = (40, 50, 60)       # Cor do texto principal dentro do card
    COR_CAIXA_TEXTO = (210, 220, 230)   # Cor de fundo do campo de digitação
    COR_DESTAQUE = (70, 130, 180)       # Cor azul usada no título e na borda externa

    # --- Posicionamento dos Elementos ---
    # Define o retângulo do Card principal de forma centralizada na tela
    largura_card, altura_card = 550, 350
    x_card = (tela.get_width() - largura_card) // 2
    y_card = (tela.get_height() - altura_card) // 2
    rect_card = pygame.Rect(x_card, y_card, largura_card, altura_card)

    # Define o retângulo do campo de digitação interno (Input Box)
    largura_input, altura_input = 400, 50
    x_input = rect_card.centerx - (largura_input // 2)
    y_input = rect_card.top + 190
    rect_input = pygame.Rect(x_input, y_input, largura_input, altura_input)

    # Define o retângulo do botão "Ver Ranking", entre o campo de texto e o rodapé
    largura_btn_ranking, altura_btn_ranking = 220, 36
    x_btn_ranking = rect_card.centerx - (largura_btn_ranking // 2)
    y_btn_ranking = rect_card.top + 248
    rect_btn_ranking = pygame.Rect(x_btn_ranking, y_btn_ranking, largura_btn_ranking, altura_btn_ranking)

    # --- Loop Principal do Menu ---
    while rodando_menu:
        # Garante que o menu rode travado a 60 quadros por segundo
        relogio.tick(60)
        
        # --- Captura de Eventos ---
        for evento in pygame.event.get():
            # Fecha o programa caso o usuário clique no 'X' da janela
            if evento.type == pygame.QUIT:
                pygame.quit()
                exit()
            
            # Gerencia as teclas pressionadas pelo usuário
            if evento.type == pygame.KEYDOWN:
                # Se pressionar ENTER, valida o texto e encerra o menu
                if evento.key == pygame.K_RETURN:
                    if nome.strip() == "":
                        nome = "Jogador" # Define nome padrão caso esteja em branco
                    rodando_menu = False
                
                # Se pressionar BACKSPACE, remove o último caractere digitado
                elif evento.key == pygame.K_BACKSPACE:
                    nome = nome[:-1]
                
                # Caso seja outra tecla, adiciona ao nome (com limite de 15 caracteres)
                else:
                    if len(nome) < 15 and evento.unicode.isprintable():
                        nome += evento.unicode
                # Se clicar no botão "Ver Ranking", abre a tela de ranking
            if evento.type == pygame.MOUSEBUTTONDOWN and evento.button == 1:
                if rect_btn_ranking.collidepoint(evento.pos):
                    tela_ranking(tela)

        # --- Desenho dos Elementos na Tela ---
        
        # 1. Preenche a tela de fundo (atrás do card) com a cor padrão do jogo
        tela.fill(FUNDO)

        # 2. Desenha o Card centralizado (retângulo preenchido com cantos arredondados)
        pygame.draw.rect(tela, COR_CARD, rect_card, border_radius=25)
        
        # 3. Desenha o contorno/borda fina do Card para dar acabamento
        pygame.draw.rect(tela, COR_DESTAQUE, rect_card, width=3, border_radius=25)

        # 4. Renderiza as superfícies de texto estáticas do menu
        texto_jogo = fonte_titulo.render(config.TITULO_JOGO, True, COR_DESTAQUE)
        texto_chamada = fonte_subtitulo.render("Digite seu nome para começar:", True, COR_TEXTO_CARD)
        texto_instrucao = fonte_rodape.render("Pressione ENTER para jogar", True, (120, 130, 140))

        # 5. Desenha os textos na tela alinhando-os ao centro horizontal do Card
        tela.blit(texto_jogo, texto_jogo.get_rect(center=(rect_card.centerx, rect_card.top + 60)))
        tela.blit(texto_chamada, texto_chamada.get_rect(center=(rect_card.centerx, rect_card.top + 130)))
        tela.blit(texto_instrucao, texto_instrucao.get_rect(center=(rect_card.centerx, rect_card.bottom - 30)))

        # 6. Desenha a caixinha interna onde o texto será exibido
        pygame.draw.rect(tela, COR_CAIXA_TEXTO, rect_input, border_radius=10)
        
        # 7. Renderiza dinamicamente o nome que o jogador está digitando
        texto_nome = fonte_input.render(nome, True, COR_TEXTO_CARD)
        
        # 8. Desenha o nome dentro da caixinha aplicando um espaçamento (offset) na esquerda e centralizando verticalmente
        pos_x_texto = rect_input.x + 15
        pos_y_texto = rect_input.y + (rect_input.height - texto_nome.get_height()) // 2
        tela.blit(texto_nome, (pos_x_texto, pos_y_texto))

        # 9. Desenha o botão "Ver Ranking"
        pygame.draw.rect(tela, config.BOTAO, rect_btn_ranking, border_radius=8)
        texto_btn_ranking = fonte_subtitulo.render("Ver Ranking", True, (255, 255, 255))
        tela.blit(texto_btn_ranking, texto_btn_ranking.get_rect(center=rect_btn_ranking.center))

        # --- Atualização da Janela ---
        # Atualiza a tela a cada frame para renderizar as modificações
        pygame.display.update()

        
    # Retorna o nome final obtido para o script principal
    return nome

def tela_ranking(tela):
    """
    Exibe a tela de ranking em formato de card, listando nome e tempo
    dos jogadores, ordenados do menor para o maior tempo.
    """
    fonte_titulo = pygame.font.SysFont("Arial", 36, bold=True)
    fonte_linha = pygame.font.SysFont("Arial", 24)
    fonte_vazio = pygame.font.SysFont("Arial", 22)

    COR_CARD = (240, 244, 248)
    COR_TEXTO_CARD = (40, 50, 60)
    COR_DESTAQUE = (70, 130, 180)
    COR_LINHA_PAR = (225, 232, 240)

    largura_card, altura_card = 600, 600
    x_card = (tela.get_width() - largura_card) // 2
    y_card = (tela.get_height() - altura_card) // 2
    rect_card = pygame.Rect(x_card, y_card, largura_card, altura_card)

    largura_btn, altura_btn = 160, 40
    rect_btn_voltar = pygame.Rect(
        rect_card.centerx - largura_btn // 2,
        rect_card.bottom - 60,
        largura_btn,
        altura_btn,
    )

    ranking = dados.carregar_ranking()
    MAX_LINHAS_VISIVEIS = 12
    ranking_exibido = ranking[:MAX_LINHAS_VISIVEIS]

    rodando_ranking = True
    relogio = pygame.time.Clock()

    while rodando_ranking:
        relogio.tick(60)

        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                pygame.quit()
                exit()

            if evento.type == pygame.KEYDOWN:
                if evento.key in (pygame.K_ESCAPE, pygame.K_RETURN):
                    rodando_ranking = False

            if evento.type == pygame.MOUSEBUTTONDOWN and evento.button == 1:
                if rect_btn_voltar.collidepoint(evento.pos):
                    rodando_ranking = False

        tela.fill(FUNDO)

        pygame.draw.rect(tela, COR_CARD, rect_card, border_radius=25)
        pygame.draw.rect(tela, COR_DESTAQUE, rect_card, width=3, border_radius=25)

        texto_titulo = fonte_titulo.render("Ranking - Melhores Tempos", True, COR_DESTAQUE)
        tela.blit(texto_titulo, texto_titulo.get_rect(center=(rect_card.centerx, rect_card.top + 45)))

        x_posicao = rect_card.left + 40
        x_nome    = rect_card.left + 110
        x_tempo   = rect_card.right - 120
        y_topo_lista = rect_card.top + 95

        for indice, (nome, tempo) in enumerate(ranking_exibido):
            y_linha = y_topo_lista + indice * 36
            rect_linha = pygame.Rect(rect_card.left + 20, y_linha - 4, largura_card - 40, 32)
            if indice % 2 == 0:
                pygame.draw.rect(tela, COR_LINHA_PAR, rect_linha, border_radius=6)
            texto_posicao = fonte_linha.render(f"{indice + 1}.", True, COR_TEXTO_CARD)
            texto_nome    = fonte_linha.render(nome, True, COR_TEXTO_CARD)
            texto_tempo   = fonte_linha.render(f"{tempo}s", True, COR_TEXTO_CARD)
            tela.blit(texto_posicao, (x_posicao, y_linha))
            tela.blit(texto_nome, (x_nome, y_linha))
            tela.blit(texto_tempo, (x_tempo, y_linha))

        pygame.draw.rect(tela, config.BOTAO, rect_btn_voltar, border_radius=8)
        texto_voltar = fonte_linha.render("Voltar", True, (255, 255, 255))
        tela.blit(texto_voltar, texto_voltar.get_rect(center=rect_btn_voltar.center))

        pygame.display.update()