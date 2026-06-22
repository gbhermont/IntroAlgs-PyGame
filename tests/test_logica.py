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

def test_condicao_vitoria_false():
    "Testa se a função condicao_vitoria retorna False quando nem todas as cartas estão descobertas"
    dados.inicializar_tabuleiro(1)

    assert condicao_vitoria() is False


def test_condicao_vitoria_true():
    "testa se a função condicao_vitoria retorna True quando todas as cartas estão descobertas. "
    "Para isso, inicializa o tabuleiro e marca todas as cartas como descobertas antes de chamar a função."
    dados.inicializar_tabuleiro(1)

    for carta in dados.cartas:
        carta["descoberta"] = True

    assert condicao_vitoria() is True


def test_passar_fase():
    "Testa se a função passar_fase retorna o próximo nível quando a fase é passada com sucesso. "
    assert passar_fase(True, 1) == 2


def test_nao_passar_fase():
    "Testa se a função passar_fase retorna o mesmo nível quando a fase não é passada com sucesso."
    assert passar_fase(False, 2) == 2


def test_detectar_clique_reiniciar():
    "Testa se a função detectar_clique_reiniciar retorna True quando o clique ocorre dentro do botão de reiniciar. "
    dados.inicializar_tabuleiro(1)

    # Dentro do botão
    assert detectar_clique_reiniciar((610, 40), 1) is True


def test_detectar_clique_reiniciar_fora():
    "Testa se a função detectar_clique_reiniciar retorna False quando o clique ocorre fora do botão de reiniciar. "
    dados.inicializar_tabuleiro(1)

    assert detectar_clique_reiniciar((0, 0), 1) is False