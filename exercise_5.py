# Write a function to check if a number is even or odd.
num = int(input("Enter a number: "))

if num == 0:
    print(num, "is neither even nor odd number.")
    exit()

if num % 2 == 0:
    print(num, "is even number")

elif num % 2 != 0:
    print(num, "is odd number")

else:
    print(num, "is neither even nor odd number.")


# Write a function to count the number of vowels in a string
string = input("Enter a string: ")

count = 0

for i in string:
    # if i in "aeiou":
    if i == "a" or i == "e" or i == "i" or i == "o" or i == "u" or i == "A" or i == "E" or i == "I" or i == "O" or i == "U":
        count += 1

print(string, "contains", count, "vowels")


# Write a function to check if a number is prime or not
num = int(input("Enter a number: "))


def primeCheck(num):
    if num <= 1:
        return False

    if num == 2 or num % 2 == 0:
        return False

    for i in range(3, num):
        if num % i == 0:
            return False
    return True


isPrime = primeCheck(num)
if isPrime:
    print(num, "is a prime number")
else:
    print(num, "is not a prime number")
