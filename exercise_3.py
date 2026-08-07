# Print all odd number from 1 to 20.
for i in range(1, 21):
    if i % 2 == 1:
        print(i)

# print the table of 57.
num = 57
count = 1

while count <= 10:
    print(num, "x", count, "=", num*count)
    count += 1

# Print all multiples of 3 from 1 to 50, skip 15.
for i in range(3, 51):
    if i % 3 == 0:
        if i == 15:
            continue
        print(i)

# Take two integers a and b as input. Find and print the first number between 1 and 1000 that is divisible by both numbers.
a = int(input("Enter first number: "))
b = int(input("Enter second number: "))

for i in range(1, 1001):
    if i % a == 0 and i % b == 0:
        print(i)
        break
