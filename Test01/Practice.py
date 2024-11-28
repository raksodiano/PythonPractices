# Guess the number
import random


def guess_number():
    max_number = 100
    secret_number = random.randint(1, max_number)
    attempts = 0
    guessed = False

    print("Welcome to this guessing game!")
    print(f"Guess a number from 1 to {max_number}")

    while not guessed:
        answer = input(f"Enter the number from 1 to {max_number} that you think it is: ")

        if answer.isdigit():
            answer = int(answer)

            if answer > max_number:
                print(f"The number entered must not be greater than {max_number}")
                continue
            elif answer < 1:
                print("The number entered cannot be less than 1.")
                continue

            attempts += 1

            if answer < secret_number:
                print(f"The number is greater than {answer}")
            elif answer > secret_number:
                print(f"The number is less than {answer}")
            else:
                print(
                    f"You have succeeded!, the number {answer} is correct and you have guessed it in {attempts} tries.")
                break
        else:
            print("Please, enter a valid number")


guess_number()
