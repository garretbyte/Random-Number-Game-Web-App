import random

def play_game():
    print("Welcome to the Guess The Right Number Game!")
    print("I'm thinking of a number between 1 and 100.")
    print("Can you guess what it is?")

    number = random.randint(1, 100)
    attempts = 0

    while True:
        guess = input("Enter your guess: ").strip()

        if not guess.isdigit():
            print("Please enter a valid number.")
            continue

        guess = int(guess)
        attempts += 1

        if guess < number:
            print("Too Low!")
        elif guess > number:
            print("Too High!")
        else:
            print(f"Correct! You guesses it in {attempts} attempts.")
            break

def main():
    while True:
        play_game() # Call the play_game function to start the game
        play_again = input("Play again? (yes/no): ").strip().lower()
        if play_again != 'yes':
            print("Thanks for playing! Goodbye!")
            break

if __name__ == "__main__":
    main()
