class Person:
    def __init__(self, name: str, age: int, gender: str):
        self.name = name
        self.age = age
        self.gender = gender

    def introduce(self):
        print(f"Hello, my name is {self.name}. I am {self.age} years old and I am  {self.gender}.")

# Taking runtime input
name = input("Enter your name: ")
age = int(input("Enter your age: "))
gender = input("Enter your gender: ")

person = Person(name, age, gender)
person.introduce()
