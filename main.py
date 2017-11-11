import itertools

class Game:
    def __init__(self):
        self.board = {i : ' ' for i in range(1, 10)}
        self.player = None
        self.AI = None
        self.characters = ['X', 'O']

    def start(self):
        print("Choose a number between 1 and 9 to place your character on the board; left to right, top down. \n")
        print(self.example_grid())
        self.choose_character()

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

    def get_player(self):
        return self.player

    def get_AI(self):
        return self.AI

Game = Game()
Game.start()
