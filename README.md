# Jogo da Vida de John Horton Conway

Uma implementação do Jogo da Vida de John Horton Conway em Python usando a biblioteca Pygame.

<div align="center">
<img src="https://github.com/DaviLDamasceno/Jogo-da-Vida/assets/53913486/f2f803f4-bf6c-4143-bd55-414ce61399ae" width="300px"/>
</div>div>

## Descrição

O Jogo da Vida é um autômato celular desenvolvido pelo matemático britânico John Horton Conway em 1970. O jogo ocorre em uma grade bidimensional infinita, onde cada célula pode estar viva representada por um quadrado branco ou morta representada por um quadrado azul claro. A evolução das células ocorre de acordo com regras simples:

- Toda célula morta com exatamente três vizinhos vivos torna-se viva (nascimento).
- Toda célula viva com menos de dois vizinhos vivos morre por isolamento.
- Toda célula viva com mais de três vizinhos vivos morre por superpopulação.
- Toda célula viva com dois ou três vizinhos vivos permanece viva.

O jogo começa com uma configuração inicial de células vivas e evolui em cada iteração de acordo com essas regras.

## Funcionalidades

- Interface gráfica interativa usando Pygame.
- Configuração inicial aleatória das células vivas.
- Grade visualizada com retângulos brancos para células vivas e retângulos pretos para células mortas.
- Linhas entre as colunas e linhas da grade para melhor visualização.

## Requisitos

- Python 3.x
- Pygame

## Como executar

1. Certifique-se de ter o Python 3.x instalado. Você pode baixá-lo em https://www.python.org/downloads/.
2. Instale a biblioteca Pygame executando o seguinte comando no terminal: pip install pygame
3. Clone ou faça o download deste repositório.
4. Navegue até o diretório do projeto no terminal.
5. Execute o seguinte comando: python JogoDaVida.py
6. O jogo da vida será iniciado e uma janela com a interface gráfica será exibida.
7. Observe a evolução das células vivas na grade.

## Contribuição

Contribuições são bem-vindas! Se você quiser melhorar este projeto, sinta-se à vontade para enviar um pull request.
