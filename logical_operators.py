# Logical Operators: and, or, not

# or

st1 = 3 > 5
st2 = 3 < 5

print(st1 or st2)  # Output: True

st2 = 3 > 12
print(st1 or st2)  # Output: False

# and
st1 = 3 < 5
st2 = 3 < 12
print(st1 and st2)  # Output: True

st2 = 3 > 12
print(st1 and st2)  # Output: False

# not
print(True)  # Output: True
print(not True)  # Output: False
print(not False)  # Output: True
print(not (3 > 2))  # Output: False
