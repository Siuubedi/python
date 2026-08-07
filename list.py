# It is the collection of different items. It can be mutable or immutable.
# List is similar to array in JavaScript.

marks1 = [98, 99, 97, 95, 93]

marks = [98, 99, 97, 95, 93, "A", 92.5]
print(type(marks))  # <class 'list'>

# Operations in list:

# Length
print(len(marks))  # 7

# Indexing
print(marks[0])  # 98

# Reverse Indexing
print(marks[-1])  # 92.5

# Slicing
print(marks[0:3])  # [98, 99, 97]
print(marks[-3:-1])  # [93, "A"]
print(marks[-3:])  # [93, "A", 92.5]
print(marks[:3])  # [98, 99, 97]

# Loop
for score in marks:
    print(score)

# Adding items in list

# Adding item at the end of list:
marks.append(99)
print(marks)  # [98, 99, 97, 95, 93, "A", 92.5, 99]

# Adding item at the particular index of list:
marks.insert(0, 100)
print(marks)  # [100, 98, 99, 97, 95, 93, "A", 92.5, 99]

# To search if any value exists in list:
print(98 in marks)  # True
print(200 in marks)  # False

# Clear an array:
marks1.clear()
print(marks1)  # []
