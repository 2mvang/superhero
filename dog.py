# dog.py
class Dog:
     # Required properties are defined inside the __init__ constructor method
    def __init__(self, name, breed):## Only put REQUIRED things
        self.name = name
        self.breed = breed
    # Methods are defined as their own named functions inside the class
    def bark(self):
        print("Woof!")
    def sit(self):
        print("<> sits")
    def roll(self):
        print("<> rolls over")

## Will print
##  <__main__.Dog object at 0x101488278> # The Dog Class
##  Rex # your dog's name
