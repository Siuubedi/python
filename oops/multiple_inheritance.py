class A:
    varA = "From Class A"


class B:
    varB = "From Class B"


class C(A, B):
    varC = "From Class C"


c1 = C()
print(c1.varC)  # From Class C

# Multiple Inheritance
print(c1.varA)  # From Class A
print(c1.varB)  # From Class B
