import pygame
import src.dados as dados
from src.funcoes import menu_inicio

from src.config import (
    LARGURA_TELA,
    ALTURA_TELA,
    FPS,
    TITULO_JOGO,
    FUNDO,
    CARTA,
    TEXTO,
    BOTAO,
    TEMPO_TELA_VITORIA,
    NIVEL_MAXIMO,
)

from src.funcoes import (
    desenhar_botao,
    desenhar_tentativas,
    somar_tentativa,
    reiniciar_jogo,
    condicao_vitoria,
    passar_fase,
    detectar_clique_reiniciar,
    menu_inicio
)


def executar_jogo():
    """
    Loop principal do jogo.
    Começa no nivel 1, avança automaticamente para o 2 e depois para o 3.
    Ao vencer o nivel 3 o jogo encerra.
    """
    pygame.init()

    tela = pygame.display.set_mode((LARGURA_TELA, ALTURA_TELA))
    pygame.display.set_caption(TITULO_JOGO)

    relogio = pygame.time.Clock()

    nome_jogador = menu_inicio(tela)
    
    if nome_jogador == "":
        nome_jogador = "Jogador"  #macla

    """começa sempre no nivel 1 (facil)"""
    nivel = 1
    dados.inicializar_tabuleiro(nivel)

    tentativas        = 0
    venceu            = False
    jogo_concluido    = False  # True quando o nivel 3 foi vencido
    tempo_inicio_vitoria = 0

    tempo_inicio = pygame.time.get_ticks()
    tempo_atual  = 0
    rodando      = True

    while rodando:
        relogio.tick(FPS)

        """o tempo só sobe enquanto o jogador ainda não venceu o nivel atual"""
        if not venceu:
            tempo_atual = (pygame.time.get_ticks() - tempo_inicio) // 1000

        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                rodando = False

            if evento.type == pygame.KEYDOWN:
                if evento.key == pygame.K_ESCAPE:
                    rodando = False

            """só processa cliques enquanto o nivel ainda está ativo"""
            if evento.type == pygame.MOUSEBUTTONDOWN and evento.button == 1 and not venceu:
                if detectar_clique_reiniciar(evento.pos, nivel):
                    """reiniciou: zera tentativas e tempo do nivel atual"""
                    tentativas   = 0
                    tempo_inicio = pygame.time.get_ticks()
                else:
                    detectar_clique(evento.pos)

        """verifica pares e acumula tentativas enquanto o nivel está ativo"""
        if not venceu:
            tentativas = atualizar_jogo(tela, tentativas, venceu, tempo_atual, nivel, nome_jogador)

            if condicao_vitoria():
                venceu               = True
                jogo_concluido       = (nivel == NIVEL_MAXIMO)
                tempo_inicio_vitoria = pygame.time.get_ticks()
                dados.salvar_no_ranking(nome_jogador, tempo_atual)
                dados.verificar_e_salvar_recorde(tempo_atual)

        """
        Transição automática de nivel.
        Depois de TEMPO_TELA_VITORIA milissegundos mostrando o card de vitória,
        avança pro proximo nivel. Se era o ultimo, encerra o jogo.
        """
        tempo_na_tela_vitoria = pygame.time.get_ticks() - tempo_inicio_vitoria

        if venceu and not jogo_concluido and tempo_na_tela_vitoria >= TEMPO_TELA_VITORIA:
            nivel += 1
            dados.inicializar_tabuleiro(nivel)
            tentativas   = 0
            venceu       = False
            tempo_atual  = 0
            tempo_inicio = pygame.time.get_ticks()

        if jogo_concluido and tempo_na_tela_vitoria >= TEMPO_TELA_VITORIA:
            rodando = False

        if rodando:
            desenhar_elementos(tela, tentativas, venceu, tempo_atual, nivel, nome_jogador)

    pygame.quit()


def detectar_clique(pos_mouse):
    """Passa por todas as cartas para ver se o mouse clicou em alguma"""
    if len(dados.cartas_selecionadas) >= 2:
        return
    for i in range(len(dados.cartas)):
        carta = dados.cartas[i]

        """Verifica se o clique bateu dentro do quadrado da carta"""
        if carta["x"] <= pos_mouse[0] <= carta["x"] + carta["largura"]:
            if carta["y"] <= pos_mouse[1] <= carta["y"] + carta["altura"]:
                """Garante que a carta só vira se estiver fechada"""
                if not carta["virada"] and not carta["descoberta"]:
                    carta["virada"] = True
                    dados.cartas_selecionadas.append(i)


def atualizar_jogo(tela, tentativas, venceu, tempo_atual, nivel, nome_jogador):
    """Verifica se o par de cartas escolhido é igual ou diferente e retorna o número atual de tentativas"""
    if len(dados.cartas_selecionadas) == 2:

        desenhar_elementos(tela, tentativas, venceu, tempo_atual, nivel, nome_jogador)
        pygame.time.wait(800)

        """Pega a posição das duas cartas que foram clicadas"""
        pos1 = dados.cartas_selecionadas[0]
        pos2 = dados.cartas_selecionadas[1]

        carta1 = dados.cartas[pos1]
        carta2 = dados.cartas[pos2]

        """Se forem iguais, o jogador acertou o par"""
        if carta1["id"] == carta2["id"]:
            carta1["descoberta"] = True
            carta2["descoberta"] = True
        else:
            carta1["virada"] = False
            carta2["virada"] = False

        tentativas = somar_tentativa(len(dados.cartas_selecionadas), tentativas)
        dados.cartas_selecionadas.clear()

    return tentativas


def desenhar_card_vitoria(tela, nome_jogador, tentativas, tempo=0, nivel=1):
    """Desenha um pop-up gráfico (card) centralizado com os resultados do nivel."""
    largura_card, altura_card = 500, 280
    x_card = (LARGURA_TELA - largura_card) // 2
    y_card = (ALTURA_TELA  - altura_card)  // 2
    rect_card = pygame.Rect(x_card, y_card, largura_card, altura_card)

    pygame.draw.rect(tela, (224, 242, 241), rect_card, border_radius=20)

    fonte_titulo = pygame.font.SysFont("Arial", 36, bold=True)
    fonte_dados  = pygame.font.SysFont("Arial", 26)

    """mensagem diferente dependendo se é o ultimo nivel ou não"""
    if nivel == NIVEL_MAXIMO:
        msg_titulo = "Você zerou o jogo!"
    else:
        msg_titulo = f"Nivel {nivel} concluído!"

    texto_titulo    = fonte_titulo.render(msg_titulo, True, (120, 220, 255))
    texto_subtitulo = fonte_dados.render("Você encontrou todos os pares!", True, TEXTO)
    texto_resultado = fonte_dados.render(f"Tentativas: {tentativas}", True, TEXTO)
    texto_tempo     = fonte_dados.render(f"Tempo: {tempo}s", True, TEXTO)
    texto_nome = fonte_dados.render(f"Jogador: {nome_jogador}", True, TEXTO)

    # --- Posições ---
    # Centraliza o Título bem no topo do card
    tela.blit(texto_titulo, texto_titulo.get_rect(center=(rect_card.centerx, rect_card.top + 45)))
    
    # Coloca o Nome do Jogador logo abaixo do título (Y = top + 95)
    tela.blit(texto_nome, texto_nome.get_rect(center=(rect_card.centerx, rect_card.top + 95)))
    
    # Desce o Subtítulo um pouco mais para baixo (Y = top + 145)
    tela.blit(texto_subtitulo, texto_subtitulo.get_rect(center=(rect_card.centerx, rect_card.top + 145)))
    
    # Mostra as Tentativas (Y = top + 195)
    tela.blit(texto_resultado, texto_resultado.get_rect(center=(rect_card.centerx, rect_card.top + 195)))
    
    # Mostra o Tempo no final do card (Y = top + 245)
    tela.blit(texto_tempo, texto_tempo.get_rect(center=(rect_card.centerx, rect_card.top + 245)))


def desenhar_elementos(tela, tentativas, venceu, tempo, nivel, nome_jogador):
    """Desenha o fundo, as cartas, o HUD e o card de vitória se necessário."""
    tela.fill(FUNDO)
    fonte = pygame.font.SysFont("Arial", 40)

    for carta in dados.cartas:
        posicao_carta = (carta["x"], carta["y"])
        
        if carta["virada"] or carta["descoberta"]:
            imagem_frente = dados.imagens_frente[carta["id"]]
            tela.blit(imagem_frente, posicao_carta)
        else:
            tela.blit(dados.imagens_verso, posicao_carta)

    if venceu:
        desenhar_card_vitoria(tela, nome_jogador, tentativas, tempo, nivel)

    desenhar_tentativas(tela, tentativas, fonte)
    desenhar_botao(tela)

    """exibe o nivel atual, o tempo e o recorde no canto superior esquerdo"""
    fonte_hud = pygame.font.SysFont("Arial", 28)

    tela.blit(fonte_hud.render(f"Nivel: {nivel}", True, TEXTO),  (20, 30))
    tela.blit(fonte_hud.render(f"Tempo: {tempo}s", True, TEXTO), (160, 30))

    recorde = dados.carregar_recorde("data/recorde.txt")
    if recorde > 0:
        tela.blit(fonte_hud.render(f"Recorde: {recorde}s", True, TEXTO), (20, 100))
    
    texto_nome = fonte_hud.render(
    f"Jogador: {nome_jogador}",
    True,
    TEXTO
)
    tela.blit(fonte_hud.render(f"Recorde: {recorde}s", True, TEXTO), (320, 30))

    tela.blit(texto_nome, (20, 140))
    pygame.display.update()
