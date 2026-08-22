import random

secret_number = random.randint(1, 10)

print("🎮 Welcome to the Number Guessing Game!")
print("I'm thinking of a number between 1 and 10.")

guess = int(input("Enter your guess: "))

if guess == secret_number:
    print("🎉 Correct! You guessed it!")
elif guess < secret_number:
    print("Too low! The number was", secret_number)
else:
    print("Too high! The number was", secret_number)