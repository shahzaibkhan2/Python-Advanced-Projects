# Import random module
import random

# Define a class for player
class Player:
    def __init__(self, name):
        self.name = name
        self.score = 0

    # Define a function to add point
    def add_point(self):
        self.score += 1

# Define a child class of human player from player class
class HumanPlayer(Player):
    def __init__(self, name):
        super().__init__(name)

    # Define a function to get a move
    def get_move(self):
        valid_moves = ['rock', 'paper', 'scissors']
        while True:
            move = input('Choose your move (rock/paper/scissors): ').lower()
            if move in valid_moves:
                return move
            print('Invalid move, please try again.')

# Define a child class for computer player from player class
class ComputerPlayer(Player):
    def __init__(self):
        super().__init__('Computer')

    # Define a function to get a move for computer player
    def get_move(self):
        return random.choice(['rock', 'paper', 'scissors'])

# Define a class for game
class Game:
    def __init__(self):
        self.human_player = HumanPlayer(input('Enter your name: '))
        self.computer_player = ComputerPlayer()
        self.winners = []

    # Define a function to play game
    def play(self):
        print('Welcome to the rock, paper, scissors game!')
        while True:
            human_move = self.human_player.get_move()
            computer_move = self.computer_player.get_move()
            print(f'{self.human_player.name} chose {human_move}, {self.computer_player.name} chose {computer_move}.')
            if human_move == computer_move:
                print('Tie!')
            elif (human_move == 'rock' and computer_move == 'scissors') or \
                 (human_move == 'paper' and computer_move == 'rock') or \
                 (human_move == 'scissors' and computer_move == 'paper'):
                print(f'{self.human_player.name} wins!')
                self.human_player.add_point()
                self.winners.append(self.human_player)
            else:
                print(f'{self.computer_player.name} wins!')
                self.computer_player.add_point()
                self.winners.append(self.computer_player)

            print(f'{self.human_player.name}: {self.human_player.score}  {self.computer_player.name}: {self.computer_player.score}')

            if self.human_player.score == 3 or self.computer_player.score == 3:
                break

        if self.human_player.score == 3:
            print(f'{self.human_player.name} wins the game!')
        else:
            print(f'{self.computer_player.name} wins the game!')

        print('Previous winners:')
        for winner in self.winners:
            print(winner.name)

game = Game()
game.play()
