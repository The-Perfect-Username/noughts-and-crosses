import itertools

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
            print(self.create_grid())
            print(self.ai_player())

    def ai_player(self):
        tmp = [key for key, value in self.board.items() if value is self.player]
        for i, j in enumerate(tmp):
            self.ai_memory = [x for x in self.ai_memory if j not in x]


Game = Game()
Game.start()
