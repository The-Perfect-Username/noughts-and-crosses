import itertools
from random import randint

class Game:
    def __init__(self):
        self.board = {i : ' ' for i in range(1, 10)}
        self.player = None
        self.AI = None
        self.characters = ['X', 'O']
        self.complete = False
        self.combinations = [[1, 2, 3], [4, 5, 6], [7, 8, 9], [1, 4, 7], [2, 5, 6], [3, 6, 9], [1, 5, 9], [3, 5, 7]]
        self.ai_memory = self.combinations

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
            choice = int(input("Your turn: "))
            self.board[choice] = self.player
            self.ai_player()
            print(self.board)
            print(self.create_grid())

    def ai_player(self):
        player_coords = [key for key, value in self.board.items() if value is self.player]
        ai_coords = [key for key, value in self.board.items() if value is self.AI]

        for i in player_coords:
            self.ai_memory = [x for x in self.ai_memory if i not in x]

        if not self.find_best_placement(ai_coords):
            found = False
            while not found:
                ran = randint(1, 9)
                if ' ' in self.board[ran]:
                    self.board[ran] = self.AI
                    found = True

    def find_best_placement(self, ai_coords):
        for ai in ai_coords:
            for m in self.ai_memory:
                if ai in m:
                    for i in m:
                        if self.AI is not self.board[i]:
                            self.board[i] = self.AI
                            print(i)
                            return True
        return False


Game = Game()
Game.start()
