"""--------------------Hangaman Game--------------------"""

import random # Import the Module.

def play_hangman(): # Create the main Function.
    words = ['python', 'javascript', 'java', 'ruby', 'kotlin'] # The words, You can add more.
    word = random.choice(words) # Choosing the words.
    guessed_word = ['_'] * len(word)
    attempts = 6

    print("--------------------Hangaman Game--------------------")
    print(" ".join(guessed_word))

    while attempts > 0 and '_' in guessed_word: # Initialize the Loop.
        guess = input("Guess a letter: ").lower()

        if guess in word:                             # |
            for i, letter in enumerate(word):         # | 
                if letter == guess:                   # |   Initialize the Conditional Statements.
                    guessed_word[i] = guess           # |
        else:                                         # |
            attempts -= 1
            print(f"Wrong guess! {attempts} attempts remaining.")

        print(" ".join(guessed_word))

    if '_' not in guessed_word: # Print the Output.
        print("Congratulations! You've guessed the word.")
    else:
        print(f"Game over! The word was {word}.")

play_hangman() # Call the Function.
