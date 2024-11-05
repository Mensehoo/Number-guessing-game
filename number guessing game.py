import random

def number_guessing_game():
    target_number = random.randint(1, 100)
    attempts = 0

    print("Welcome to the number guessing game!")
    print("I have chosen a number between 1 and 100. Try to guess the number.!")

    while True:
        try:
            guess = int(input("Enter your guess: "))
            attempts += 1

            if guess < target_number:
                print("Your guess is too low. Try a higher number.")
            elif guess > target_number:
                print("Your guess is too high. Try a lower number.")
            else:
                print(f"Congratulations! You successfully guessed the {target_number} in {attempts} trials..")
                break

        except ValueError:
            print("Invalid input. Please enter a number.")

number_guessing_game()
