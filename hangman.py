import random
import os 
import time 

def choose_word():
    with open("words.txt", "r") as file:
        words = file.read().splitlines()
    
    return random.choice(words)

def display_word(word, guessed_letters):
    display = ""
    for letter in word:
        if letter in guessed_letters:
            display += letter
        else:
            display += "_"
    return display

def print_hangman(attempts):
    hangman_stages = [
        """
        -----
        |   |
            |
            |
            |
            |
        ------
        """,
        """
        -----
        |   |
        O   |
            |
            |
            |
        ------
        """,
        """
        -----
        |   |
        O   |
        |   |
            |
            |
        ------
        """,
        """
        -----
        |   |
        O   |
       /|   |
            |
            |
        ------
        """,
        """
        -----
        |   |
        O   |
       /|\\  |
            |
            |
        ------
        """,
        """
        -----
        |   |
        O   |
       /|\\  |
       /    |
            |
        ------
        """,
        """
        -----
        |   |
        O   |
       /|\\  |
       / \\  |
            |
        ------
        """
    ]

    print(hangman_stages[6 - attempts])
def hangwon():
    hangwon_stages = [
         """
        -----
        |   |
        O   |
       /|\\  |
       / \\  |
            |
        ------
        """,
        
        """
        -----
        |   |
        O   |
       /|\\  |
       / \\  |
        \O/   |
        ------
        """,
        
        """
        -----
        |   |
        O   |
       /|\\  |
       / \\  |
        \O/   |
         |    |
        ------
        """
    ]

    for _ in range(3):  
        for frame in hangwon_stages:
            os.system('cls' if os.name == 'nt' else 'clear') 
            print(frame)
            time.sleep(0.5) 


def hangman():
    print("Welcome to Hangman!")
    secret_word = choose_word()
    guessed_letters  = []
    attempts = 6
    
    print("The word has", len(secret_word), "letters.")
    while attempts > 0:
        print("\nAttempts left:", attempts)
        current_display = display_word(secret_word, guessed_letters)
        print("Current Word:", current_display)

        guess = input("Guess a letter: ").lower()

        if len(guess) != 1 or not guess.isalpha():
            print("Please enter a single alphabetical character.")
            continue

        if guess in guessed_letters:
            print("You've already guessed that letter. Try again.")
            continue

        guessed_letters.append(guess)

        if guess not in secret_word:
            print("Incorrect guess!")
            print_hangman(attempts)
            attempts -= 1

        if "_" not in display_word(secret_word, guessed_letters):
            hangwon()
            print("Congratulations! You've guessed the word:", secret_word)
            break

    if attempts == 0:
        print("Sorry, you've run out of attempts. The word was:", secret_word)

if __name__ == "__main__":
    hangman()
