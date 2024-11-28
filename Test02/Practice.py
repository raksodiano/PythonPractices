# The incredible game of Hangman
import random


def load_words_from_file() -> str:
    """
    Reads a list of words from a file named 'Words.txt' located in the same directory
    as the script and returns a random word from the list.

    :return: A random word from the list in the file.
    """
    try:
        # Open and read the file 'Words.txt' in the same directory
        with open('./Words.txt', 'r', encoding='utf-8') as file:
            # Read all lines from the file and remove any extra spaces or empty lines
            words_list = [line.strip() for line in file if line.strip()]

        # Choose a random word from the list of words
        words_dict = random.choice(words_list)

        # Return the selected word
        return words_dict

    except FileNotFoundError:
        print(f"Error: The file 'Words.txt' was not found in the current directory.")
        return None
    except Exception as e:
        print(f"An error occurred: {e}")
        return None


def progress(secret_word, letters_guessed):
    letter_guessed = ''

    for letter in secret_word:
        if letter in letters_guessed:
            letter_guessed += letter
        else:
            letter_guessed += '_'

    return letter_guessed


def game_hangman():
    secret_word = load_words_from_file()
    letters_guessed = []
    attempts = len(secret_word) + 3
    game_over = False

    print("Welcome to the incredible game of Hangman!")
    print(f"In this opportunity you have {attempts} guesses to guess the word")
    print(progress(secret_word, letters_guessed))

    while not game_over and attempts > 0:
        answer = input("Enter a letter: ").lower()

        if len(answer) != 1 or not answer.isalpha():
            print("Enter a valid letter")
            continue
        elif answer in letters_guessed:
            print("You have already used that letter")
            continue
        else:
            letters_guessed.append(answer)

            if answer in secret_word:
                print("A guessed letter!")
            else:
                attempts -= 1
                print("The letter is not in the word")
                print(f"You have {attempts} attempts left")

        current_progress = progress(secret_word, letters_guessed)

        if "_" not in current_progress:
            game_over = True
            print("You Win!")
            print(f"guessed word {secret_word}, in {attempts} attempts")

    if attempts == 0:
        print(f"Sorry, the word was {secret_word}")


game_hangman()
