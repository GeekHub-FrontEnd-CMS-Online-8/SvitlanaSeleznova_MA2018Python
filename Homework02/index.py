import SimpleGUICS2Pygame.simpleguics2pygame as simplegui
import random

num_range = 100
secret = 0
user_guess = 0
num_guesses = 7

def new_game():
    global secret, num_range, num_guesses
    secret = random.randrange(0, num_range)
    if num_range == 100:
        num_guesses = 7
    elif num_range == 1000:
        num_guesses = 10
    else:
        print("Please choose a range.")

    print("")
    print("A new game has started with a range from 0 to " + str(num_range) + ".")
    print("You have " + str(num_guesses) + " guesses remaining.")

def decrement_guesses():
    global num_guesses
    num_guesses = num_guesses - 1
    if num_guesses > 0:
        print("Remaining guesses: " + str(num_guesses))
    else:
        print("Sorry, you lose! The number was " + str(secret) + ".")
        new_game()

def range100():
    global num_range
    num_range = 100
    new_game()

def range1000():
    global num_range
    num_range = 1000
    new_game()


def input_guess(guess):
    global secret, user_guess
    user_guess = int(guess)
    print("")
    if user_guess == secret:
        print("Your guess was " + str(user_guess))
        print("You win!")
        new_game()
    elif user_guess > secret:
        print("Your guess was " + str(user_guess))
        print("Lower!")
    elif user_guess < secret:
        print("Your guess was " + str(user_guess))
        print("Higher!")
    else:
        print("Something went terribly wrong!")
    decrement_guesses()

f = simplegui.create_frame("Guess the number",300,300)

f.add_button("Range [0, 100]", range100, 200)
f.add_button("Range [0, 1000]", range1000, 200)
f.add_input("Enter guess", input_guess, 50)

new_game()
f.start()