variables = ["rock", "paper", "scissors", "lizard", "spock"]

'''
Regras:
spock amassa tesoura
tesoura corta papel
papel cobre pedra
pedra amassa lagarto
lagarto envenena spock

spock vaporiza pedra
pedra destroi tesoura
tesoura decapita lagarto
lagarto come papel
papel disaprova spock
'''

def Win():
    print("You Win! :)")

def Lose():
    print("You lose! :(")

'''
Etapas:
()criar uma lógica capaz de simplificar o jogo
()comecar tentando com pedra papel tesoura
()A tela de comando inicialmente rodará loop infinito mostrando os valores para cada opção do presente no jogo
()o usuário deverá digitar o número correspondente para cada opção
()número será de acordo com o valor da opção na tabela
()usar tuplas para definir as regras onde o primeiro valor da tupla será o vencedor
()inicialmente o jogo será solo com uma função aleatória 
()o código deve ser capaz de procurar a tupla correspondente que possua os dois valores de entrada
()ao encontrar a tupla correspondente, o código deverá retornar quem foi o vencedor da disputa
'''
