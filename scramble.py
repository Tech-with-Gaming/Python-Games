"""--------------------Unscramble The Word--------------------"""

import random # Import the Module.

def scramble_word(word): # Create The Scrambling Function.
    scrambled = list(word)
    random.shuffle(scrambled)
    return ''.join(scrambled)

def play_word_scramble(): # Create the Function.
    words = ["python", "javascript", "java", "ruby", "kotlin"] # The word, You can add more.
    word = random.choice(words) # Scrambling the Word.
    scrambled = scramble_word(word)

    print("--------------------Unscramble The Word--------------------")

    print("Unscramble the word: " + scrambled) # Print Output.
    guess = input("Your guess: ")

    if guess == word:
        print("Correct!")
    else:
        print(f"Wrong! The word was {word}.")

play_word_scramble() # Call the Function.
