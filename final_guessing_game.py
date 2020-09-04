from random import randint
from colorama import init
from termcolor import colored

init()

while True:
    print(colored("WELCOME TO THE GUESSING GAME! CHOOSE A LOWER AND UPPER VALUE TO GUESS BETWEEN...", on_color="on_cyan"))
    while True:
        while True:
            try:
                num1 = int(
                    input("What would you like the lower value to be?\n"))
            except ValueError:
                print(
                    colored("PLEASE ENTER A VALID WHOLE NUMBER INPUT", on_color="on_red"))
            else:
                break
        while True:
            try:
                num2 = int(
                    input("What would you like the upper value to be?\n"))
            except ValueError:
                print(
                    colored("PLEASE ENTER A VALID WHOLE NUMBER INPUT", on_color="on_red"))
            else:
                break
        try:
            number = randint(num1, num2)
            if num2 - num1 >= 4:
                break
            else:
                print(colored(
                    "MAKE SURE THE UPPER VALUE IS AT LEAST 4 MORE THAN THE LOWER VALUE", on_color="on_red"))
                pass
        except ValueError:
            print(colored(
                "MAKE SURE THE UPPER VALUE IS LARGER THAN THE LOWER VALUE", on_color="on_red"))
    attempts = 0
    games = min(abs((num2-num1+1)//5), 25)
    if games == 1:
        print(colored(
            f"You have been assigned {games} attempt, good luck!", on_color="on_magenta"))
    else:
        print(colored(
            f"You have been assigned {games} attempts, good luck!", on_color="on_magenta"))
    while attempts <= games-1:
        while True:
            try:
                guess = input(
                    f"Guess the random number correctly between {num1} and {num2} (type 'q' to quit)\n")
                if guess == "q":
                    pass
                else:
                    guess = int(guess)
            except ValueError:
                print(
                    colored("PLEASE ENTER A VALID WHOLE NUMBER INPUT", on_color="on_red"))
            else:
                break
        if (games-1)-attempts > 0:
            if guess == 'q':
                break
            elif guess < number:
                print(
                    colored(f"Too low, try again... remaining attempts: {(games-1)-attempts}\n", "red"))
                attempts += 1
            elif guess > number:
                print(
                    colored(f"Too high, try again... remaining attempts: {(games-1)-attempts}\n", "red"))
                attempts += 1
            else:
                break
        else:
            if guess == 'q':
                break
            elif guess < number:
                print(
                    colored(f"Too low... remaining attempts: {(games-1)-attempts}\n", "red"))
                attempts += 1
            elif guess > number:
                print(
                    colored(f"Too high... remaining attempts: {(games-1)-attempts}\n", "red"))
                attempts += 1
            else:
                break
    if guess == number:
        print(colored("You guessed correctly, well done!", on_color="on_green"))
        play_again = input(
            "Do you want to play again? (type 'y' to replay, enter anything else to exit)\n").lower()
        if play_again == "y":
            pass
        else:
            print(colored("Thank you for playing :)", "green"))
            break
    else:
        print(colored(f"Unlucky, the number was {number}", on_color="on_red"))
        play_again = input(
            "Do you want to play again? (type 'y' to replay, enter anything else to exit)\n").lower()
        if play_again == "y":
            pass
        else:
            print(colored("Thank you for playing :)", "green"))
            break
