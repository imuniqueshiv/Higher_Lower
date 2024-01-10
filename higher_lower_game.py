from art import logo, vs  # Import ASCII art from the 'art' module
from game_data import data  # Import data from the 'game_data' module
import random  # Import the 'random' module for random number generation
import os  # Import the 'os' module for system-related functionality

def clear_screen():
    # Clear the terminal screen based on the operating system
    os.system('cls' if os.name == 'nt' else 'clear')

# Call the function to clear the screen

def format_data(account):
    """Format the account data into printable format."""
    # Extract information from the 'account' dictionary and format it into a string
    account_name = account['name']
    account_Description = account['description']
    account_Country = account['country']
    return f" {account_name}, a {account_Description}, from {account_Country}."

def check_answer(guess, follower_count1, follower_count2):
    """Take the user guess and follower counts and returns if they got it right."""
    # Compare follower counts based on the user's guess and return True if correct, False otherwise
    if follower_count1 > follower_count2:
        return guess == "a"
    else:
        return guess == "b"

# Choose the first account for comparison
account_2 = random.choice(data)   

# Print the game logo
print(logo)
score = 0
game_should_continue = True
while game_should_continue: 
    # Set account_1 to the previous account_2 and choose a new account_2
    account_1 = account_2
    account_2 = random.choice(data)
    
    # Ensure that account_1 and account_2 are different
    while account_1 == account_2:
        account_1 = random.choice(data)

    # Display the formatted information of the two accounts for comparison
    print(f"Compare A: {format_data(account_1)}.")
    print(vs)
    print(f"Against B: {format_data(account_2)}.")

    # Take user input for their guess
    guess = input("Who has more followers?: Type 'a' for person1 or 'b' for person2: ").lower()

    # Count followers for each account
    follower_count1 =  account_1['follower_count']
    follower_count2 =  account_2['follower_count']
    
    # Check if the user's guess is correct and update the score
    is_correct = check_answer(guess, follower_count1, follower_count2)
    
    # Clear the screen for the next iteration
    clear_screen()
    print(logo)
    
    # Provide feedback based on the correctness of the guess
    if is_correct:
        score += 1
        print(f"You're right! Current score: {score}")
    else:
        game_should_continue = False
        print(f"Sorry, that's wrong. Final score: {score}")
