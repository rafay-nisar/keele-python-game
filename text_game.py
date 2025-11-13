import random

# Simple console guessing game for Keele assessment

def main():
    print("Welcome to the improved guessing game!")
    print("I'm thinking of a number between 1 and 20.")

    number = random.randint(1, 20)
    attempts = 0

    while True:
        try:
            guess = int(input("Take a guess: "))
            attempts += 1
            if guess < number:
                print("Too low! Try again.")
            elif guess > number:
                print("Too high! Try again.")
            else:
                print(f"Good job! You guessed it in {attempts} attempts.")
                break
        except ValueError:
            print("Please enter a whole number between 1 and 20.")
            print("You can guess as many times as you like, or press Ctrl+C to stop.")

if __name__ == "__main__":
    main()
