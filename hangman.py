import random

def choose_word():
    words = ["cottontail", "uncontrollable", "smite", "pollen", "beach"]
    return random.choice(words)

def hangman():
    word = choose_word()
    guessed_letters = set()
    attempts = 6

    while attempts > 0:
        display_word = "".join(letter if letter in guessed_letters else "_" for letter in word)
        print(display_word)

        if display_word == word:
            print("Congratulations! You guessed the word!")
            break

        guess = input("Guess a letter: ").lower()
        if guess in guessed_letters:
            print("You already guessed that letter!")
            continue

        guessed_letters.add(guess)

        if guess not in word:
            attempts -= 1
            print(f"Wrong! You have {attempts} attempts left.")

    else:
        print(f"Game over! The word was {word}.")

if __name__ == "__main__":
    hangman()
