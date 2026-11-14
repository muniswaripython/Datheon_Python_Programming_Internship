import random

# Load English words from words.txt
def load_words():
    try:
        with open("words.txt", "r") as file:
            words = [
                word.strip().lower()
                for word in file
                if word.strip().isalpha()
            ]

        words = [word for word in words if 4 <= len(word) <= 12]

        if words:
            return words

    except FileNotFoundError:
        print("Words file not found!")

    return ["python", "computer", "program", "developer"]


# ASCII Hangman drawings
stages = [
    """
       -----
       |   |
           |
           |
           |
           |
    =========
    """,
    """
       -----
       |   |
       O   |
           |
           |
           |
    =========
    """,
    """
       -----
       |   |
       O   |
       |   |
           |
           |
    =========
    """,
    """
       -----
       |   |
       O   |
      /|   |
           |
           |
    =========
    """,
    """
       -----
       |   |
       O   |
      /|\\  |
           |
           |
    =========
    """,
    """
       -----
       |   |
       O   |
      /|\\  |
      /    |
           |
    =========
    """,
    """
       -----
       |   |
       O   |
      /|\\  |
      / \\  |
           |
    =========
    """
]


# Main Hangman game
def play_game():

    words = load_words()

    secret_word = random.choice(words)

    guessed_letters = set()

    attempts = 6

    print("\n================================")
    print("     WELCOME TO HANGMAN GAME")
    print("================================")

    print("Guess the hidden word.")
    print("You have 6 incorrect attempts.")

    while attempts > 0:

        print(stages[6 - attempts])

        display_word = ""

        for letter in secret_word:

            if letter in guessed_letters:
                display_word += letter + " "
            else:
                display_word += "_ "

        print("\nWord:", display_word)

        print("Remaining attempts:", attempts)

        print("Guessed letters:", sorted(guessed_letters))

        # Check winning condition
        if all(letter in guessed_letters for letter in secret_word):

            print("\nCongratulations! YOU WON!")
            print("The correct word was:", secret_word)

            return

        guess = input("\nEnter one letter: ").lower().strip()

        # Validate input
        if len(guess) != 1 or not guess.isalpha():

            print("Please enter only one alphabet letter.")
            continue

        # Prevent duplicate guesses
        if guess in guessed_letters:

            print("You already guessed this letter!")
            continue

        guessed_letters.add(guess)

        # Check the guessed letter
        if guess in secret_word:

            print("Correct guess!")

        else:

            attempts -= 1

            print("Wrong guess!")

    # Losing condition
    print(stages[6])

    print("\nGAME OVER! YOU LOST.")

    print("The correct word was:", secret_word)


# Start the game
if __name__ == "__main__":
    play_game()