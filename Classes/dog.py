class Dog:
    """A simple attempt to model a dog."""

    def __init__(self, name, gender, age):
        self.name = name
        self.gender = gender
        self.age = age

    def bark(self, is_loud=False):
        if is_loud:
            print("WOOF WOOF!")
        else:
            print("woof...")

    def sit(self):
        print(self.name.title() + " is now sitting.")

    def roll_over(self):
        print(self.name.title() + " rolled over!")

    def compute_age(self):
        print(self.age * 7)
