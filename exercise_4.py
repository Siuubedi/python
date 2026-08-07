# Get a list of roll numbers: [101, 105, 102, 101, 108, 105, 110]. Print all unique roll nums in the list.
roll_number = {101, 105, 102, 101, 108, 105, 110}  # -> Need to make this a set
print(roll_number)


# Given Employee records in the form of a lit or tuples where each tuple contains:
# (Employee ID, Employee Name, Salary)
# [
#     (101, "Alice", 50000),
#     (102, "Bob", 65000),
#     (103, "Charlie", 45000)
# ]
# Ask user to enter Employee ID and search it inside records.

employee = [
    (101, "Alice", 50000),
    (102, "Bob", 65000),
    (103, "Charlie", 45000)
]

id = int(input("Enter Employee ID: "))
i = 0
for record in employee:
    for ID in record:
        if (ID == id):
            print("Employee with id:", id, "is", record[i])
    i = i+1
