import colors

class Game:
    def __init__(self, id):
        self.variables = ['rock', 'paper', 'scissors', 'lizard', 'spock']
        self.rule = {
                    'rock': (['crushes', 'lizard'], ['crushes', 'scissors']),
                    'paper': (['disproves', 'spock'], ['covers', 'rock']),
                    'scissors': (['cuts', 'paper'], ['decapites', 'lizard']),
                    'lizard': (['poisons', 'spock'], ['eats', 'paper']),
                    'spock': (['smashes', 'scissors'], ['vaporizes', 'rock'])
                    }
        self.ready = False
        self.id = id
        self.score = [0, 0]
    
    def connected(self):
        return self.ready
    
    def win(self, player1, player2, index):
        return f'\n{player1} {self.rule[player1][index][0]} {player2}\n{colors.green}You Win! :){colors.reset}'
    
    def lose(self, player1, player2):
        winner = ''
        for i in range(2):
            winner = f'\n{player2} {self.rule[player2][i][0]} {player1}' if(self.rule[player2][i][1] == player1) else ""
        return(f'{winner}\n{colors.red}You lose! :({colors.reset}')
    
    def running(self, player1, player2, score):
        win_player1, index = False, -1
        for i in range(2):
            if(self.rule[player1][i][1] == player2):
                win_player1 = True
                index = i
        if(win_player1):
            print(self.win(player1, player2, index))
            score[0] += 1
            
        
        else:
            print(self.lose(player1, player2))
            score[1] += 1
