from src.funcoes import calcular_pontos, jogador_perdeu, limitar_valor
from src.funcoes import somar_tentativa, reiniciar_jogo
import src.dados as dados

def test_calcular_pontos():
    """Deve somar corretamente os pontos atuais com os pontos ganhos."""
    assert calcular_pontos(10, 5) == 15


def test_jogador_perdeu_com_zero_vidas():
    """Deve indicar derrota quando o total de vidas chega a zero."""
    assert jogador_perdeu(0) is True


def test_jogador_nao_perdeu_com_vidas():
    """Nao deve indicar derrota quando o jogador ainda tem vidas."""
    assert jogador_perdeu(3) is False


def test_limitar_valor_abaixo_do_minimo():
    """Deve retornar o limite minimo quando o valor informado for menor."""
    assert limitar_valor(-5, 0, 100) == 0


def test_limitar_valor_acima_do_maximo():
    """Deve retornar o limite maximo quando o valor informado for maior."""
    assert limitar_valor(150, 0, 100) == 100


def test_limitar_valor_dentro_do_intervalo():
    """Deve manter o valor original quando ele ja estiver no intervalo."""
    assert limitar_valor(50, 0, 100) == 50

def test_reiniciar_jogo():
    "Testa se, depois de reiniciar o jogo, as tentativas voltam a ser 0 e o tabuleiro volta a configuração inicial"
    dados.inicializar_tabuleiro()
    assert reiniciar_jogo(9) == 0
    assert len(dados.cartas) == 12

def test_somar_tentativa():
    "Testa se a função somar_tentativa soma corretamente o número de tentativas"
    assert somar_tentativa(2, 3) == 4

def test_somar_tentativa_sem_duas_cartas():
    "Testa se a função somar_tentativa não soma tentativas quando não há exatamente duas cartas selecionadas"
    assert somar_tentativa(1, 3) == 3