#!/usr/bin/env python3
# Author: Mikhail Ibrahim
# Date: Mar 27, 2025
# Description: A simple number guessing game with error handling for non-integer input.

import random  # Import random module

# Generate a random number between 0 and 9
correct_answer = random.randint(0, 9)

# Ask the user for their guess
print("Guess a number between 0 and 9.")

try:
    user_guess = int(input())  # Try to convert the input to an integer

    # Check if the guess is correct
    if user_guess == correct_answer:
        print("Answer is correct, congratulations!")  # Correct guess message
    else:
        print(
            f"Are you sure? Try it again! The correct answer was: {correct_answer}"
        )  # Incorrect guess message with answer

except ValueError:
    print(f"{user_guess} is not an integer.")  # Handle non-integer input

finally:
    print("Thanks for playing.")  # End message
