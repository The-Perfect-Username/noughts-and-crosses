class Game:
    def __init__(self):
        self.board = {i : None for i in range(1, 10)}
        # self.sample = {}
        self.coordinates = [
                            {'x': 0, 'y': 0},
                            {'x': 0, 'y': 7},
                            {'x': 0, 'y': 12},
                            {'x': 2, 'y': 2},
                            {'x': 2, 'y': 7},
                            {'x': 2, 'y': 12},
                            {'x': 4, 'y': 2},
                            {'x': 4, 'y': 7},
                            {'x': 4, 'y': 12}
                            ]
        self.player = None
        self.AI = None
        self.characters = ['X', 'O']

    def start(self):
        print("Choose a number between 1 and 9 to place your character on the board; left to right, top down. \n")
        print(self.create_grid())
        self.choose_character()

    def create_grid(self):
        print(self.board)
        grid = ''
        for x in range(5):
            for y in range(14):
                if (x % 2 == 1) or (x == 1):
                    if (y == 4 or y == 9):
                        grid += '|'
                    else:
                        grid += '-'
                else:
                    if (y == 4 or y == 9):
                        grid += '|'
                    else:
                        grid += ' '

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


# example_board = '''
#      1  | 2  | 3
#     ----|----|----
#      4  | 5  | 6
#     ----|----|----
#      7  | 8  | 9
# '''
#
#
# def board():
#     return '''
#             |    |
#         ----|----|----
#             |    |
#         ----|----|----
#             |    |
#     '''.format()

Game = Game()
Game.start()
