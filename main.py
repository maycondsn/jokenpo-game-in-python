import colors
from game import Game
from bot import Bot

Game = Game(1)

while True:
        try:
            scoreboard = f'\n{colors.blue}player: {Game.score[0]}{colors.reset}   |   {colors.orange}bot: {Game.score[1]}{colors.reset}\n'
            print(scoreboard)
            print('1 - rock |   2 - paper   |   3 - scissors    |   4 - lizard  |   5 - spock   |   6 - leave\n')
            x = int(input("enter a value: ")) 
            
            if(x == 6):
                print(scoreboard)
                break
            
            variable = Game.variables[x-1]
            bot = Bot(Game.variables)
            print(f'You: {variable}') 
            print(f'Bot: {bot}')
            print(f'\n{colors.yellow}DRAW!{colors.reset}\n') if variable == bot else Game.running(variable, bot, Game.score)
            
        except:
            print('INVALID VALUE!')
            