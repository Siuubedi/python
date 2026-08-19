class Person:
    __name = "Anonymous"


pr = Person()
print(pr.__name)  # Error: AttributeError: can't access private attribute '__name'
