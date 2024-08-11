import unittest
from Classes.dog import Dog


class TestDog(unittest.TestCase):
    def setUp(self):
        self.my_dog = Dog("willie", "male", 6)
        self.neighbor_dog = Dog("spike", "male", 4)

    def test_sit(self):
        self.assertIsNone(self.my_dog.sit())
        self.assertIsNone(self.neighbor_dog.sit())

    def test_roll_over(self):
        self.assertIsNone(self.my_dog.roll_over())

    def test_bark(self):
        self.assertIsNone(self.my_dog.bark())
        self.assertIsNone(self.neighbor_dog.bark(True))

    def test_compute_age(self):
        self.assertIsNone(self.my_dog.compute_age())
        self.assertIsNone(self.neighbor_dog.compute_age())


if __name__ == "__main__":
    unittest.main()
