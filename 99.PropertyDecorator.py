class Person:
    def __init__(self, name):
        self._name = name

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        if len(value) > 0:
            self._name = value
        else:
            print("Name cannot be empty.")


person = Person("Raj")
print(person.name)  

person.name = "Rohan"  
print(person.name)

person.name = ""  
