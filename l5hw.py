def count_speed():
    g = 10
    h = int(input("введите высоту"))
    V = (2 * g * h) ** 2
    print(V)

class Animal():
    def __init__(self):
        self.name = ""
        self.color = ""
    def show(self):
        print(self.name, self.color)


class Bird(Animal):
    def __init__(self):
        self.specios = ""
    def show(self):
        print(self.specios)

class Monkey(Animal):
    def __init__(self):
        self.size = ""
    def show(self):
        print(self.size)

class Lion(Animal):
    def __init__(self):
        self.region_in_which_life = ""
    def show(self):
        print(self.region_in_which_life)

class Person():
    def __init__(self):
        self.name = "человек"
        self.age = 17
        int(self.age)
    def have_birthday(self):
            if say_hello():
                self.age += 1
    def say_hello(self):
        print(self.name, self.age, "лет")
    # def have_birthday(self):
    #     if say_hello():
    #         self.age += 1
    def is_adult(self):
        if self.age > 17:
            print("True")
        else:
            print("False")


person1 = Person()
person1.age =18
# print(person1.name, person1.age, "лет")
person1.say_hello()
person1.is_adult()
person2 = Person()
person2.age = 37
persons = Person()
if person1.age > person2.age:
    print("person1 is elder")
elif person2.age > person1.age:
    print("person2 is elder")
