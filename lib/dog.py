#!/usr/bin/env python3

APPROVED_BREEDS = [
    "Mastiff",
    "Chihuahua",
    "Corgi",
    "Shar Pei",
    "Beagle",
    "French Bulldog",
    "Pug",
    "Pointer"
]

class Dog:
    def __init__(self, name="Dog", breed="Pug"):
        self._name = None
        self._breed = None
        self.name = name  # This will use the setter method
        self.breed = breed  # This will use the setter method

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, name):
        if isinstance(name, str) and (1 <= len(name) <= 25):
            self._name = name
        else:
            self._name = None
            print("Name must be string between 1 and 25 characters.")

    @property
    def breed(self):
        return self._breed

    @breed.setter
    def breed(self, breed):
        if breed in APPROVED_BREEDS:
            self._breed = breed
        else:
            self._breed = None
            print("Breed must be in list of approved breeds.")
