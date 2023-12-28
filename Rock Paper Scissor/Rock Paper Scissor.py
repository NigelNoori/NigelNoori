import random

def get_user_choice():
    """
    Get the user's choice for Rock, Paper, or Scissors.
    """
    user_choice = input("Enter your choice (rock, paper, or scissors): ").lower()
    
    # Validate user input
    while user_choice not in ["rock", "paper", "scissors"]:
        print("Invalid choice. Please enter rock, paper, or scissors.")
        user_choice = input("Enter your choice (rock, paper, or scissors): ").lower()
    
    return user_choice

def get_computer_choice():
    """
    Generate a random choice for the computer: Rock, Paper, or Scissors.
    """
    return random.choice(["rock", "paper", "scissors"])

def determine_winner(user_choice, computer_choice):
    """
    Determine the winner based on user and computer choices.
    """
    if user_choice == computer_choice:
        return "It's a tie!"
    elif (
        (user_choice == "rock" and computer_choice == "scissors") or
        (user_choice == "paper" and computer_choice == "rock") or
        (user_choice == "scissors" and computer_choice == "paper")
    ):
        return "You win!"
    else:
        return "Computer wins!"

def play_game():
    """
    Main function to play the Rock, Paper, Scissors game.
    """
    print("Welcome to the Rock, Paper, Scissors game!")

    # Get user and computer choices
    user_choice = get_user_choice()
    computer_choice = get_computer_choice()

    # Display choices
    print(f"You chose {user_choice}.")
    print(f"Computer chose {computer_choice}.")

    # Determine and print the winner
    result = determine_winner(user_choice, computer_choice)
    print(result)

if __name__ == "__main__":
    play_game()
