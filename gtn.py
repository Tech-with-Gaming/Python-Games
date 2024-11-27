"""--------------------Guess The Number--------------------"""


import random # Import the Module.

def gtn(): # Make the Function.
    print("--------------------Guess The Number--------------------")
    
    guess = int(input("Enter Your Guess: ")) # Take the Input from the User.
    comp = random.randint(0, 100) # The Computer's Guess.
    guesses = 0 # Number of Guesses.

    while True: # Initialize the Loop.
        if guess < comp: # Add the Condition.
            print("Go High") # Print the Result.
            guesses += 1 # Increment the Guesses.
            guess = int(input("Enter Your Guess: ")) # Take the Input Again.

        elif guess > comp: # Add the Condition.
            print("Go Low") # Print the Result. 
            guesses += 1 # Increment the Guesses.
            guess = int(input("Enter Your Guess: ")) # Take the Input Again.


        elif guess == comp: # Add the Condition.
            print("You Won") # Print the Result.
            guesses += 1 # Increment the Guesses.
            print(f"You Guessed the Number in {guesses:,} times.") # Print the Number of Guesses also Format with Commas. (Optional)
            break # Break the Loop.

gtn() # Call the Function.