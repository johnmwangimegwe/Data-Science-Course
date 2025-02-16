
import random
import turtle

# List of words for the game
WORDS = [
    "python", "hangman", "code", "computer", "keyboard"
]

# Function to draw the hangman stand
def draw_gallows():
    turtle.speed(5)
    turtle.penup()
    turtle.goto(-100, -200)
    turtle.pendown()
    turtle.forward(200)  # Draw base
    turtle.backward(100)  # Go back to the center
    turtle.left(90)
    turtle.forward(250)  # Draw vertical pole
    turtle.right(90)
    turtle.forward(100)  # Draw top beam
    turtle.right(90)
    turtle.forward(30)  # Draw small rope

# Function to draw the head
def draw_head():
    turtle.penup()
    turtle.goto(80, 0)  # Position for head
    turtle.pendown()
    turtle.circle(20)  # Draw head circle

# Function to draw the body
def draw_body():
    turtle.penup()
    turtle.goto(100, -20)  # Start below the head
    turtle.pendown()
    turtle.setheading(270)  # Pointing downwards
    turtle.forward(80)  # Draw torso

# Function to draw the left arm
def draw_left_arm():
    turtle.penup()
    turtle.goto(100, -30)
    turtle.pendown()
    turtle.setheading(225)  # Angle for left arm
    turtle.forward(45)  # Draw left arm

# Function to draw the right arm
def draw_right_arm():
    turtle.penup()
    turtle.goto(100, -30)
    turtle.pendown()
    turtle.setheading(315)  # Angle for right arm
    turtle.forward(45)  # Draw right arm

# Function to draw the left leg
def draw_left_leg():
    turtle.penup()
    turtle.goto(100, -100)
    turtle.pendown()
    turtle.setheading(225)  # Angle for left leg
    turtle.forward(45)  # Draw left leg

# Function to draw the right leg
def draw_right_leg():
    turtle.penup()
    turtle.goto(100, -100)
    turtle.pendown()
    turtle.setheading(315)  # Angle for right leg
    turtle.forward(45)  # Draw right leg

# List of drawing steps in order
hangman_parts = [
    draw_head, draw_body,
    draw_left_arm, draw_right_arm,
    draw_left_leg, draw_right_leg
]

# Function to start the game and choose a word
def start_game():
    turtle.clear()  # Clear any previous drawings
    turtle.title("Hangman Game")
    turtle.hideturtle()
    draw_gallows()  # Draw the stand
    return random.choice(WORDS).lower()  # Pick a random word

# Function to check if input is valid
def check_input(letter, guessed):
    if len(letter) != 1:  # Must be a single letter
        print("Enter only one letter.")
        return False
    if not letter.isalpha():  # Must be a letter
        print("Only letters are allowed.")
        return False
    if letter in guessed:  # Must be a new guess
        print("You already guessed that letter.")
        return False
    return True

# Function to update the word display
def update_display(word, display, letter):
    return [letter if word[i] == letter else display[i] for i in range(len(word))]

# Main function to run the game
def play_hangman():
    word = start_game()  # Get a random word
    guessed_letters = set()  # Keep track of guessed letters
    display = ['_'] * len(word)  # Display hidden word
    mistakes = 0  # Count incorrect guesses
    max_mistakes = 6  # Maximum allowed mistakes

    while mistakes < max_mistakes:
        print("\nCurrent word:", ' '.join(display))
        print(f"Attempts left: {max_mistakes - mistakes}")
        print("Guessed letters:", ', '.join(sorted(guessed_letters)))

        guess = input("Enter a letter: ").lower()

        if not check_input(guess, guessed_letters):
            continue  # Ask for input again if invalid

        guessed_letters.add(guess)  # Store guessed letter

        if guess in word:  # If letter is in word
            display = update_display(word, display, guess)
            if '_' not in display:  # If no blanks remain, user wins
                print(f"\nCongratulations! You won! The word was: {word}")
                turtle.clearscreen()
                return
        else:  # If guess is wrong
            hangman_parts[mistakes]()  # Draw next body part
            mistakes += 1
            print(f"Wrong guess. {max_mistakes - mistakes} attempts left.")

    print(f"\nGame Over! The word was: {word}")  # If player loses
    print("Click on the window to close.")
    turtle.exitonclick()

# Run the game if script is executed
if __name__ == "__main__":
    play_hangman()
