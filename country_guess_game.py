import csv
import random

def read_countries_from_csv(filename):
    countries = []
    with open(filename, newline='', encoding='utf-8') as csvfile:
        reader = csv.reader(csvfile)
        for row in reader:
            # Assuming country names are in first column; adjust if needed
            countries.append(row[0].strip())
    return countries

def display_word(word, guessed_letters):
    display = ""
    for letter in word:
        if letter.lower() in guessed_letters:
            display += letter
        else:
            display += "-"
    return display

def play_game(filename):
    countries = read_countries_from_csv(filename)
    if not countries:
        print("No countries found in the CSV file.")
        return

    secret_word = random.choice(countries)
    guessed_letters = set()
    wrong_guesses = 0
    max_wrong = 5

    print("Welcome to the Country Guessing Game!")
    while True:
        print("Word: ", display_word(secret_word, guessed_letters))
        guess = input("Guess a letter: ").lower()

        if len(guess) != 1 or not guess.isalpha():
            print("Please guess a single letter.")
            continue

        if guess in guessed_letters:
            print("You already guessed that letter.")
            continue

        guessed_letters.add(guess)

        if guess not in secret_word.lower():
            wrong_guesses += 1
            print(f"Wrong guess! {max_wrong - wrong_guesses} guesses left.")
        else:
            print("Good guess!")

        if all(letter.lower() in guessed_letters or not letter.isalpha() for letter in secret_word):
            print("Congratulations! You guessed the country:", secret_word)
            break

        if wrong_guesses >= max_wrong:
            print("Sorry, you've run out of guesses. The country was:", secret_word)
            break

if __name__ == "__main__":
    # Replace 'countries.csv' with the actual CSV filename containing country names
    play_game("countries.csv")
