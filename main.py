class Game:
    def __init__(self):
        self.board = {i : None for i in range(0, 9)}
        self.player = None
        self.AI = None
        self.characters = ['X', 'O']

    def create_grid(self):
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
#
# board =
#
# print("Choose a number between 1 and 9 to place your character on the board")
# print(example_board)
#
# character = input("Which character do you want? X or O ")
# print ("You have chosen {}".format(character))
# keep_playing = True
#
# while keep_playing:
