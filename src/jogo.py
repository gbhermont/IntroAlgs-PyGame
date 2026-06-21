import pygame
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

from src.funcoes import desenhar_botao, desenhar_tentativas, somar_tentativa, reiniciar_jogo

def detectar_clique_reiniciar(pos_mouse, tentativas):
    "Detecta se o clique do mouse foi no botão de reiniciar e, se sim, reinicia o jogo"
    retangulo_botao = pygame.Rect(320, 540, 160, 40) 
    if retangulo_botao.collidepoint(pos_mouse):
        return reiniciar_jogo(tentativas)
    return tentativas

def executar_jogo():
    """Executa o loop principal do jogo: verificar eventos, desenhar tela, atualizar tela, controlar FPS"""
    pygame.init()

    tela = pygame.display.set_mode((LARGURA_TELA, ALTURA_TELA))
    pygame.display.set_caption(TITULO_JOGO)

    relogio = pygame.time.Clock()
    
    dados.inicializar_tabuleiro()

    tentativas = 0
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
                    tentativas = detectar_clique_reiniciar(evento.pos, tentativas)
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
    if len(dados.cartas_selecionadas) >= 2: #essa verificacao faz com que o sistema não deixe o jogador continuar clicando antes de processar se ele acertou ou não o par
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


def atualizar_jogo(tela, tentativas):
    """Verifica se o par de cartas escolhido é igual ou diferente"""
    if len(dados.cartas_selecionadas) == 2:

        desenhar_elementos(tela, tentativas)
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

        tentativas = somar_tentativa(len(dados.cartas_selecionadas), tentativas) #usa a funcao que soma as tentativas (tem q deixar antes do clear)
        dados.cartas_selecionadas.clear()
    return tentativas

def desenhar_elementos(tela, tentativas):
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
    desenhar_tentativas(tela, tentativas, fonte)
    desenhar_botao(tela)
    pygame.display.update()

executar_jogo()
