# Dictionary is used for storing key-value pairs.
# It is similar to object in JS.
# It is ordered, changeable and doesn't allow duplicates.

dict = {
    "name": "Gaurav",
    "name": "Subedi"
}

# print(dict) # {"name": "Subedi"} -> This is because dictionary only stores the latest value if the key is repeated.

student = {
    "name": "Gaurav",
    "age": 24,
    "address": "Bangalore",
    "isPassedOut": True,
    "cgpa": 8.91,
}

print(student)

print(student["address"]) # Bangalore

# To change the value of a key:
student["address"] = "Waling"
print(student)

# To add a new key-value pair:
student["phone"] = "9846071244"
print(student)

# To apply loop on dictionary:
for key in student:
    print(key, student[key])