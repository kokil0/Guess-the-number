import random

cnumber = random.randint(1, 200)
name=input("May i ask your name?\n")
print(name, "we are going to play a game. I am thinking of a number between 1 to 200")
print("Go ahead. Guess!")
attempts = 0
maximum_attempts = 6
while attempts<maximum_attempts:
    user_number = int(input("Guess: "))

    attempts += 1
    if cnumber == user_number:
        print("Yes you are right")
        break
    elif cnumber > user_number:
        print("The guess of the number that you have entered is too low")
        print("Try again!")
    else:
        print("The guess of the number that you have entered is too high")
        print("Try again!")

if attempts == maximum_attempts:
    print("Nope. The number I was thinking of was ", cnumber)
    input("Do you want to play again?\n")