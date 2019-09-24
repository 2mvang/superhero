# my-dogs.py
import dog
from dog import Dog

annie = dog.Dog("Annie", "SuperDog")
print(annie.name)
annie.bark()

chomp = dog.Dog("Chomp", "ArgDog")
print(chomp.name)
chomp.sit()

milky = dog.Dog("Milky", "BobaDog")
print(milky.name)
milky.roll()
