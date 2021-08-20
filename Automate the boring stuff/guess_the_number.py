# Programa pra exercitar os conceitos vistos nas primeiras aulas

from time import sleep
from random import randint

print(15*'-')
print('\nTry to guess which number the computer will think\n')
print(15*'-')

print("Hello, what's your name?")
name=input()

print(f"Welcome, {name}. Let's start! \nI'm thinking in a number betwen 1 and 20...")
sleep(2)

comp_number = randint(1,20)

print("Ok, I finished! You have 6 attempts.")

for user_attempts in range(1,7):
    user_guess = int(input(f'Sua tentativa {user_attempts} é: '))

    if user_guess > comp_number:
        print("It's too high.")
    elif user_guess < comp_number:
        print("It's too low.")
    else:
        # condition for right guess
        break

if user_guess == comp_number:
    print(f"\nCONGRATULATIONS {name.upper()}!!\nYou guess the number!")
else:
    print(f"\nNope. The number thinked was {comp_number}")