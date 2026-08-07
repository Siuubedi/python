# Tuple is used for storing multiple items in a single variable.
# It is similar to array in JS but is immutable so you cannot change the value of the tuple.
# Tuple is created by using parentheses.

marks = (98, 99, 97, 95, 93)
print(type(marks))  # <class 'tuple'>

marks = (98, 99, 97, 95, 93, 95, 95)
# Count the number of occurrences of a value in a tuple.
print(marks.count(95))  # 3

# Get the index (first index if repeating values)
print(marks.index(95))  # 3
