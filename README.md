#Match Up 

Projeto final da disciplina de Introdução a Algoritmos/Programação, desenvolvido com Python e Pygame.

Este repositório é um template para os grupos da disciplina. A proposta é começar com uma base funcional e evoluir o jogo ao longo do semestre.

## Integrantes do grupo

Nome 1: Gabriel de Souza Junqueira Hermont 
Nome 2: Kemily Eduardo da Luz 
Nome 3: Maria Clara Soalheiro Bessa 
Nome 4: Armando Schoenstatt Rodrigues e Moreira 

Tipo de jogo: Jogo de Memória 

## Estrutura do projeto

- `main.py`: ponto de entrada da aplicação.
- `config.py`: guardará as configurações principais, como tamanho da tela, cores e FPS, título do jogo.
- `jogo.py`: Contém o loop principal da partida e gerencia as regras ativas, mecânica de cliques, verificação de igualdade das cartas e avanço automático de fases.
- `funcoes.py`: Responsável pelas telas de interface gráfica, como o menu de início em formato de card (para captura do nome do jogador), a tela gráfica do ranking geral e funções utilitárias de desenho de botões e textos.
- `src/`: código-fonte principal do jogo (loop, regras, sprites e dados).
- `dados.py`: É responsável por carregar e salvar recordes locais, salvar nomes e tempos no ranking, inicializar a matriz do tabuleiro e carregar/redimensionar os recursos visuais das cartas.
- `assets/`: imagens.
- `data/`: arquivos persistentes (recorde/ranking).
- `tests/`: testes unitários com `pytest`.
- `docs/`: documentação do projeto, incluindo proposta inicial.

## Descrição do jogo

No jogo Match Up, os jogadores enfrentam um tabuleiro com diversas cartas viradas para baixo, a temática do jogo é a série Off-Campus. A interface exibe o nível atual, o tempo decorrido, o recorde local e o nome do jogador, além de um contador de tentativas e um botão gráfico para reiniciar a partida. O jogador interage exclusivamente por meio do mouse, clicando nas cartas para revelá-las. O principal objetivo é encontrar todos os pares correspondentes, exigindo memorização rápida das imagens. O desafio aumenta progressivamente a cada nível, alterando o tamanho do tabuleiro e a quantidade de cartas.


## Objetivo do jogador

Objetivo do jogador: Encontrar todos os pares de cartas no menor número de tentativas possível. 

## Regras do jogo

Regra 1: O jogador pode virar apenas duas cartas por vez.
Regra 2: Se as duas cartas selecionadas forem idênticas, elas permanecem visíveis e são contabilizadas como um par encontrado.
Regra 3: Caso as cartas escolhidas sejam diferentes, elas serão exibidas por um breve período e, em seguida, voltarão a ficar viradas para baixo.
Regra 4: O jogo prossegue para a próxima fase até que todos os pares no tabuleiro sejam encontrados.
Regra 5: O número total de tentativas e o tempo são registrados e exibidos ao longo de toda a partida. 

## Controles

- Clique do mouse: Utilizado para selecionar e virar as cartas no tabuleiro.
- ESC / ENTER: Atalhos de teclado para sair do jogo ou confirmar ações rápidas de transição nas telas de interface.
- Botão fechar janela (X): Encerra o jogo.
