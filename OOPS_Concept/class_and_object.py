# simple class example

class Student:

    def __init__(self, name, age):

        self.name = name
        self.age = age

    def display(self):

        print(self.name)
        print(self.age)

s1 = Student("Soujanya", 21)

s1.display()