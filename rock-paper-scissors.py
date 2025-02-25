import random
import os
import sys

# ANSI color codes for styling
WHITE = "\033[97m"
BLUE = "\033[94m"
ORANGE = "\033[93m"
GREEN = "\033[32m"  # Prettier green color
RESET = "\033[0m"

# Flag to check if "sword" can still be used
sword_available = True

# Header
print(
    """
+--------------------------------+
Welcome to Rock-Paper-Scissors!
+--------------------------------+
"""
)


# Main Code
def determine_winner(player1_action, player2_action, player1_name, player2_name):
    global sword_available

    if player1_action == "sword" and not sword_available:
        print(
            f"{ORANGE}The mighty sword lies broken, {player1_name} must choose another path.{RESET}"
        )
        return 0  # Tie, no points awarded

    if player1_action == player2_action:
        print(f"{WHITE}Both players selected {player1_action}. It's a tie!{RESET}")
        return 0  # Tie
    elif player1_action == "rock":
        if player2_action == "scissors":
            print(f"{BLUE}{player1_name} wins! Rock smashes scissors!{RESET}")
            return 1  # Player 1 wins
        else:
            print(f"{ORANGE}{player2_name} wins! Paper covers rock!{RESET}")
            return -1  # Player 2 wins
    elif player1_action == "paper":
        if player2_action == "rock":
            print(f"{BLUE}{player1_name} wins! Paper covers rock!{RESET}")
            return 1  # Player 1 wins
        else:
            print(f"{ORANGE}{player2_name} wins! Scissors cuts paper!{RESET}")
            return -1  # Player 2 wins
    elif player1_action == "scissors":
        if player2_action == "paper":
            print(f"{BLUE}{player1_name} wins! Scissors cuts paper!{RESET}")
            return 1  # Player 1 wins
        else:
            print(f"{ORANGE}{player2_name} wins! Rock smashes scissors!{RESET}")
            return -1  # Player 2 wins
    elif player1_action == "sword":
        if player2_action == "shield":
            print(
                f"{WHITE}Shield blocks the sword! It's a tie, and sword can no longer be used.{RESET}"
            )
            sword_available = False
            return 0  # Tie
        print(f"{BLUE}Sword always wins! {player1_name} wins!{RESET}")
        return 1  # Player 1 wins
    elif player1_action == "shield":
        if player2_action == "rock":
            print(
                f"{WHITE}The shield meets rock and gets crushed under the weight! {player2_name} wins!{RESET}"
            )
            return -1  # Player 2 wins
        elif player2_action == "paper":
            print(
                f"{WHITE}The shield tries to block paper, but it gets wrapped around it! {player2_name} wins!{RESET}"
            )
            return -1  # Player 2 wins
        elif player2_action == "scissors":
            print(
                f"{WHITE}The shield gets sliced by scissors, it's no match! {player2_name} wins!{RESET}"
            )
            return -1  # Player 2 wins
        elif player2_action == "sword":
            print(f"{WHITE}Shield blocks sword! Sword can no longer be used.{RESET}")
            sword_available = False
            return 0  # Tie


def play_round(player1_name, player2_name, is_single_player=True):
    global sword_available

    if is_single_player:
        user_action = input(
            f"{WHITE}{player1_name}, enter a choice (rock, paper, scissors): {RESET}"
        ).lower()
        possible_actions = ["rock", "paper", "scissors", "sword", "shield"]

        if user_action in ["hello", "hi", "hey"]:
            print(
                f"{GREEN}Please take the game seriously and choose rock, paper, or scissors.{RESET}"
            )
            return 0  # No result if player types a greeting

        if user_action not in possible_actions:
            print(
                f"{ORANGE}Invalid choice! Please choose rock, paper, or scissors.{RESET}"
            )
            return 0  # No winner if invalid input

        if user_action == "sword" and sword_available:
            computer_action = random.choice(
                ["shield"] if random.random() < 0.5 else ["rock", "paper", "scissors"]
            )
            print(
                f"\n{BLUE}{player1_name} chose {user_action}{RESET}, {ORANGE}Computer chose {computer_action}{RESET}.\n"
            )

            if computer_action == "shield":
                print(
                    f"{WHITE}Computer chose shield! It's a tie, and sword can no longer be used.{RESET}"
                )
                sword_available = False
                return 0  # Tie

            print(f"{BLUE}Sword always wins! {player1_name} wins!{RESET}")
            return 1  # Player 1 wins

        computer_action = random.choice(possible_actions[:3])
        print(
            f"\n{BLUE}{player1_name} chose {user_action}{RESET}, {ORANGE}Computer chose {computer_action}{RESET}.\n"
        )

        return determine_winner(user_action, computer_action, player1_name, "Computer")

    else:
        print(
            f"{WHITE}{player1_name}, enter your choice (rock, paper, scissors): {RESET}"
        )
        player1_action = input().lower()  # Player 1 input without prompt

        if player1_action in ["hello", "hi", "hey"]:
            print(
                f"{BLUE}{player1_name} greets {player2_name} warmly! {player2_name}, you may reply with 'hi', 'hello', or 'hey'.{RESET}"
            )
            player2_action = input(
                f"{WHITE}{player2_name}, enter your response: {RESET}"
            ).lower()

            if player2_action == "hello":
                print(
                    f"{GREEN}{player1_name} and {player2_name} share a warm 'Hello!' moment! Back to the game!{RESET}"
                )
                return 0  # Tie
            elif player2_action == "hi":
                print(
                    f"{GREEN}{player1_name} and {player2_name} smile and say 'Hi!' Let's continue the game!{RESET}"
                )
                return 0  # Tie
            elif player2_action == "hey":
                print(
                    f"{GREEN}A casual 'Hey!' echoes between {player1_name} and {player2_name}. Back to the game!{RESET}"
                )
                return 0  # Tie

        sys.stdout.write("\033[F")

        print(
            f"{WHITE}{player2_name}, enter your choice (rock, paper, scissors{', shield' if player1_action == 'sword' and sword_available else ''}): {RESET}"
        )
        player2_action = input().lower()

        possible_actions = [
            "rock",
            "paper",
            "scissors",
            "shield",
        ]  # No "sword" for player 2

        if (
            player1_action not in possible_actions + ["sword"]
            or player2_action not in possible_actions
        ):
            print(
                f"{ORANGE}Invalid choices! Please choose rock, paper, scissors, or shield.{RESET}"
            )
            return 0  # No winner if invalid input

        print(
            f"\n{BLUE}{player1_name} chose {player1_action}{RESET}, {ORANGE}{player2_name} chose {player2_action}{RESET}.\n"
        )

        return determine_winner(
            player1_action, player2_action, player1_name, player2_name
        )


def main():
    game_mode = input(
        f"{WHITE}Do you want to play against the Computer or with another Player? (Enter 'computer' or 'player'): {RESET}"
    ).lower()

    if game_mode == "computer":
        player1_name = "You"
        player2_name = "Computer"
        is_single_player = True
    elif game_mode == "player":
        player1_name = input(f"{WHITE}Enter Player 1's name: {RESET}")
        player2_name = input(f"{WHITE}Enter Player 2's name: {RESET}")
        is_single_player = False
    else:
        print(
            f"{ORANGE}Invalid game mode selected! Please choose 'computer' or 'player'.{RESET}"
        )
        return

    user_wins = 0
    computer_wins = 0

    while True:
        result = play_round(player1_name, player2_name, is_single_player)

        if result == 1:
            user_wins += 1
        elif result == -1:
            computer_wins += 1

        print(
            f"Current Score - {BLUE}{player1_name}: {user_wins}{RESET}, {ORANGE}{player2_name}: {computer_wins}{RESET}\n"
        )

        if user_wins == 3:
            print(f"{BLUE}Congratulations, {player1_name}! You won the game!{RESET}")
            break
        elif computer_wins == 3:
            print(f"{ORANGE}{player2_name} won the game. Better luck next time!{RESET}")
            break


main()
