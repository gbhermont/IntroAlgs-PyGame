import pygame
import src.dados as dados
import src.config as config

def calcular_pontos(pontos_atual, pontos_ganhos):
    """Soma os pontos ganhos à pontuação atual."""
    return pontos_atual + pontos_ganhos


def tomar_dano(vida_atual, dano):
    """Reduz a vida atual com base no dano recebido."""
    return vida_atual - dano


def jogador_perdeu(vidas):
    """Indica se o jogador ficou sem vidas."""
    return vidas <= 0


def limitar_valor(valor, minimo, maximo):
    """Mantém um valor dentro do intervalo [minimo, maximo]."""
    if valor < minimo:
        return minimo
    if valor > maximo:
        return maximo
    return valor


def verificar_colisao(retangulo_1, retangulo_2):
    """Verifica sobreposição entre dois retângulos do Pygame."""
    return retangulo_1.colliderect(retangulo_2)

def desenhar_botao(tela):
    fonte = pygame.font.SysFont("Arial", 32, True, False)
    
    # Centralizado de forma perfeita em relação ao novo grid de cartas (X=350, Y=645)
    retangulo_botao = pygame.Rect(600, 30, 200, 45) 
    pygame.draw.rect(tela, (config.BOTAO), retangulo_botao, border_radius=8)
    
    texto_botao = fonte.render("Reiniciar", True, (255, 255, 255))
    texto_posicao = texto_botao.get_rect(center=retangulo_botao.center)
    tela.blit(texto_botao, texto_posicao)
    return retangulo_botao

def desenhar_tentativas(tela,tentativas,fonte):
    texto = fonte.render(f"Tentativas: {tentativas}", True, (0,0,0)) #faz o texto na cor preta(0,0,0) usando a fonte que passei como parametro
    posicao_texto = texto.get_rect(topright=(1350, 30)) #pega o retângulo do texto e posiciona ele no canto superior direito da tela
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
    dados.cartas.clear() #limpa a lista de cartas para reiniciar o jogo
    dados.cartas_selecionadas.clear() #limpa a lista de cartas selecionadas
    dados.inicializar_tabuleiro() #inicia o tabuleiro dnv
    return 0 #retorna 0 para resetar as tentativas

def condicao_vitoria():
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
    #fase = passar_fase(venceu) -> implementar isso no fluxo do jogo dps

def detectar_clique_reiniciar(pos_mouse, nivel):
    """Detecta se o clique foi no botão reiniciar. Se sim, reinicia o nivel atual e retorna True."""
    retangulo_botao = pygame.Rect(600, 30, 200, 45)
    if retangulo_botao.collidepoint(pos_mouse):
        dados.cartas.clear()
        dados.cartas_selecionadas.clear()
        dados.inicializar_tabuleiro(nivel)
        return True
    return False
