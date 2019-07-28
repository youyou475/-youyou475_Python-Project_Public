import random

number = random.randint(1,10)
guess1 = input("Guess This Number(From 1 to 10):")
guess2 = int(guess1)
guesstimes = 0

if guess2 > number:
    print("It's smaller than yours.")
if guess2 < number:
    print("It's bigger than yours.")

while guesstimes < 3:
    guess1 = input("Try again:")
    guess2 = int(guess1)
    if guess2 > number:
        print("It's smaller than yours.")
    if guess2 < number:
        print("It's bigger than yours.")
    guesstimes += 1
    if guess2 == number:
        print("It's right!You are good!")
        break
else:
    print("You don't have any times.Hope you can win next time!")