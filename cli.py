from game import Game
from colorama import Fore, Style


def play_pvp(starting_player):
    game = Game(starting_player)
    while game.winner is None:
        print()
        game.print()
        turn = ["X", "O"][game.turn - 1]
        pos = int(
            input(
                f"Enter {Fore.RED if turn == 'X' else Fore.BLUE}{turn}{Style.RESET_ALL} position (1-9): "
            )
        )
        success = game.play(pos - 1)
        while not success:
            print("Invalid move!")
            pos = int(input("Enter position (1-9): "))
            success = game.play(pos - 1)
    print()
    game.print()
    return game.winner


def play_ai(starting_player, ai_player, difficulty):
    game = Game(starting_player)

    # TODO: implement AI
    print("AI not implemented yet!")
    exit()


def main():
    scores = [0, 0, 0]

    game_type = None
    player = 1  # 1 = X, 2 = O
    first_to_wins = 1  # Number of wins to finish the game

    # AI variables
    ai_player = None
    difficulty = None

    # Get game type
    inp = input("Play against AI? (y/n): ")
    while inp not in ["y", "n"]:
        inp = input("Play against AI? (y/n): ")

    # Handle AI game
    if inp == "y":
        # Get player's choice for x/o
        inp = input("Play as X or O? (x/o): ")

        while inp not in ["x", "o"]:
            inp = input("Play as X or O? (x/o): ")

        ai_player = 1 if inp == "o" else 2

        # Get player's choice for difficulty
        inp = input("Choose difficulty (easy/medium/hard): ")

        while inp not in ["easy", "medium", "hard"]:
            inp = input("Choose difficulty (easy/medium/hard): ")

        difficulty = inp

        # TODO: Implement AI
        pass
    
    # Handle PvP game
    else:
        game_type = "pvp"
        
    # Get number of wins to finish the game
    inp = input("How many wins to finish the game?: ")
    
    while not inp.isnumeric():
        inp = input("How many wins to finish the game?: ")
        
    first_to_wins = int(inp)
        

    # Play game
    while scores[1] < first_to_wins and scores[2] < first_to_wins:
        result = (
            play_pvp(player)
            if game_type == "pvp"
            else play_ai(player, ai_player, difficulty)
        )
        scores[result] += 1
        player = 1 if player == 2 else 2
        print("Winner:", ["Draw", "X", "O"][result])
        print(
            f"{Fore.RED}X{Style.RESET_ALL} wins:{Fore.RED}",
            scores[1],
            "/",
            first_to_wins,
            Style.RESET_ALL,
        )
        print(
            f"{Fore.BLUE}O{Style.RESET_ALL} wins:{Fore.BLUE}",
            scores[2],
            "/",
            first_to_wins,
            Style.RESET_ALL,
        )
        print("Draws:", scores[0], "")

    # Print winner
    winner = 1 if scores[1] > scores[2] else 2
    print()
    print(
        f"{Style.BRIGHT}{Fore.RED if winner == 1 else Fore.BLUE}{'X' if winner == 1 else 'O'} wins {scores[1] if winner == 1 else scores[2]}-{scores[2] if winner == 1 else scores[1]}{Style.RESET_ALL}"
    )

if __name__ == "__main__":
    main()
