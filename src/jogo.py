import pygame
import sys
import src.dados as dados

from src.config import (
    LARGURA_TELA,
    ALTURA_TELA,
    FPS,
    TITULO_JOGO,
    FUNDO,
    CARTA,
    BOTAO,
    TEXTO,
)

def executar_jogo():
    """Executa o loop principal do jogo: verificar eventos, desenhar tela, atualizar tela, controlar FPS"""
    pygame.init()

    tela = pygame.display.set_mode((LARGURA_TELA, ALTURA_TELA))
    pygame.display.set_caption(TITULO_JOGO)

    relogio = pygame.time.Clock()
    
    dados.inicializar_tabuleiro()

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
                    detectar_clique(evento.pos)
        
        atualizar_jogo(tela)
        desenhar_elementos(tela)

    pygame.quit()


def detectar_clique(pos_mouse):
    """Passa por todas as cartas para ver se o mouse clicou em alguma"""
    for i in range(len(dados.cartas)):
        carta = dados.cartas[i]
        
        """Verifica se o clique bateu dentro do quadrado da carta"""
        if carta["x"] <= pos_mouse[0] <= carta["x"] + carta["largura"]:
            if carta["y"] <= pos_mouse[1] <= carta["y"] + carta["altura"]:
                """Garante que a carta só vira se estiver fechada"""
                if not carta["virada"] and not carta["descoberta"]:
                    carta["virada"] = True
                    dados.cartas_selecionadas.append(i)


def atualizar_jogo(tela):
    """Verifica se o par de cartas escolhido é igual ou diferente"""
    if len(dados.cartas_selecionadas) == 2:

        desenhar_elementos(tela)
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

        dados.cartas_selecionadas.clear()


def desenhar_elementos(tela):
    """Desenha o fundo da janela e o estado atual de todas as cartas"""
    tela.fill(FUNDO)
    fonte = pygame.font.SysFont("Arial", 40)

    for carta in dados.cartas:
        """Desenha a carta aberta mostrando o seu número"""
        if carta["virada"] or carta["descoberta"]:
            pygame.draw.rect(
                tela,
                (240, 240, 240),
                (carta["x"], carta["y"], carta["largura"], carta["altura"]),
            )
            txt = fonte.render(str(carta["id"]), True, TEXTO)
            tela.blit(txt, (carta["x"] + 40, carta["y"] + 25))
        else:
            pygame.draw.rect(
                tela, CARTA, (carta["x"], carta["y"], carta["largura"], carta["altura"])
            )

    pygame.display.update()

executar_jogo()
