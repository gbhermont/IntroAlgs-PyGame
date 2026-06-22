# Proposta Inicial do Jogo

Este documento deve ser preenchido pelo grupo na Semana 1 do projeto.

A proposta deve apresentar uma ideia simples, clara e viável para ser desenvolvida com Python e Pygame dentro do prazo disponível.

## 1. Nome provisório do jogo

Match Up


## 2. Integrantes do grupo

- Nome 1:Gabriel de Souza Junqueira Hermont
- Nome 2:Kemily Eduardo da Luz
- Nome 3:Maria Clara Soalheiro Bessa
- Nome 4:Armando Schoenstatt Rodrigues e Moreira

## 3. Tipo de jogo

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

Objetivo:

Encontrar todos os pares de cartas no menor número de tentativas possível e avançar de nível.

## 6. Regras principais

Regras do grupo:

Regra 1: O jogador pode virar apenas duas cartas por vez.
Regra 2: Se as duas cartas selecionadas forem idênticas, elas permanecem visíveis e são contabilizadas como um par encontrado.
Regra 3: Caso as cartas escolhidas sejam diferentes, elas serão exibidas por um breve período e, em seguida, voltarão a ficar viradas para baixo.
Regra 4: O jogo prossegue para a próxima fase até que todos os pares no tabuleiro sejam encontrados.
Regra 5: O número total de tentativas será registrado e exibido ao longo de toda a partida.

## 7. Condição de vitória

Explique como o jogador vence ou conclui o jogo.

Condição de vitória:

> O jogador vence a partida quando consegue encontrar e combinar todos os pares de cartas presentes no tabuleiro.

## 8. Condição de derrota ou encerramento

Explique como o jogador perde ou quando a partida termina.

Condição de derrota ou encerramento:

A partida é encerrada em duas situações: quando o jogador encontra todos os pares de cartas do tabuleiro, resultando em vitória, ou quando o jogador decide fechar a janela do jogo, ou se o jogador não conseguir encontrar todos os pares no tempo estipulado.

## 9. Elementos previstos no jogo

Descreva os principais elementos que farão parte do jogo.

Cartas, tempo, tentativas.

## Jogador ou elemento principal

Descrição:

> O jogador irá interagir com o jogo por meio do mouse, clicando nas cartas do tabuleiro para revelá-las e tentar encontrar os pares corretos. Sua principal função será memorizar as posições das cartas e realizar as combinações certas até completar o jogo.

## Obstáculos, inimigos ou desafios

Descrição:

> Os principais desafios serão lembrar a posição das cartas já reveladas e evitar erros nas combinações, conseguir achar todos os pares dentro do limite de tempo e passar de nível onde a dificuldade aumenta a cada fase.

## Itens, alvos ou objetos de interação

Descrição:

> Os principais elementos de interação serão as cartas do tabuleiro, que ficarão viradas para baixo até serem clicadas. Cada carta terá uma imagem ou símbolo, e o objetivo será encontrar seus pares. O jogo também contará com tela inicial, botão de reiniciar, mensagem de vitória, níveis de dificuldade, tentativas, temporizador e ranking por tempo.

## Pontuação, vidas, tempo ou progresso


Descrição:

> O jogo acompanhará o progresso por meio do contador de tentativas, um temporazidor e se o jogador passou de nível. Além de um ranking para definir quem fez o melhor tempo.

## 10. Controles previstos

Informe os comandos que serão utilizados pelo jogador.

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
docs/: Diretório para a documentação do projeto, incluindo README.md e proposta.md.



Organização planejada:

main.py: Ponto de entrada principal da aplicação, responsável por iniciar o jogo. 
config.py: Arquivo dedicado a armazenar as configurações globais do jogo, como dimensões da tela, paleta de cores, taxa de quadros por segundo (FPS) e título do jogo.


## 12. Recursos externos previstos

Informe se o grupo pretende utilizar imagens, sons, fontes, tutoriais ou códigos externos.

Exemplo:

- imagens obtidas de banco gratuito;
- sons gratuitos;
- tutorial usado apenas como referência;
- fonte personalizada.

Recursos previstos:

> Utilização de imagens gratuitas.

Caso não pretenda utilizar recursos externos, escreva:

> 

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

Escopo mínimo:

> A versão mínima do jogo terá cartas embaralhadas em tabuleiro, um controle por clique de mouse para virar as cartas, dificuldade por níveis, tentativas, temporizador e mensagem de vitória.

## 15. Possíveis melhorias, caso haja tempo

Melhorias possíveis:

- Melhoria 1: adicionar sons e efeitos visuais ao virar as cartas e ao concluir a
partida.
- Melhoria 2:  criar níveis de dificuldade diferentes, aumentando a quantidade de
cartas no tabuleiro.
- Melhoria 3: implementar uma tela inicial e um ranking com os melhores resultados,
baseado no menor número de tentativas ou no menor tempo.
- Melhoria 4: Permitir que tenha 2 jogadores
