# Create student class that takes name & marks of 3 students as arguments in constructor.
# Then create a method to print the average.

class Student:
    def __init__(self, name, marks1, marks2, marks3):
        self.name = name
        self.marks1 = marks1
        self.marks2 = marks2
        self.marks3 = marks3

    def average(self):
        avg = round((self.marks1 + self.marks2 + self.marks3) / 3, 2)
        print("Average marks of", self.name, "is", avg)
        return avg


s1 = Student("Gaurav", 10.5, 20, 30)
s1.average()
