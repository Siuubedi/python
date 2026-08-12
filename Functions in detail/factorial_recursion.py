def factorial(num):
    fact = num

    if num == 1:
        return fact

    return fact * factorial(num-1)


n = 4
print("Factorial of", n, "is:", factorial(n))
