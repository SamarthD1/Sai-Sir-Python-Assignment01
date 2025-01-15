class Animal:
    def __init__(self, name):
        self.name = name
    
    def speak(self):
        print(f"{self.name} makes a sound.")

class Dog(Animal):
    pass
    
animal = Animal("Generic Animal")
animal.speak()

dog = Dog("Buddy")
dog.speak()