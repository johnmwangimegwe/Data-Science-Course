import random

def choose_word():
    """Selects a random word from a predefined list."""
    words = ["Apple", "Orange", "Banana", "Coconut", "Pineapple", 
         "Mango", "Strawberry", "Blueberry", "Watermelon", "Grapes"]
    return random.choice(words)

def display_word(word, guessed_letters):
    """Displays the word with dashes for unguessed letters."""
    return " ".join([letter if letter in guessed_letters else "_" for letter in word])

def hangman():
    """Main function to execute the Hangman game."""
    word = choose_word()  # Select a random word
    guessed_letters = set()  # Set to store guessed letters
    attempts = 6  # Maximum number of failed attempts
    
    print("Welcome to Hangman Game!")
    
    while attempts > 0:
        print("\nWord:", display_word(word, guessed_letters))
        print(f"Attempts left: {attempts}")
        
        # Get user input
        #When a user inputs a capitilized letter, the .lower() method returns the letter to a lower case
        guess = input("Guess a letter: ").lower()
        
        # Input validation: must be a single letter
        # A string is alphabetic if all characters are alphabetic and at least one character is in the string.
        if len(guess) != 1 or not guess.isalpha():
            print("Invalid input. Please enter a single letter.")
            continue
        
        # Check if the letter has already been guessed
        if guess in guessed_letters:
            print("You already guessed that letter. Try another.")
            continue
        
        guessed_letters.add(guess)  # Add letter to guessed set
        
        if guess in word:
            print("Good guess!")
        else:
            print("Wrong guess! You Can Try Again")
            attempts -= 1  # Reduce attempts for wrong guesses
        
        # Check if the player has guessed all letters
        if all(letter in guessed_letters for letter in word):
            print("\nCongratulations! You guessed the word:", word)
            return
    
    # Game over condition
    print("\nGame Over! The word was:", word)
    print("You Lost!")

# Run the game
if __name__ == "__main__":
    hangman()
