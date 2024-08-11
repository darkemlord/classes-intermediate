from .dog import Dog


class Beagle(Dog):
    """A simple attempt to model a beagle."""

    def __init__(self, name, gender, age, is_gun_shy):
        super().__init__(name, gender, age)
        self.is_gun_shy = is_gun_shy

    def hunt(self):
        if self.is_gun_shy:
            print("I'm gun shy!")
        else:
            print("I'm hunting!")

    def speak(self):
        return "Woof"

    def fetch(self):
        return "fetching"
