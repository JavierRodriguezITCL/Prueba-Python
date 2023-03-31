class Animal:
    def speak(self, string):
        return string

class Dog(Animal):
    def speak(self):
        print(super().speak("Woof"))

class Cat(Animal):
    def speak(self):
        print(super().speak("Meow"))

class Pig(Animal):
    def speak(self):
       print(super().speak("Oink"))
    
perro = Dog()
perro.speak()
