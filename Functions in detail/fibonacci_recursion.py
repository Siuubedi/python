# Print first 5 Fibonacci numbers
def fibonacci(num, fib1=0, fib2=1):
    if num == 0:
        return

    print(fib1, ",", end=" ")

    nextFib = fib1 + fib2

    return fibonacci(num-1, fib2, nextFib)

n = 5
fibonacci(n)
