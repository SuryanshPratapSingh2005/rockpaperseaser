import random

def determine_winner(user_choice, computer_choice):
    """Determines the winner of a rock-paper-scissors game.

    Args:
        user_choice: The user's choice (rock, paper, or scissors).
        computer_choice: The computer's choice (rock, paper, or scissors).

    Returns:
        A string representing the winner ("user", "computer", or "tie").
    """

    if user_choice == computer_choice:
        return "tie"
    elif user_choice == "rock":
        if computer_choice == "scissors":
            return "user"
        else:
            return "computer"
    elif user_choice == "paper":
        if computer_choice == "rock":
            return "user"
        else:
            return "computer"
    elif user_choice == "scissors":
        if computer_choice == "paper":
            return "user"
        else:
            return "computer"

def play_rock_paper_scissors():
    """Plays a rock-paper-scissors game with the user.

    Prints the user's choice, the computer's choice, and the winner.
    """

    # Prompt the user to choose rock, paper, or scissors.
    user_choice = input("Choose rock, paper, or scissors: ")

    # Validate the user's choice.
    while user_choice not in ["rock", "paper", "scissors"]:
        user_choice = input("Invalid choice. Choose rock, paper, or scissors: ")

    # Generate a random choice (rock, paper, or scissors) for the computer.
    computer_choice = random.choice(["rock", "paper", "scissors"])

    # Determine the winner.
    winner = determine_winner(user_choice, computer_choice)

    # Print the user's choice, the computer's choice, and the winner.
    print("You chose:", user_choice)
    print("The computer chose:", computer_choice)
    print("The winner is:", winner)

if __name__ == "__main__":
    play_rock_paper_scissors()
