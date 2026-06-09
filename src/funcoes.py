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


#DESENVOLVIMENTO DO PROJETO JOGO DA MEMÓRIA

import pygame

def desenhar_botao(tela):
    fonte = pygame.font.SysFont("Arial", 32, True, False)
    '''a função recebe a tela, define a posição do botão, desenha ele e retorna o retângulo do botão para ser usado na detecção de clique'''
    retangulo_botao = pygame.Rect(320, 540, 160, 40) 
    pygame.draw.rect(tela, (100, 100, 100), retangulo_botao, border_radius=8)
    '''escrever reiniciar no centro do botao'''
    texto_botao = fonte.render("Reiniciar", True, (255, 255, 255))
    texto_posicao = texto_botao.get_rect(center=retangulo_botao.center) #posicao da caixa do botao
    tela.blit(texto_botao, texto_posicao)
    return retangulo_botao

def desenhar_tentativas(tela,tentativas,fonte):
    texto = fonte.render(f"Tentativas: {tentativas}", True, (0,0,0)) #faz o texto na cor preta(0,0,0) usando a fonte que passei como parametro
    posicao_texto = texto.get_rect(topright=(780, 20)) #pega o retângulo do texto e posiciona ele no canto superior direito da tela
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
    