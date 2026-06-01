# Proposta Inicial do Jogo

Este documento deve ser preenchido pelo grupo na Semana 1 do projeto.

A proposta deve apresentar uma ideia simples, clara e viável para ser desenvolvida com Python e Pygame dentro do prazo disponível.

## 1. Nome provisório do jogo

Match Up

Exemplo:

> Corrida dos Obstáculos

## 2. Integrantes do grupo

Liste os integrantes do grupo.

- Nome 1:Gabriel de Souza Junqueira Hermont
- Nome 2:Kemily Eduardo da Luz
- Nome 3:Maria Clara Soalheiro Bessa
- Nome 4:Armando Schoenstatt Rodrigues e Moreira

## 3. Tipo de jogo

Indique o tipo de jogo que será desenvolvido.

Exemplos:

- jogo de desviar de obstáculos;
- jogo de coleta de itens;
- labirinto simples;
- jogo de perguntas e respostas;
- jogo de memória;
- Pong;
- Snake;
- Breakout;
- nave desviando de meteoros;
- corrida simples com obstáculos;
- jogo de clique rápido;
- jogo de sobrevivência simples.

Tipo escolhido pelo grupo:

> Jogo de Memória

## 4. Descrição geral do jogo

Explique, em poucas linhas, como o jogo funcionará.

Procure responder:

- O que aparece na tela?
- O que o jogador controla?
- O que o jogador precisa fazer?
- Quais desafios aparecem durante a partida?

Descrição:

> No jogo Match Up, os jogadores são apresentados a um tabuleiro com diversas cartas viradas para baixo. A interface do jogo também exibe informações relevantes, como o número de tentativas realizadas e a opção de reiniciar a partida. O jogador interage com o jogo utilizando o mouse, clicando nas cartas para revelá-las. O principal objetivo é encontrar todos os pares de cartas idênticas, exigindo que o jogador memorize a posição de cada imagem. O desafio reside em recordar a localização das imagens para formar as combinações corretas. A partida é concluída quando todos os pares são descobertos. Um exemplo clássico desse tipo de jogo é o "Jogo do Mico".

## 5. Objetivo do jogador

Explique qual é o objetivo principal do jogador.

Exemplos:

- coletar o maior número possível de itens;
- sobreviver pelo maior tempo possível;
- chegar até o final do labirinto;
- acertar alvos;
- responder perguntas corretamente;
- evitar obstáculos;
- quebrar todos os blocos.

Objetivo:

Encontrar todos os pares de cartas no menor número de tentativas possível.

## 6. Regras principais

Liste as principais regras do jogo.

Exemplo:

- O jogador começa com 3 vidas.
- Cada moeda coletada vale 10 pontos.
- Cada colisão com obstáculo remove 1 vida.
- A partida termina quando as vidas chegam a zero.
- O jogador vence se alcançar 100 pontos.

Regras do grupo:

Regra 1: O jogador pode virar apenas duas cartas por vez.
Regra 2: Se as duas cartas selecionadas forem idênticas, elas permanecem visíveis e são contabilizadas como um par encontrado.
Regra 3: Caso as cartas escolhidas sejam diferentes, elas serão exibidas por um breve período e, em seguida, voltarão a ficar viradas para baixo.
Regra 4: O jogo prossegue até que todos os pares no tabuleiro sejam encontrados.
Regra 5: O número total de tentativas será registrado e exibido ao longo de toda a partida.

## 7. Condição de vitória

Explique como o jogador vence ou conclui o jogo.

Exemplos:

- atingir determinada pontuação;
- chegar ao final da fase;
- sobreviver até o tempo acabar;
- responder uma quantidade mínima de perguntas;
- quebrar todos os blocos.

Condição de vitória:

> O jogador vence a partida quando consegue encontrar e combinar todos os pares de cartas presentes no tabuleiro.

## 8. Condição de derrota ou encerramento

Explique como o jogador perde ou quando a partida termina.

Exemplos:

- perder todas as vidas;
- acabar o tempo;
- colidir com determinado obstáculo;
- errar muitas perguntas;
- deixar a bola cair, no caso de Breakout ou Pong.

Condição de derrota ou encerramento:

A partida é encerrada em duas situações: quando o jogador encontra todos os pares de cartas do tabuleiro, resultando em vitória, ou quando o jogador decide fechar a janela do jogo.

## 9. Elementos previstos no jogo

Descreva os principais elementos que farão parte do jogo.

## Jogador ou elemento principal

Exemplo:

> Um personagem controlado pelas setas do teclado.

Descrição:

> Escreva aqui.

## Obstáculos, inimigos ou desafios

Exemplo:

> Obstáculos aparecem em posições aleatórias e devem ser evitados.

Descrição:

> Escreva aqui.

## Itens, alvos ou objetos de interação

Exemplo:

> Moedas aparecem na tela e aumentam a pontuação quando coletadas.

Descrição:

> Escreva aqui.

## Pontuação, vidas, tempo ou progresso

Exemplo:

> O jogador começa com 3 vidas e ganha 10 pontos por item coletado.

Descrição:

> Escreva aqui.

## 10. Controles previstos

Informe os comandos que serão utilizados pelo jogador.

Exemplo:

- Seta para cima: mover para cima
- Seta para baixo: mover para baixo
- Seta para esquerda: mover para esquerda
- Seta para direita: mover para direita
- Espaço: realizar ação
- ESC: sair do jogo

Controles do grupo:

- Clique do mouse: Utilizado para selecionar e virar as cartas no tabuleiro.
- ESC: Tecla para sair do jogo.
- Botão fechar janela (X): Encerra o jogo.


## 11. Organização inicial do código

Explique como o grupo pretende organizar o código.

Exemplo:

main.py: Ponto de entrada principal da aplicação, responsável por iniciar o jogo.
config.py: Arquivo dedicado a armazenar as configurações globais do jogo, como dimensões da tela, paleta de cores, taxa de quadros por segundo (FPS) e outras constantes.
jogo.py: Contém o loop principal do jogo e gerencia a transição e o estado das diferentes telas (ex: menu, jogo, fim de jogo).
cartas.py: Módulo responsável pela lógica das cartas, incluindo sua criação, embaralhamento, virar/desvirar e verificação de pares.
funcoes.py: Módulo para funções auxiliares e utilitárias, como renderização de textos, criação de botões e outros elementos gráficos comuns.
src/: Diretório que abrigará o código-fonte principal do jogo, incluindo a lógica do loop, regras, sprites e dados específicos.
assets/: Diretório para armazenar todos os recursos visuais e sonoros do jogo, como imagens das cartas, fontes e efeitos sonoros.
data/: Diretório para arquivos persistentes, como o registro de recordes ou rankings de jogadores.
tests/: Diretório para os testes unitários do projeto, utilizando a ferramenta pytest.
docs/: Diretório para a documentação do projeto, incluindo esta proposta inicial e outros documentos relevantes.



Organização planejada:

> Escreva aqui.


## 12. Recursos externos previstos


Recursos previstos:

- Imagens para o jogo da memória irão ser usadas seguindo um tema específico em um banco gratuito disponível na internet.
- Sons gratuitos serão usados para enfeitar o projeto ao clique nos menus, no acerto/erro de um par de imagens durante o jogo e ao finalizar uma partida.
- Tutoriais gratuitos disponíveis na internet sobre funções e capacidades da biblioteca PyGame.
- Uma fonte personalizada será usada para deixar nosso jogo mais condizente com o tema.


## 13. Principais dificuldades esperadas

Dificuldades previstas:

- Dificuldade 1: Embaralhamento das cartas
- Dificuldade 2: Considerar 2 cartas como um "par certo"
- Dificuldade 3: Divisão de tarefas/produção do código em grupo
- Dificuldade 4: Uso da biblioteca PyGame e produção da interface gráfica
- Dificuldade 5: Organização do código/projeto em múltiplos arquivos
- Dificuldade 6: Organização do ranking do tempo
- Dificuldade 7: Contabilizar os erros

## 14. Escopo mínimo para a entrega final

Descreva qual será a versão mínima aceitável do jogo.

Esta seção é importante para evitar que o grupo escolha uma ideia grande demais.

Exemplo:

> A versão mínima do jogo terá um personagem controlado pelo teclado, obstáculos aparecendo na tela, sistema de vidas, sistema de pontuação e tela de fim de jogo.

Escopo mínimo:

> Escreva aqui.

## 15. Possíveis melhorias, caso haja tempo

Liste funcionalidades extras que o grupo poderá implementar se conseguir concluir o escopo mínimo.

Exemplos:

- tela inicial;
- sons;
- fases;
- aumento de dificuldade;
- ranking;
- animações;
- novos tipos de obstáculos;
- diferentes personagens;
- menu de pausa.

Melhorias possíveis:

- Melhoria 1:
- Melhoria 2:
- Melhoria 3:
