import random

number = random.randint(1,100)
player = input("Hello, what is your name? ")
print(f"Hey {player}! Let's play a guessing game.")
no_of_guess = 0

while no_of_guess < 5:
    try:
        guess_number = int(input("Guess a number between 1 and 100: "))
        no_of_guess += 1
        if guess_number < number:
            print("You guessed too low")
        if guess_number > number:
            print("You guesses too high")
        if guess_number == number:
            print(f"You guessed the number in {no_of_guess} tries!")
            break
    except ValueError:
        print("Error! You need to enter a number.")
if no_of_guess >= 5:
    print(f"You exceeded the attempts. The correct number is {number}.")
