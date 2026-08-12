def factorial(num):
    fact = num
    while num > 1:
        fact = fact * (num-1)
        num = num-1
    return fact
        

print(factorial(4))
