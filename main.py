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
        self.count_down = 9 # Number of places
        self.combinations = [[1, 2, 3], [4, 5, 6], [7, 8, 9], [1, 4, 7], [2, 5, 8], [3, 6, 9], [1, 5, 9], [3, 5, 7]]
        self.ai_memory = self.combinations
        self.player_memory = []

    def start(self):
        print("Choose a number between 1 and 9 to place your character on the board; left to right, top down. \n")
        print(self.example_grid())
        self.choose_character()
        self.play()

    ## Creates the grid with the character placements
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

    ## Creates the example grid to show which numbers allocates your character
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

    ## Player chooses whether they want to use X or O
    def choose_character(self):
        char = None
        while True:
            char = input("Choose a character (X or O): ").upper()
            if char in self.characters:
                self.player = char
                for c in self.characters:
                    if self.player != c:
                        self.AI = c
                break

    ## Play the game
    def play(self):
        # Keep playing while the game is not complete
        while not self.complete:
            try:
                # User input
                choice = int(input("Your turn: "))
                # Place palyer's character in position if it is free
                if self.board[choice] is ' ':
                    self.board[choice] = self.player
                    # Count down the number of free places
                    self.count_down -= 1
                    # Check to see if the player has won the game
                    if self.check_winner(self.player):
                        print(self.create_grid())
                        print("Player has won the game\n")
                        break
                    # AI's turn
                    self.ai_player()
                    # Check to see if the AI has won the game
                    if self.check_winner(self.AI):
                        print(self.create_grid())
                        print("AI has won the game")
                        break
                    # Display the grid after both players have had their turn to show the new placements
                    print(self.create_grid())
                else:
                    print("Position already taken. \n")
            except KeyboardInterrupt:
                print("Exiting game")
                sys.exit()
            except:
                if not self.complete:
                    print("Please choose a number between 1 and 9")

    # AI player. Keeps track of which positions the player has taken and which positions it has taken
    # then tries to find the best possible position to take in order to win the game.
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
                    self.count_down -= 1
                    found = True

    # Tries to find the best placement for the AI by finding current combinations that either have one or more characters
    # or tries to play defensively by checking if the player is about to win and preventing the player from winning.
    def find_best_placement(self, ai_coords):
        player_about_to_win = self.is_about_to_win(self.player, self.player_memory)
        if player_about_to_win and not self.is_about_to_win(self.AI, self.ai_memory):
            for i in player_about_to_win:
                if self.board[i] is ' ':
                    self.board[i] = self.AI
                    self.count_down -= 1
                    return True
        else:
            for ai in ai_coords:
                for m in self.ai_memory:
                    if ai in m:
                        for i in m:
                            if self.AI is not self.board[i]:
                                self.board[i] = self.AI
                                self.count_down -= 1
                                return True
        return False

    ## Checks to see if the player (including AI) is about to win the match
    def is_about_to_win(self, player, coords):
        for c in coords:
            count = 0
            for i in c:
                if player is self.board[i]:
                    count += 1
            if count == 2:
                return c
        return False

    ## Checks to see if the current player (including AI) has won the game
    def check_winner(self, player):
        # If there are still placements available then check for winners
        if (self.count_down > 0):
            # Loop throuch all posible winning combinations and check if the player has those combinations
            for possible in self.combinations:
                # Number of positions that user has in a winning combination
                p = 0
                for i in possible:
                    # if the current character in the current position belongs to the current player then iterate by 1
                    if self.board[i] == player:
                        p += 1
                # If there are 3 characters in a winning combination that belongs to the player then the player has won
                if p == 3:
                    return True
            return False
        else: # If no placements are left then it is a draw
            self.complete = True
            print(self.create_grid())
            print("It's a draw!\n")
            sys.exit()

Game = Game()
Game.start()
