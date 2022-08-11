import random

variables = ["rock", "paper", "scissor", "lizard", "spock"]

'''
Regras:
spock amassa tesoura    (spock(1)scissor(0))
spock vaporiza pedra    (spock(1)rock(0))

lagarto envenena spock  (lizard(1)spock(0))
lagarto come papel      (lizard(1)paper(0))

papel disaprova spock   (paper(1)spock(0))
papel cobre pedra       (paper(1)rock(0))

pedra amassa lagarto    (rock(1)lizard(0))
pedra destroi tesoura   (rock(1)scissor(0))

tesoura corta papel     (scissor(1)paper(0))
tesoura decapita lagarto(scissor(1)lizard(0))
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

rock = ('lizard', 'scissor')
paper = ('spock', 'rock')
spock = ('scissors', 'rock')
scissor = ('paper','lizard')
lizard = ('spock', 'paper')

def Bot():
    
    return variables[random.randint(1, 5)-1]

def Game():
    print('1 - rock\n2 - paper\n3 - scissor\n4 - lizard\n5 - spock\n')
    
    while True:
        try:
            x = int(input("enter a value: ")) 
            variable1 = variables[x-1]      
            print(f'You: {variable1}') 
            print(f'Bot: {Bot()}')
            
        except:
            print('Invalid value')
Game()
