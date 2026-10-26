import random

random_num = random.randint(1,10)

previous_guesses = []

correct_guess = False


user_guess = int(input("Enter a number between 1-10 "))

def compare_guesses(user_guess):
    if user_guess > random_num:
        print("Please Try again, the random number is Lower.")

        return False
    elif user_guess < random_num:   
        print("Please Try again, the random number is Higher.")

        return False


    else:
        print("That is the correct number")
        return True



    print("previous guesses ", + previous_guesses)

while correct_guess != True:
    while user_guess < 1 or user_guess > 10:
        print("invaild input")
        user_guess = int(input("invalid, Please enter another number 1-10 "))

    while user_guess in previous_guesses:
        print("you already guessed", previous_guesses)
        user_guess =int(input("choose a different number "))
        while user_guess < 1 or user_guess> 10:
            print("Invalid input")
            user_guess = int(input("please enter another whole number between 1 through 10 "))

    previous_guesses.append(user_guess)
    correct_guess = compare_guesses(user_guess)










