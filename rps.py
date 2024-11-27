"""--------------------Rock Paper Scissors--------------------"""

import random  # Import the module

def rps():  # Create the function
    
    choices = ["Rock", "Paper", "Scissors"]  # List of choices

    user = input("Enter your Choice (Rock, Paper, Scissors): ")  # User Input
    userscore = 0  # Initialize the user score
    compscore = 0  # Initialize the computer score

    while True:  # Initialize the loop
        comp = random.choice(choices)  # Computer choice from the list
        print(f"Computer chose: {comp}")  # Show computer's choice
        
        if (user.lower() == "rock" and comp == "Scissors") or \
           (user.lower() == "paper" and comp == "Rock") or \
           (user.lower() == "scissors" and comp == "Paper"):  # Add the conditions
            print("You Won!")  # Print the result
            userscore += 1  # Increment the user score
        elif user.lower() == comp.lower():  # Check for a tie
            print("It's a tie!")  # Print the result
        else:
            print("You Lost!")  # Print the result
            compscore += 1  # Increment the computer score

        print(f"Your Score: {userscore} | Computer's Score: {compscore}")  # Print the score

        # Ask the user if they want to play again
        play_again = input("Do you want to play again? (yes/no): ").lower()
        if play_again != "yes":
            print("Thanks for playing!")
            break

        user = input("Enter your Choice (Rock, Paper, Scissors): ")  # Take the input again

rps()
