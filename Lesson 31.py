# Задание 4
# Создайте класс «Дробь». Необходимо хранить в полях
# класса: числитель и знаменатель. Реализуйте методы класса
# для ввода данных, вывода данных, реализуйте доступ к
# отдельным полям через методы класса. Также создайте
# методы класса для выполнения арифметических операций (сложение, вычитание, умножение, деление, и т.д.).
# class Fraction:
#     numerator = int()
#     denominator = int()
#
#     def __init__(self, number):
#         self.numerator = int(number[:number.find('/')])
#         self.denominator = int(number[number.find('/') + 1:])
#
#     def __str__(self):
#         return f'{self.numerator}/{self.denominator}'
#
#     def __add__(self, other):
#         n1 = self.numerator * other.denominator
#         n2 = self.denominator * other.denominator
#         n3 = other.numerator * self.denominator
#         n4 = other.denominator * self.denominator
#         denominator = n2
#         numerator = n1 + n3
#         return f'{numerator}/{denominator}'
#
#     def decemation(self):
#         return self.numerator/self.denominator
# d = Fraction('11/24')
# e = Fraction('5/11')
#
#
# print(d)
# print(e)
# print(d,"+",e,"=",d+e)
#
# h = Fraction(d+e)
# print(h)
# print(h.decemation())


class Human:
    age = int()
    gender = str()
    height = int()
    weight = float()
    prof = str()
    name = str()
    surname = str()
    hp = int()
    sp = int()
    streight = int()
    stamina = int()
    hunger = int()
    __graduation = str()

    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.prof = 'child'
        self.age = 0
        __graduation = "Child"

    def __str__(self):
        return f'Name: {self.name} Surname : {self.surname} Profession : {self.prof}'

    def change_prof(self, new_prof):
        self.prof = new_prof

    def wait_one_year(self):
        self.age = self.age + 1

    @property
    def graduation(self):
        return self.__graduation

    @graduation.setter
    def graduation(self, new_graduation):
        if self.age >= 0 and self.age <= 6 and "Child" in new_graduation:
            self.__graduation = new_graduation
        if self.age >= 6 and self.age <= 15 and "School" in new_graduation:
            self.__graduation = new_graduation
        if self.age >= 15 and self.age <= 20 and "Colledge" in new_graduation:
            self.__graduation = new_graduation
        if self.age >= 18 and self.age <= 22 and "University" in new_graduation:
            self.__graduation = new_graduation


# Задание 1
# Создайте класс Human, который будет содержать
# информацию о человеке.
# С помощью механизма наследования, реализуйте класс
# Builder (содержит информацию о строителе), класс Sailor
# (содержит информацию о моряке), класс Pilot (содержит
# информацию о летчике).
# Каждый из классов должен содержать необходимые
# для работы методы
import random


class Builder(Human):
    __position = str()

    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.prof = 'Builder'
        self.age = 18
        self.__graduation = random.choice(['College', 'University'])

    @property
    def position(self):
        return self.__position

    @position.setter
    def position(self, new_position):
        if "College" in self.__graduation and new_position in ['Journeyman','Master']:
            self.position = new_position
        if "University" in self.__graduation and new_position in ['Journeyman', 'Master',"Foreman"]:
            self.position = new_position


bender = Builder('Bender', 'Rodrogez')
print(bender)
print(bender.graduation)
bender.position = "Foreman"
print(bender.position)
