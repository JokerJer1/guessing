import random
print("Welcome to the Number Guessing Game! \nI'm thinking of a number between 1 and 100. \nYou have 5 chances to guess the correct number. ")



random_int = random.randint(1, 100)

def difficulty():
    while True:
        try:
            difficulty = int(input("\nPlease select the difficulty level: \n1. Easy (10 chances) \n2. Medium (5 chances) \n3. Hard (3 chances)\nEnter your choice: "))
            
            if difficulty == 1:
                print("Great! You have selected the Easy difficulty level.")
                return 10  # Return number of chances for Easy level
            elif difficulty == 2:
                print("Great! You have selected the Medium difficulty level.")
                return 5   # Return number of chances for Medium level
            elif difficulty == 3:
                print("Great! You have selected the Hard difficulty level.")
                return 3   # Return number of chances for Hard level
            else:
                print("Invalid choice. Please enter 1, 2, or 3.")
        except ValueError:
            print("Invalid input. Please enter a number.")


diff = difficulty()

def guess_check(answer, difficulty):
    count = 1
    while count <= difficulty:
        guess = int(input("Enter your guess: "))
        count += 1
        if guess == answer:
            print(f"Congratulations! You guessed the correct number in {count} attempts.")
            break
        elif guess > answer:
            print(f"Incorrect! The number is less than {guess}.")
        elif guess < answer:
            print(f"Incorrect! The number is greater than {guess}.")
        else:
            print("Out of range! Try again!")
    print(f"Game over! The correct number was {answer}!")


guess_check(random_int, diff)