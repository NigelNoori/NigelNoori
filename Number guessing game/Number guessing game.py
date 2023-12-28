import random

def generate_random_number(low, high):
    """
    Generate a random number between the specified low and high bounds.
    """
    return random.randint(low, high)

def get_user_guess():
    """
    Get the user's guess for the randomly generated number.
    """
    guess = input("Enter your guess: ")
    
    # Validate user input
    while not guess.isdigit():
        print("Invalid input. Please enter a valid number.")
        guess = input("Enter your guess: ")
    
    return int(guess)

def play_game():
    """
    Main function to play the number guessing game.
    """
    print("Welcome to the Number Guessing Game!")

    # Set the range for the random number
    low_bound = 1
    high_bound = 100
    random_number = generate_random_number(low_bound, high_bound)

    print(f"I'm thinking of a number between {low_bound} and {high_bound}.")

    attempts = 0
    while True:
        user_guess = get_user_guess()
        attempts += 1

        if user_guess == random_number:
            print(f"Congratulations! You guessed the correct number {random_number} in {attempts} attempts.")
            break
        elif user_guess < random_number:
            print("Too low! Try again.")
        else:
            print("Too high! Try again.")

if __name__ == "__main__":
    play_game()
25