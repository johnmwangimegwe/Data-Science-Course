# Import the random module to let the computer pick a random choice
import random

# Function to get the computer's choice
def get_computer_choice():
    """
    This function selects a random choice for the computer.
    The choices are 'rock', 'paper', and 'scissors'.
    """
    choices = ["rock", "paper", "scissors"]  # List of choices
    return random.choice(choices)  # Randomly pick one and return it

# Function to decide who wins a round
def determine_winner(user_choice, computer_choice):
    """
    This function compares the user's choice and the computer's choice 
    and determines the winner of a single round.
    
    Returns:
        - 'user' if the user wins
        - 'computer' if the computer wins
        - 'draw' if both choices are the same
    """
    if user_choice == computer_choice:
        return "draw"  # If both choices are the same, it's a draw
    elif user_choice == "rock" and computer_choice == "scissors":
        return "user"  # Rock beats Scissors
    elif user_choice == "scissors" and computer_choice == "paper":
        return "user"  # Scissors beats Paper
    elif user_choice == "paper" and computer_choice == "rock":
        return "user"  # Paper beats Rock
    else:
        return "computer"  # If none of the above, the computer wins

# Function to play the game for multiple rounds
def play_game(rounds):
    """
    This function runs the game for the given number of rounds.
    The game stops early if one player reaches an unbeatable score.
    """
    
    user_score = 0  # Keeps track of the user's score
    computer_score = 0  # Keeps track of the computer's score
    
    """
    // is the floor division operator. 
    It performs division but rounds the result down to the nearest whole number (integer).
    """

    # The number of points needed to win before all rounds are played
    max_score = (rounds // 2) + 1  # Example: If rounds = 3, max_score = 2

    # Loop through the number of rounds
    for round_num in range(1, rounds + 1):
        print(f"\nRound {round_num}")  # Show the current round number
        
        # Explain the choices to the user
        print("Enter your choice: 0 for Rock, 1 for Paper, 2 for Scissors")

        # Get a valid choice from the user
        while True:
            try:
                user_input = int(input("Your choice (0, 1, or 2): "))
                if user_input in [0, 1, 2]:  # Check if input is valid
                    break  # Exit the loop if input is correct
                else:
                    print("Invalid input. Please enter 0, 1, or 2.")  # Ask again
            except ValueError:  # If input is not a number
                print("Invalid input. Please enter a number (0, 1, or 2).")

        # Convert the user's number input to the actual choice (rock, paper, or scissors)
        choices = ["rock", "paper", "scissors"]  # List of possible choices
        user_choice = choices[user_input]  # Convert number to word
        computer_choice = get_computer_choice()  # Get the computer's choice

        # Show both choices
        print(f"You chose: {user_choice}")
        print(f"Computer chose: {computer_choice}")

        # Determine the winner of this round
        winner = determine_winner(user_choice, computer_choice)
        
        # Update the score and announce the winner
        if winner == "user":
            user_score += 1  # Increase user's score
            print("You win this round!")
        elif winner == "computer":
            computer_score += 1  # Increase computer's score
            print("Computer wins this round!")
        else:
            print("It's a draw!")

        # Display current score
        print(f"Score: You {user_score} - {computer_score} Computer")

        # Stop the game early if a player reaches max_score
        if user_score >= max_score or computer_score >= max_score:
            break  # Exit the loop if the game is already decided

    # Announce the final winner
    if user_score > computer_score:
        print("\n🎉 Congratulations! You win the game!")
    elif computer_score > user_score:
        print("\n😔 Sorry, the computer wins the game.\n Kindly Try Again")
    else:
        print("\n🤝 The game is a draw.\n Nice Play")

# Function to start the game
def main():
    """
    This function asks the user how many rounds they want to play 
    and starts the game.
    """
    
    print("Welcome to Rock-Paper-Scissors!")  # Welcome message
    print("You will enter 0 for Rock, 1 for Paper, or 2 for Scissors.")
    
    # Ask the user for the number of rounds (must be 3, 5, 7, or 9)
    while True:
        try:
            rounds = int(input("Enter the number of rounds (3, 5, 7, or 9): "))
            if rounds in [3, 5, 7, 9]:  # Check if input is valid
                break  # Exit the loop if input is correct
            else:
                print("Invalid number of rounds. Please choose 3, 5, 7, or 9.")  # Ask again
        except ValueError:  # If input is not a number
            print("Invalid input. Please enter a number (3, 5, 7, or 9).")

    # Start the game with the chosen number of rounds
    play_game(rounds)

# Run the main function when the program starts
if __name__ == "__main__":
    main()
