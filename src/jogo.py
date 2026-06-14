import pygame
import src.dados as dados

from src.config import (
    LARGURA_TELA,
    ALTURA_TELA,
    FPS,
    TITULO_JOGO,
    FUNDO,
    CARTA,
    TEXTO,
)

from src.funcoes import (
    desenhar_botao,
    desenhar_tentativas,
    somar_tentativa,
    reiniciar_jogo,
)


def detectar_clique_reiniciar(pos_mouse, tentativas):
    """Detecta se o clique do mouse foi no botão de reiniciar usando a posição atualizada"""
    # Deixe essa caixinha com o mesmo tamanho que definimos em funcoes.py
    retangulo_botao = pygame.Rect(350, 645, 200, 45)
    if retangulo_botao.collidepoint(pos_mouse):
        dados.cartas.clear()
        dados.cartas_selecionadas.clear()
        dados.inicializar_tabuleiro()
        return 0, False  
    return tentativas, None


def executar_jogo():
    """Executa o loop principal do jogo: verificar eventos, desenhar tela, atualizar tela, controlar FPS"""
    pygame.init()

    tela = pygame.display.set_mode((LARGURA_TELA, ALTURA_TELA))
    pygame.display.set_caption(TITULO_JOGO)

    relogio = pygame.time.Clock()

    dados.inicializar_tabuleiro()

    tentativas = 0
    venceu = False
    rodando = True

    """Loop principal do jogo"""
    while rodando:
        relogio.tick(FPS)

        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                rodando = False

            if evento.type == pygame.KEYDOWN:
                if evento.key == pygame.K_ESCAPE:
                    rodando = False

            """"Detecta clique do mouse"""
            if evento.type == pygame.MOUSEBUTTONDOWN:
                if evento.button == 1:
                    # 1. Checa primeiro se clicou em reiniciar (funciona mesmo se já tiver vencido)
                    novas_tentativas, mudou_estado = detectar_clique_reiniciar(
                        evento.pos, tentativas
                    )
                    if mudou_estado is False:
                        tentativas = novas_tentativas
                        venceu = False
                        continue  # Pula o resto para não clicar em cartas sem querer

                    # 2. Só deixa clicar nas cartas se o jogo ainda não acabou
                    if not venceu:
                        detectar_clique(evento.pos)

        # Correção: tentativas agora é atualizada de forma segura
        tentativas = atualizar_jogo(tela, tentativas, venceu)

        if condicao_vitoria():
            venceu = True

        desenhar_elementos(tela, tentativas, venceu)

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


def atualizar_jogo(tela, tentativas, venceu):
    """Verifica se o par de cartas escolhido é igual ou diferente e retorna o número atual de tentativas"""
    if len(dados.cartas_selecionadas) == 2:

        desenhar_elementos(tela, tentativas, venceu)
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


def desenhar_elementos(tela, tentativas, venceu):
    """Desenha o fundo da janela e o estado atual de todas as cartas usando imagens"""
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
        texto_vitoria = fonte.render("Você venceu!", True, TEXTO)
        posicao = texto_vitoria.get_rect(center=(LARGURA_TELA // 2, 45))
        tela.blit(texto_vitoria, posicao)

    desenhar_tentativas(tela, tentativas, fonte)
    desenhar_botao(tela)
    pygame.display.update()


def condicao_vitoria():
    """Verifica se todas as cartas estão com os pares encontrados"""
    if len(dados.cartas) == 0:
        return False
    for carta in dados.cartas:
        if not carta["descoberta"]:
            return False
    return True
