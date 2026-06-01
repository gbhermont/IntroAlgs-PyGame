#Match Up 

Projeto final da disciplina de Introdução a Algoritmos/Programação, desenvolvido com Python e Pygame.

Este repositório é um template para os grupos da disciplina. A proposta é começar com uma base funcional e evoluir o jogo ao longo do semestre.

## Integrantes do grupo

Nome 1: Gabriel de Souza Junqueira Hermont -
Nome 2: Kemily Eduardo da Luz - 
Nome 3: Maria Clara Soalheiro Bessa - 
Nome 4: Armando Schoenstatt Rodrigues e Moreira 

Tipo de jogo: Jogo de Memória 

## Estrutura do projeto

- `main.py`: ponto de entrada da aplicação.
- `config.py`: guardará as configurações principais, como tamanho da tela, cores e FPS.
- `jogo.py`: terá o loop principal e o controle das telas.
- `cartas.py`: cuidará da criação, embaralhamento e verificação dos pares de cartas.
- `funcoes.py`: terá funções auxiliares, como desenhar textos e botões. 
- `src/`: código-fonte principal do jogo (loop, regras, sprites e dados).
- `assets/`: imagens, fontes e sons.
- `data/`: arquivos persistentes (recorde/ranking).
- `tests/`: testes unitários com `pytest`.
- `docs/`: documentação do projeto, incluindo proposta inicial.

## Descrição do jogo

No jogo de memória, aparece na tela um tabuleiro com cartas viradas para baixo, além de informações como número de tentativas gastas e opção de reiniciar. O jogador controla o mouse e escolhe as cartas clicando nelas para revelá-las. O objetivo é encontrar todos os pares iguais, memorizando a posição de cada carta. Durante a partida, o desafio é lembrar onde cada imagem está e fazer as combinações corretas. O jogo termina quando todos os pares forem encontrados. 

Exemplo:

> Exemplo: O jogo do Mico, onde você deve achar o par de cada animal correspondente.
> 
## Objetivo do jogador

Objetivo do jogador: Encontrar todos os pares de cartas no menor número de tentativas possível. 

Exemplo:

>Encontrar todos os pares de cartas no menor número de tentativas possível.


## Regras do jogo

Regra 1: O jogador pode virar apenas duas cartas por vez. 
Regra 2: Se as duas cartas escolhidas forem iguais, elas permanecem viradas e contam como um par encontrado.
Regra 3: Se as cartas forem diferentes, elas ficam visíveis por alguns segundos e depois voltam a ficar viradas para baixo. 
Regra 4: O jogador deve continuar jogando até encontrar todos os pares do tabuleiro.
Regra 5: O número de tentativas será contado durante toda a partida 
Condição de vitória: O jogador vence quando consegue encontrar todos os pares de cartas do tabuleiro. 
Condição de derrota ou encerramento: A partida termina quando o jogador encontra todos os pares de cartas ou fecha a janela do jogo. 

Exemplo:

- O jogador usa o click do mouse para virar as cartas.
- Ter 2 cartas iguais mostra que ele acertou o par
- Caso o contrário ele tem que tentar readivinhar o par de novo


## Controles

O jogador escolherá as cartas com o click do seu mouse

Exemplo:

- Click do mouse
- ESC: sair do jogo
- Botão fechar janela (X): encerrar o jogo
- Botão de reiniciar (mouse): iniciar uma nova partida. 

## Como executar o projeto

### 1. Clonar o repositório

```bash
git clone LINK_DO_REPOSITORIO
cd NOME_DA_PASTA
pip install -r requirements.txt
python main.py
```

## Como executar os testes

```bash
python -m pytest
```

## Checklist mínimo para entrega

- Preencher este README com nome final, descrição real, regras e controles do jogo.
- Atualizar `docs/proposta.MD` com a proposta do grupo.
- Garantir que o jogo executa com `python main.py`.
- Garantir que os testes passam com `pytest`.

## Observações para os alunos

- Mantenham o código organizado em módulos pequenos e com responsabilidade clara.
- Comentem partes importantes da lógica, principalmente regras do jogo.
- Registrem decisões técnicas no README do grupo ao longo do desenvolvimento.
