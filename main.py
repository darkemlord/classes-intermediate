from Classes.dog import Dog
from Classes.beagle import Beagle

my_dog = Dog("willie", "male", 6)
neighbor_dog = Dog("spike", "male", 4)
my_beagle = Beagle("buddy", "female", 3, False)

my_dog.sit()
neighbor_dog.sit()
my_dog.roll_over()

my_dog.bark()
neighbor_dog.bark(True)
neighbor_dog.compute_age()

my_beagle.compute_age()
my_beagle.hunt()
