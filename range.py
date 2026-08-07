range(5)  # 0 1 2 3 4 -> returns sequence of '5' numbers.
range(1, 5)  # 1 2 3 4 -> returns sequence of '4' numbers.

# 1 3 5 7 9 -> returns sequence of '5' numbers, skipping '2' numbers.
nums = range(1, 10, 2)

print(nums)

# 1 3 -> returns sequence of '3' numbers, skipping '2' numbers.
print(range(1, 5, 2))
