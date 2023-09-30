class Student():
    def __init__(self):
        self.name = "Миша"
        self.klass = "9"

    def say_hello(self):
        print("Привет", self.name, "из", self.klass, "класса")

student1 = Student()
student1.say_hello()
student1.name = "Максим"
student1.klass = "7"
student1.say_hello()

class Animal():
    def __init__(self):
        self.name = "Собака"
        self.sound = "Гав"

    def voise(self):
        print(self.sound)

animal1 = Animal()
animal1.voise()
animal1.name = "Кошка"
animal1.sound = "Мяу"
animal1.voise()

class Book():
    def __init__(self):
        self.name = "Властелин Колец"
        self.avtor = '"Джон Роналд Руэл Толкин"'

    def info(self):
        print(self.avtor, self.name)

book1 = Book()
book1.info()

class Fruit():
    def __init__(self):
        self.name = "Яблоко"
        self.color = "Красное"

    def info(self):
        print(self.name, '-', self.color)

fruit1 = Fruit()
fruit1.info()
