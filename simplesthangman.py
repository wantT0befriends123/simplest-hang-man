import random

# Load words from a file
def load_words(filepath):
    with open(filepath, 'r') as file:
        words = file.read().splitlines()
    return words

# Display the hangman state
def display_hangman(tries):
    stages = [
        """
           -----
           |   |
           O   |
          /|\\  |
          / \\  |
               |
        --------
        """,
        """
           -----
           |   |
           O   |
          /|\\  |
          /    |
               |
        --------
        """,
        """
           -----
           |   |
           O   |
          /|\\  |
               |
               |
        --------
        """,
        """
           -----
           |   |
           O   |
          /|   |
               |
               |
        --------
        """,
        """
           -----
           |   |
           O   |
           |   |
               |
               |
        --------
        """,
        """
           -----
           |   |
           O   |
               |
               |
               |
        --------
        """,
        """
           -----
           |   |
               |
               |
               |
               |
        --------
        """
    ]
    return stages[tries]

# Select difficulty level
def select_difficulty():
    print("Select difficulty level:")
    print("1. Easy")
    print("2. Hard")
    print("3. Impossible")
    choice = input("Enter choice (1/2/3): ")
    if choice == '1':
        return '/Users/gameofapps/Documents/simplest hangman/words_easy.txt'
    elif choice == '2':
        return '/Users/gameofapps/Documents/simplest hangman/words_medium.txt'
    elif choice == '3':
        return '/Users/gameofapps/Documents/simplest hangman/words_hard.txt'
    else:
        print("Invalid choice. Defaulting to Easy.")
        return '/Users/gameofapps/Documents/simplest hangman/words_easy.txt'

# Main game function
def play_hangman():
    word_file = select_difficulty()
    words = load_words(word_file)
    word = random.choice(words).upper()
    word_letters = set(word)
    guessed_letters = set()
    tries = 6

    print("Welcome to Hangman!")
    while tries > 0 and word_letters:
        print(display_hangman(tries))
        print(f"Word: {' '.join([letter if letter in guessed_letters else '_' for letter in word])}")
        print(f"Guessed letters: {', '.join(sorted(guessed_letters))}")
        
        guess = input("Guess a letter: ").upper()
        if guess in guessed_letters:
            print("You already guessed that letter.")
        elif guess in word_letters:
            word_letters.remove(guess)
            guessed_letters.add(guess)
        else:
            tries -= 1
            guessed_letters.add(guess)
            print(f"Wrong guess. You have {tries} tries left.")

    if not word_letters:
        print(f"Congratulations! You guessed the word: {word}")
    else:
        print(display_hangman(tries))
        print(f"Game over. The word was: {word}")