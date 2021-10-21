import random

print("Number Guesing Game")

number = random.randint(1,9)
chance = 0
print("Gues a number between (0 to 9):")

while chance < 5:

    guess = int(input("Enter your Guess:-"))

    if guess == number :
        print("You Won")
        break

    elif guess < number:
        print("Your guess is very low: guess a number higher than",guess)
    else:
        print("Your guess is very high: guess a number lower than",guess)
        chance +=1

    if not chance < 5:
        print("You Lose, the number is ",number)   
