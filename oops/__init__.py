class Student:
    college = "Jain University"

    def __init__(self, name):
        self.name = name
        print(self.name, "fron init function studies at", self.college)
        print("Adding new student in DB.")

    # The call_name() function is the method of the Student class.
    def call_name(self):
        print(self.name, "from call_name function studies at", self.college)


s1 = Student("Gaurav")
# Calling method.
s1.call_name()
# print(s1.name) # Output: Gaurav

print("---------------------------------------------------")

s2 = Student("Subedi")
s2.call_name()
