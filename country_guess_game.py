import csv
import random
# Random word selection logic placeholder

# Load countries from CSV
def load_countries(file_path="countries.csv"):
    countries = []
    try:
        with open(file_path, newline='', encoding="utf-8") as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                countries.append(row["country"].strip())
    except Exception as e:
        print(f"Error reading CSV: {e}")
    return countries

#pick random country naame
def pick_random_country(countries):
    return random.choice(countries).lower()

#Playing the word-huess game
def play_game():
    countries = load_countries()
    if not countries:
        print("No countries found in CSV. Please check your file!")
        return

    word = pick_random_country(countries)
    guessed = set()
    wrong_guesses = set()
    max_attempts = 5

    print("Welcome to the Country Word Guessing Game! 🌍")
    print(f"Guess the country name! You have {max_attempts} wrong attempts allowed.\n")

    while True:
        # Show current state of the word
        display_word = ''.join([letter if letter in guessed else '-' for letter in word])
        print(f"Word: {display_word}")
        print(f"Wrong guesses: {', '.join(wrong_guesses)}")
        
        # Check win condition
        if '-' not in display_word:
            print("\nCongratulations! You guessed the country:", word.capitalize())
            break
        
        # Check lose condition
        if len(wrong_guesses) >= max_attempts:
            print("\nGame over! The country was:", word.capitalize())
            break

        # Ask for input
        guess = input("Enter a letter: ").lower().strip()
        
        if len(guess) != 1 or not guess.isalpha():
            print("Please enter a single alphabet letter.")
            continue

        if guess in guessed or guess in wrong_guesses:
            print("You already tried that letter.")
            continue

        # Check guessing
        if guess in word:
            guessed.add(guess)
            print("Good guess!")
        else:
            wrong_guesses.add(guess)
            print("Wrong guess!")

if __name__ == "__main__":
    play_game()
