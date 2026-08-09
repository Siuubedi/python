import random

number = int(input("Enter your guess number: "))

secret_number = random.randint(1, 50)

while secret_number != number:
    if secret_number > number:
        number = int(input("Enter a higher number: "))
    
    elif secret_number < number:
        number = int(input("Enter a lower number: "))

print("You guessed the number!")