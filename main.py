import itertools
from random import randint
import sys

class Game:
    def __init__(self):
        self.board = {i : ' ' for i in range(1, 10)}
        self.player = None
        self.AI = None
        self.characters = ['X', 'O']
        self.complete = False
        self.combinations = [[1, 2, 3], [4, 5, 6], [7, 8, 9], [1, 4, 7], [2, 5, 8], [3, 6, 9], [1, 5, 9], [3, 5, 7]]
        self.ai_memory = self.combinations
        self.player_memory = []

    def start(self):
        print("Choose a number between 1 and 9 to place your character on the board; left to right, top down. \n")
        print(self.example_grid())
        self.choose_character()
        self.play()

    def create_grid(self):
        count = 1
        grid = ''
        for y in range(5):
            if (y == 0 or y % 2 == 0):
                grid += "|".join([s.format(self.board[i]) for i, s in enumerate(list(itertools.repeat(" {} ", 3)), count)])
                count += 3
            else:
                grid += "---+---+---"
            grid += '\n'
        return grid

    def example_grid(self):
        count = 1
        grid = ''
        for y in range(5):
            if (y == 0 or y % 2 == 0):
                grid += "|".join([s.format(i) for i, s in enumerate(list(itertools.repeat(" {} ", 3)), count)])
                count += 3
            else:
                grid += "---+---+---"
            grid += '\n'
        return grid

    def choose_character(self):
        char = None
        while True:
            char = input("Choose a character (X or O): ")
            if char.upper() in self.characters:
                self.player = char
                for c in self.characters:
                    if self.player != c:
                        self.AI = c
                break

    def play(self):
        while not self.complete:
            try:
                choice = int(input("Your turn: "))
                if self.board[choice] is ' ':
                    self.board[choice] = self.player
                    if self.check_winner(self.player):
                        print(self.create_grid())
                        print("Player has won the game\n")
                        break
                    self.ai_player()
                    if self.check_winner(self.AI):
                        print(self.create_grid())
                        print("AI has won the game")
                        break
                    print(self.create_grid())
                else:
                    print("Position already taken. \n")
            except KeyboardInterrupt:
                print("Exiting game")
                sys.exit()
            except:
                print("Please choose a number between 1 and 9")


    def ai_player(self):
        player_coords = [key for key, value in self.board.items() if value is self.player]
        ai_coords = [key for key, value in self.board.items() if value is self.AI]

        for i in player_coords:
            self.ai_memory = [x for x in self.ai_memory if i not in x]
            self.player_memory = [x for x in self.combinations if i in x]

        if not self.find_best_placement(ai_coords):
            found = False
            while not found:
                ran = randint(1, 9)
                if ' ' in self.board[ran]:
                    self.board[ran] = self.AI
                    found = True

    def find_best_placement(self, ai_coords):
        player_about_to_win = self.is_about_to_win(self.player, self.player_memory)
        if player_about_to_win and not self.is_about_to_win(self.AI, self.ai_memory):
            for i in player_about_to_win:
                if self.board[i] is ' ':
                    self.board[i] = self.AI
                    return True
        else:
            for ai in ai_coords:
                for m in self.ai_memory:
                    if ai in m:
                        for i in m:
                            if self.AI is not self.board[i]:
                                self.board[i] = self.AI
                                return True
        return False

    def is_about_to_win(self, player, coords):
        for c in coords:
            count = 0
            for i in c:
                if player is self.board[i]:
                    count += 1
            if count == 2:
                return c
        return False

    def check_winner(self, player):
        for possible in self.combinations:
            p = 0
            for i in possible:
                if self.board[i] == player:
                    p += 1
            if p == 3:
                return True
        return False

Game = Game()
Game.start()
