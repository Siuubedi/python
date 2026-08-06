print(5+3)
print(5-3)
print(5*3)
print(5/3)  # Output: 1.6666666666666667
print(5//3)  # Output: 1 (This returns the integer part of the result without rounding off the decimal part)

# Modulo
print(5 % 3)  # Output: 2

# Power
print(5**3)  # => 5^3

# Assignment
x = 1
print(x+1)  # Output: 2

x += 1
print(x)  # Output: 2

x -= 1
print(x)  # Output: 1

x *= 2
print(x)  # Output: 2

# Operator Precedence
a = 1
b = 2
c = 3

d = a + b * c  # => 1 + (2 * 3)
e = a + (b * c)  # => 1 + (2 * 3)
f = (a + b) * c  # => (1 + 2) * 3
g = a * b + c  # => 1 * 2 + 3
h = a * b / c  # => 1 * 2 / 3
i = a / b * c  # => 1 / 2 * 3

print(d)  # Output: 7
print(e)  # Output: 7
print(f)  # Output: 9
print(g)  # Output: 5
print(h)  # Output: 0.6666666666666666
print(i)  # Output: 1.5
# The last two are different because in operator precedence, if multiplication and division are mixed, then the one in the left gets executed first.
