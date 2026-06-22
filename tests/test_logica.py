from src.funcoes import calcular_pontos, jogador_perdeu, limitar_valor
from src.funcoes import somar_tentativa, reiniciar_jogo
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