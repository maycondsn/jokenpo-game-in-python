import random

import colors

variables = ["rock", "paper", "scissors", "lizard", "spock"]
score = [0, 0]

rule = {
    'rock': (['crushes', 'lizard'], ['crushes', 'scissors']),
    'paper': (['disproves', 'spock'], ['covers', 'rock']),
    'scissors': (['cuts', 'paper'],['decapites', 'lizard']),
    'lizard': (['poisons', 'spock'], ['eats', 'paper']),
    'spock': (['smashes', 'scissors'], ['vaporizes', 'rock'])
}

def Win(player1, player2, index):
    print(f'\n{player1} {rule[player1][index][0]} {player2}')
    print(f"{colors.green}You Win! :){colors.reset}\n")

def Lose(player1, player2):
    for i in range(2):
        print(f'\n{player2} {rule[player2][i][0]} {player1}') if(rule[player2][i][1] == player1) else ""
    print(f"{colors.red}You lose! :({colors.reset}\n")

def Running(player1, player2, score):
    x, index = 0, -1
    for i in range(2):
        if (rule[player1][i][1] == player2):
            x = 1
            index = i
    if(x == 1):
        Win(player1, player2, index)
        score[0] += 1
    else:
        Lose(player1, player2)
        score[1] += 1
    
def Bot():
    return variables[random.randint(1, 5)-1]

def Game():
    print('1 - rock\n2 - paper\n3 - scissors\n4 - lizard\n5 - spock\n')
    
    while True:
        try:
            print(f'{colors.blue}player: {score[0]}{colors.reset}   |   {colors.orange}bot: {score[1]}{colors.reset}\n')
            x = int(input("enter a value: ")) 
            variable = variables[x-1]
            bot = Bot()
            print(f'You: {variable}') 
            print(f'Bot: {bot}')
            print(f'\n{colors.yellow}DRAW!{colors.reset}\n') if variable == bot else Running(variable, bot, score)
            
        except:
            print('INVALID VALUE!')

Game()