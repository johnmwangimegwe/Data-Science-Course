#import the random library used to generate random choices for the computer.
import random

def get_computer_choice():
    """
    Randomly selects and returns the computer's choice (rock, paper, or scissors).
    """
    choices = ["rock", "paper", "scissors"] #list of possible choices.
    return random.choice(choices) #Randomly picks one from the list using random.choice() and returns it.

def determine_winner(user_choice, computer_choice): #A function taking 2 parameters that is user choice and computer choice
    """
    Determines the winner of a round based on the rules of Rock-Paper-Scissors.
    Returns 'user', 'computer', or 'draw'.
    """
    if user_choice == computer_choice:
        return 'draw' #consistently returns a value
    elif user_choice == 'rock' and computer_choice == 'scissors':
        return 'user'
    elif user_choice == 'scissors' and computer_choice == 'paper':
        return 'user'
    elif user_choice == 'paper' and computer_choice == 'rock':
        return 'user'
    else:
        return 'computer'

def play_game(rounds):
    """
    Plays a Rock-Paper-Scissors game for a specified number of rounds.
    Stops early if a player reaches an unbeatable lead.
    """
    user_score = 0
    computer_score = 0
    max_score = (rounds // 2) + 1  # Minimum score needed to win the game

    """
    // is the floor division operator. 
    It performs division but rounds the result down to the nearest whole number (integer).
    """
    for round_num in range(1, rounds + 1):
        print(f"\nRound {round_num}")
        print("Enter your choice: 0 for Rock, 1 for Paper, 2 for Scissors")
        
        # Get user input and validate
        while True:
            try:
                user_input = int(input("Your choice (0, 1, or 2): "))
                if user_input in [0, 1, 2]:
                    break
                else:
                    print("Invalid input. Please enter 0, 1, or 2.")
            except ValueError: #Inappropriate argument value (of correct type).
                print("Invalid input. Please enter a number (0, 1, or 2).")

        # Map user input to choice
        choices = ['rock', 'paper', 'scissors'] #choices is a list where 0 -> rock, 1 -> paper, 2 -> scissors.
        user_choice = choices[user_input] #Converts the number into the corresponding string.
        computer_choice = get_computer_choice() #calls the function

        print(f"You chose: {user_choice}")
        print(f"Computer chose: {computer_choice}")

        # Determine the winner of the round
        winner = determine_winner(user_choice, computer_choice)
        if winner == 'user':
            user_score += 1
            print("You win this round!")
        elif winner == 'computer':
            computer_score += 1
            print("Computer wins this round!")
        else:
            print("It's a draw!")

        print(f"Score: You {user_score} - {computer_score} Computer")

        # Check if a player has reached the maximum score to win the game
        if user_score >= max_score or computer_score >= max_score:
            break

    # Declare the overall winner
    if user_score > computer_score:
        print("\nCongratulations! You win the game!")
    elif computer_score > user_score:
        print("\nSorry, the computer wins the game.")
    else:
        print("\nThe game is a draw.")

def main():
    """
    Main function to run the Rock-Paper-Scissors game.
    """
    print("Welcome to Rock-Paper-Scissors!")
    print("You will enter 0 for Rock, 1 for Paper, or 2 for Scissors.")
    
    # Get the number of rounds
    while True:
        try:
            rounds = int(input("Enter the number of rounds (3 or 5): "))
            if rounds in [3, 5]:
                break
            else:
                print("Invalid number of rounds. Please choose 3 or 5.")
        except ValueError:
            print("Invalid input. Please enter a number (3 or 5).")

    play_game(rounds)

if __name__ == "__main__":
    main()