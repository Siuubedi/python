# Create student class that takes name & marks of 3 students as arguments in constructor.
# Then create a method to print the average.
# Here take the marks as a list

class Student:
    def __init__(self, name, marks):
        self.name = name
        self.marks = marks

    def average(self):
        sum = 0
        for i in range(len(self.marks)):
            sum = sum + self.marks[i]

        avg = round(sum / len(self.marks), 2)
        return avg


s1 = Student("Gaurav", [10, 20, 30])
print("Average marks of", s1.name, "is", s1.average())
