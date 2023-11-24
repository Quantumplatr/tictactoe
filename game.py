from colorama import Fore, Back, Style


class Game:
    def __init__(self, *args, **kwargs):
        """Initializes the game."""
        
        if len(args) == 0:
            self.reset()
        elif len(args) == 1:
            self.reset()
            if args[0] in [1,2]:
                self.turn = args[0]
        else:
            raise TypeError("Too many arguments")
    

        
    def reset(self):
        """Resets the game."""
        
        self.turn = 1  # 1 = X, 2 = O
        self.board = [0, 0, 0, 0, 0, 0, 0, 0, 0]  # 0 = empty, 1 = X, 2 = O
        self.winner = None
        self.win_positions = None
        self.win_direction = None

    def play(self, pos: int) -> bool:
        """Plays a move at the given position.

        Args:
            pos (int): The position to play at. 0-8, left to right, top to bottom.

        Returns:
            bool: True if the move was played, False if the move was invalid.
        """
        # Game over
        if self.winner is not None:
            return False

        # Invalid position
        if pos < 0 or pos > 8:
            return False

        # All positions taken
        if all(self.board):
            return False

        # Valid move
        if self.board[pos] == 0:
            self.board[pos] = self.turn
            self.turn = 1 if self.turn == 2 else 2
            self.check_winner()
            return True
        # Position already taken
        else:
            return False

    def check_winner(self):
        # Check rows
        for i in range(0, 9, 3):
            if self.board[i] == self.board[i + 1] == self.board[i + 2] != 0:
                self.winner = self.board[i]
                self.win_positions = [i, i + 1, i + 2]
                self.win_direction = "-"
                return

        # Check columns
        for i in range(3):
            if self.board[i] == self.board[i + 3] == self.board[i + 6] != 0:
                self.winner = self.board[i]
                self.win_positions = [i, i + 3, i + 6]
                self.win_direction = "|"
                return

        # Check diagonals
        if self.board[0] == self.board[4] == self.board[8] != 0:
            self.winner = self.board[0]
            self.win_positions = [0, 4, 8]
            self.win_direction = "\\"
            return
        if self.board[2] == self.board[4] == self.board[6] != 0:
            self.winner = self.board[2]
            self.win_positions = [2, 4, 6]
            self.win_direction = "/"
            return

        # Check draw
        if all(self.board):
            self.winner = 0
            return

    def print(self):
        """Prints the board."""

        text = Style.BRIGHT + " "

        for i in range(9):
            
            # Print winning positions
            if self.win_positions is not None and i in self.win_positions:
                text += (Fore.RED if self.winner == 1 else Fore.BLUE) + self.win_direction + Style.RESET_ALL + Style.BRIGHT
                
            # Print usual positions
            else:
                
                if self.board[i] == 0:
                    text += Style.DIM + str(i+1) + Style.RESET_ALL + Style.BRIGHT
                elif self.board[i] == 1:
                    text += Fore.RED + "X" + Fore.WHITE
                elif self.board[i] == 2:
                    text += Fore.BLUE + "O" + Fore.WHITE

            if i % 3 != 2:
                text += " | "

            if i % 3 == 2 and i != 8:
                text += Style.RESET_ALL + Style.BRIGHT + "\n" + "-----------\n "

        text += Style.RESET_ALL + "\n"
        print(text)
