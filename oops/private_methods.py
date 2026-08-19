class Person:
    __name = "Anonymous"

    def __hello(self):
        print("Hola, Amigo!")

    def welcome(self):
        self.__hello()


p1 = Person()
p1.welcome()  # Hola, Amigo!

p1.__hello()  # Error: AttributeError: can't access private attribute '__hello'
