from src.funcoes import (
    desenhar_botao,
    somar_tentativa,
    reiniciar_jogo,
    condicao_vitoria,
    passar_fase,
    detectar_clique_reiniciar,
)
import src.dados as dados

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

def test_somar_tentativa():
    assert somar_tentativa(2, 4) == 5


def test_somar_tentativa_sem_par():
    assert somar_tentativa(1, 4) == 4


def test_reiniciar_jogo():
    dados.inicializar_tabuleiro(1)

    assert reiniciar_jogo(10) == 0
    assert len(dados.cartas) > 0


def test_condicao_vitoria_false():
    dados.inicializar_tabuleiro(1)

    assert condicao_vitoria() is False


def test_condicao_vitoria_true():
    dados.inicializar_tabuleiro(1)

    for carta in dados.cartas:
        carta["descoberta"] = True

    assert condicao_vitoria() is True


def test_passar_fase():
    assert passar_fase(True, 1) == 2


def test_nao_passar_fase():
    assert passar_fase(False, 2) == 2


def test_detectar_clique_reiniciar():
    dados.inicializar_tabuleiro(1)

    # Dentro do botão
    assert detectar_clique_reiniciar((610, 40), 1) is True


def test_detectar_clique_reiniciar_fora():
    dados.inicializar_tabuleiro(1)

    assert detectar_clique_reiniciar((0, 0), 1) is False