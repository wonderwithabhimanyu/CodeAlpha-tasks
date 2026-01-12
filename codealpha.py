import random

AlphaWords = ["Abhimanyu", "kumar", "Alpha", "CodeAlpha","Sample"]

word = random.choice(AlphaWords)

#CodeAlpha Game Variables
guess_latters = []
wrong_guess = 0
max_wrong_guesses = 6

print("Welcome to CodeAlpha, Hangman!")
display_word = '_' * len(word)
print("You Have 6 Attempts to Guess the Word")

display_word = "_" * len(word)

#Game Loop
while wrong_guess < max_wrong_guesses and '_' in display_word:
    print("\nCurrent Word: ", ' '.join(display_word))
    guess = input("Guess a letter: ").strip()

    if len(guess) != 1 or not guess.isalpha():
        print("Please enter a single alphabetical character.")
        continue

    if guess in guess_latters:
        print("You already guessed that letter. Try again.")
        continue

    guess_latters.append(guess)

    if guess in word:
        print("Good guess!")
        display_word = ''.join([letter if letter in guess_latters else '_' for letter in word])
    else:
        wrong_guess += 1
        print(f"Wrong guess! You have {max_wrong_guesses - wrong_guess} attempts left.")