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

> No jogo Match Up, os jogadores enfrentam um tabuleiro com diversas cartas viradas para baixo, a temática do jogo é a série Off-Campus. A interface exibe o nível atual, o tempo decorrido, o recorde local e o nome do jogador, além de um contador de tentativas e um botão gráfico para reiniciar a partida. O jogador interage exclusivamente por meio do mouse, clicando nas cartas para revelá-las. O principal objetivo é encontrar todos os pares correspondentes, exigindo memorização rápida das imagens. O desafio aumenta progressivamente a cada nível, alterando o tamanho do tabuleiro e a quantidade de cartas.

## 5. Objetivo do jogador

Encontrar todos os pares de cartas no menor número de tentativas possível e avançar de nível.

## 6. Regras principais

Regra 1: O jogador pode virar apenas duas cartas por vez.
Regra 2: Se as duas cartas selecionadas forem idênticas, elas permanecem visíveis e são contabilizadas como um par encontrado.
Regra 3: Caso as cartas escolhidas sejam diferentes, elas serão exibidas por um breve período e, em seguida, voltarão a ficar viradas para baixo.
Regra 4: O jogo prossegue para a próxima fase até que todos os pares no tabuleiro sejam encontrados.
Regra 5: O número total de tentativas e o tempo são registrados e exibidos ao longo de toda a partida.

## 7. Condição de vitória

> O jogador vence o jogo ao concluir com sucesso o terceiro e último nível do tabuleiro, encontrando todos os pares de cartas e registrando seu tempo final.

## 8. Condição de derrota ou encerramento

A partida é encerrada quando o jogador conclui o nível máximo abrindo automaticamente a tela de classificação com o ranking atualizado, ou quando o usuário decide fechar a janela do jogo através do botão (X) ou da tecla ESC.

## 9. Elementos previstos no jogo

As Cartas: O elemento central do tabuleiro. Elas mudam de quantidade e de imagem a cada nível e possuem um verso padrão.
O Temporizador (Tempo): Um cronômetro ativo que conta os segundos na tela para pressionar o jogador a terminar o nível o mais rápido possível.
O Contador de Tentativas: Registra quantas vezes o jogador tentou virar um par de cartas, ajudando a medir a eficiência da memória dele.
O Recorde: Mostra no topo da tela o melhor tempo já registrado, servindo de alvo para o jogador superar.
O Botão Reiniciar: Um botão interativo na tela que permite ao jogador resetar a fase atual a qualquer momento se ele se perder.
A Caixa de Entrada de Texto (Input): O campo na tela inicial onde o jogador digita o seu nome antes de a partida começar.
O Ranking: A tabela final que lê o arquivo de texto e lista de forma ordenada os melhores tempos junto com os nomes dos jogadores.

## Jogador ou elemento principal

> O jogador irá interagir com o jogo por meio do mouse, clicando nas cartas do tabuleiro para revelá-las e tentar encontrar os pares corretos. Sua principal função será memorizar as posições das cartas e realizar as combinações certas até completar o jogo.

## Obstáculos, inimigos ou desafios

> Os principais desafios serão lembrar a posição das cartas já reveladas e evitar erros nas combinações, conseguir achar todos os pares dentro do limite de tempo e passar de nível onde a dificuldade aumenta a cada fase.

## Itens, alvos ou objetos de interação

> Os principais elementos de interação serão as cartas do tabuleiro, que ficarão viradas para baixo até serem clicadas. Cada carta terá uma imagem ou símbolo, e o objetivo será encontrar seus pares. O jogo também contará com tela inicial, botão de reiniciar, mensagem de vitória, níveis de dificuldade, tentativas, temporizador e ranking por tempo.

## Pontuação, vidas, tempo ou progresso

> O jogo acompanhará o progresso por meio do contador de tentativas, um temporazidor e se o jogador passou de nível. Além de um ranking para definir quem fez o melhor tempo.

## 10. Controles previstos

- Clique do mouse: Utilizado para selecionar e virar as cartas no tabuleiro.
- ESC / ENTER: Atalhos de teclado para sair do jogo ou confirmar ações rápidas de transição nas telas de interface.
- Botão fechar janela (X): Encerra o jogo.


## 11. Organização inicial do código

main.py: Ponto de entrada principal da aplicação, responsável por iniciar o jogo. 
config.py: Arquivo dedicado a armazenar as configurações globais do jogo, como dimensões da tela, paleta de cores, taxa de quadros por segundo (FPS) e título do jogo.
jogo.py: Contém o loop principal e gerencia as regras do jogo, como os cliques, a detecção de pares, o fluxo de avanço automático de fases, informações na tela e telas de vitória.
funcoes.py: Módulo responsável pelas telas de interface gráfica, como o menu de início em formato de card (para captura do nome do jogador), a tela gráfica do ranking geral e funções utilitárias de desenho de botões e textos.
dados.py: É responsável por carregar e salvar recordes locais, salvar nomes e tempos no ranking, inicializar a matriz do tabuleiro e carregar/redimensionar os recursos visuais das cartas.
data/: Diretório para arquivos persistentes, como o registro de recordes ou rankings de jogadores.
assets/: Diretório contendo os recursos de imagens organizados por categorias de fases.
tests/: Diretório para os testes unitários do projeto, utilizando a ferramenta pytest.
docs/: Diretório para a documentação do projeto, incluindo README.md e proposta.md.

## 12. Recursos externos previstos

Imagens temáticas inspiradas nos personagens e casais da série de livros Off-Campus, coletadas na plataforma Pinterest

Fontes nativas do sistema (Arial) gerenciadas pelo Pygame;

Arquivos .txt locais para persistência do ranking.

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

> A versão mínima do jogo terá cartas embaralhadas em um tabuleiro, um controle por clique de mouse para virar as cartas, dificuldade por níveis, tentativas, temporizador e mensagem de vitória.

## 15. Possíveis melhorias, caso haja tempo

Melhorias possíveis:

- Melhoria 1: adicionar sons e efeitos visuais ao virar as cartas e ao concluir a
partida.
- Melhoria 2:  criar níveis de dificuldade diferentes, aumentando a quantidade de
cartas no tabuleiro.
- Melhoria 3: implementar uma tela inicial e um ranking com os melhores resultados,
baseado no menor número de tentativas ou no menor tempo.
- Melhoria 4: Permitir que tenha 2 jogadores
