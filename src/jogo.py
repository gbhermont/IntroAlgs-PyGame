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
    TEXTO
)

def detectar_clique(pos_mouse):
    """Passa por todas as cartas para ver se o mouse clicou em alguma"""
    for i in range(len(dados.cartas)):
        carta = dados.cartas[i]

        if carta['x'] <= pos_mouse[0] <= carta['x'] + carta['largura']:
            if carta['y'] <= pos_mouse[1] <= carta['y'] + carta['altura']:
                if not carta['virada'] and not carta['descoberta']:
                    carta['virada'] = True
                    dados.cartas_selecionadas.append(i) 

def atualizar_jogo(tela):
    if len(dados.cartas_selecionadas) == 2:
        
        desenhar_elementos(tela)
        pygame.time.wait(800) 
        
        pos1 = dados.cartas_selecionadas[0]
        pos2 = dados.cartas_selecionadas[1]
        
        carta1 = dados.cartas[pos1]
        carta2 = dados.cartas[pos2]
        
        if carta1['id'] == carta2['id']:
            carta1['descoberta'] = True
            carta2['descoberta'] = True
        else:
            carta1['virada'] = False
            carta2['virada'] = False

        dados.cartas_selecionadas.clear()

def desenhar_elementos(tela):
    tela.fill(FUNDO)
    fonte = pygame.font.SysFont("Arial", 40)
    
    for carta in dados.cartas:
        if carta['virada'] or carta['descoberta']:
            pygame.draw.rect(tela, (240, 240, 240), (carta['x'], carta['y'], carta['largura'], carta['altura']))
            txt = fonte.render(str(carta['id']), True, TEXTO)
            tela.blit(txt, (carta['x'] + 40, carta['y'] + 25))
        else:
            pygame.draw.rect(tela, CARTA, (carta['x'], carta['y'], carta['largura'], carta['altura']))
            
    pygame.display.update()

def executar_jogo():
    pygame.init()

    tela = pygame.display.set_mode((LARGURA_TELA, ALTURA_TELA))
    pygame.display.set_caption(TITULO_JOGO)

    relogio = pygame.time.Clock()

    dados.inicializar_tabuleiro()

    rodando = True

    while rodando:
        relogio.tick(FPS)

        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                rodando = False

            if evento.type == pygame.KEYDOWN:
                if evento.key == pygame.K_ESCAPE:
                    rodando = False
            
            # DETECTA CLIQUE DO MOUSE
            if evento.type == pygame.MOUSEBUTTONDOWN:
                if evento.button == 1: # Botão esquerdo
                    detectar_clique(evento.pos)
                    
        atualizar_jogo(tela)

        desenhar_elementos(tela)

    pygame.quit()

executar_jogo()