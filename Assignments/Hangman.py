import random  #Used to randomly select a word from the predefined list.
import turtle  #Used to draw the hangman figure step by step.

# Game configuration constants
words = ["Apple", "Orange", "Banana", "Coconut", "Pineapple", 
         "Mango", "Strawberry", "Blueberry", "Watermelon", "Grapes"]
Attempts = 6 #The number of incorrect guesses allowed before losing.
Text_Font = ("Times Roman", 24, "bold") #Defines the font style and size for messages displayed using Turtle.

# Initialize turtle graphics
def setup_turtle():
    """Initializes the turtle settings."""
    turtle.speed(5) # Sets the drawing speed
    turtle.hideturtle() # Hides the turtle cursor for a cleaner UI
    turtle.penup() # Prevents drawing while moving

def draw_gallows():
    """
    This function creates the hangman's stand, including the base, vertical pole, horizontal beam, and rope.
    Draws the hangman stand.
    """
    turtle.goto(-100, -200)  # Move turtle to base position
    turtle.pendown()  # Start drawing

    turtle.forward(200)  # Draws the base
    turtle.backward(100)  # Returns to the center of the base
    turtle.left(90)  # Rotates turtle upward
    turtle.forward(250)  # Draws the vertical pole
    turtle.right(90)  # Rotates turtle to the right
    turtle.forward(100)  # Draws the horizontal beam
    turtle.right(90)  # Rotates turtle downward
    turtle.forward(30)  # Draws the short rope
    turtle.penup()  # Stop drawing

def draw_head():
    """Draws the head of the hangman."""
    turtle.goto(80, 0)  # Position at the end of the rope
    turtle.pendown()
    turtle.circle(20)  # Draws a circle for the head
    turtle.penup()

def draw_body():
    """Draws the body."""
    turtle.goto(100, -20)  # Moves below the head
    turtle.pendown()
    turtle.setheading(270)  # Faces downward
    turtle.forward(80)  # Draws the body
    turtle.penup()

def draw_left_arm():
    """Draws the left arm."""
    turtle.goto(100, -30)  # Moves to the shoulder area
    turtle.pendown()
    turtle.setheading(225)  # Faces diagonally left
    turtle.forward(45)  # Draws the left arm
    turtle.penup()

def draw_right_arm():
    """Draws the right arm."""
    turtle.goto(100, -30)  # Moves to the shoulder area
    turtle.pendown()
    turtle.setheading(315)  # Faces diagonally right
    turtle.forward(45)  # Draws the right arm
    turtle.penup()

def draw_left_leg():
    """Draws the left leg."""
    turtle.goto(100, -100)  # Moves to the hip area
    turtle.pendown()
    turtle.setheading(225)  # Faces diagonally left
    turtle.forward(45)  # Draws the left leg
    turtle.penup()

def draw_right_leg():
    """Draws the right leg."""
    turtle.goto(100, -100)  # Moves to the hip area
    turtle.pendown()
    turtle.setheading(315)  # Faces diagonally right
    turtle.forward(45)  # Draws the right leg
    turtle.penup()

# Ordered list of body parts to draw
# A list containing the functions that draw different parts of the hangman.
# This allows sequential drawing based on incorrect guesses.
hangman_parts = [draw_head, draw_body, draw_left_arm, draw_right_arm, draw_left_leg, draw_right_leg]

def draw_message(message, emoji):
    """Displays a win/lose message below the gallows."""
    turtle.goto(0, -250)  # Move below the gallows
    turtle.write(f"{message} {emoji}", align="center", font=Text_Font)

def initialize_game():
    """Resets the game setup."""
    turtle.clear()  # Clears the screen
    turtle.title("Hangman Game")  # Sets window title
    setup_turtle()  # Initializes turtle
    draw_gallows()  # Draws the gallows
    return random.choice(words).lower()  # Selects a random word and keeps the letter in lower case


def validate_guess(letter, guessed_letters):
    """Validates user input."""
    if len(letter) != 1 or not letter.isalpha() or letter in guessed_letters:
        print("Invalid input. Enter a new single letter.")
        return False
    return True

def update_display(target_word, current_display, guess):
    """Updates displayed word with guessed letters."""
    return [guess if target_word[i] == guess else current_display[i] for i in range(len(target_word))]

def play_hangman():
    """
    Main game loop.
    Handles user input, updates guesses, and draws the hangman.
    Displays a message if the user wins or loses.
    """
    secret_word = initialize_game()
    guessed = set()
    display = ['_'] * len(secret_word)
    mistakes = 0

    while mistakes < Attempts:
        print("\nWord:", ' '.join(display))
        print(f"Guesses left: {Attempts - mistakes}")
        print("Used letters:", ', '.join(sorted(guessed)))

        try:
            guess = input("Guess a letter: ").lower()
            if not validate_guess(guess, guessed):
                continue
        except KeyboardInterrupt:
            print("\nGame aborted!")
            return

        guessed.add(guess)

        if guess in secret_word:
            display = update_display(secret_word, display, guess)
            if '_' not in display:
                draw_message("YOU WIN!", "😊")
                print(f"\nVictory! The word was: {secret_word}")
                turtle.exitonclick()
                return
        else:
            hangman_parts[mistakes]()
            mistakes += 1
            print(f"Incorrect! {Attempts - mistakes} tries left.")

    draw_message("YOU LOSE!", "😢")
    print(f"\nGame Over! The word was: {secret_word}")
    print("Click on the window to close.")
    turtle.exitonclick()

if __name__ == "__main__":
    play_hangman()
