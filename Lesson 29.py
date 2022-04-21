class WashingMachine:
    # Методы класса
    twisting = "50 per minute"
    __weight = 10
    color = "White"
    electric_count = 100
    id = 1
    count_of_water = 10
    #Методы класса
    @classmethod
    def activate(cls):
        cls.electric_count = 10000000

    # Методы объекта
    def __init__(self, weight, color):
        # Поля объекта
        self.weight = weight
        self.color = color

    def __add__(self, other):  # +
        self.weight = self.weight + other.weight

    def __int__(self):
        print("NOT INIT")

    def __str__(self):
        return (f"Weight : {self.weight}\nColor : {self.color}")

    def washing(self, weight_of_clothes):
        if self.weight > weight_of_clothes:

            print('Start wash')
        elif self.weight == weight_of_clothes:

            print('A bit Heavy')
        else:
            print('Heavy....')

    def drying(self):
        print('Start dry')

    def spining(self):
        print('Start spin')

    @property  # getter
    def weight(self):
        return self.__weight

    @weight.setter
    def weight(self, new_weight):
        if new_weight >= 0 and new_weight <= 1000:
            self.__weight = new_weight
        else:
            print("WEIGHT")

    @weight.deleter
    def weight(self):
        print('Oh noooo!')


lg = WashingMachine(20, 'red')
samsung = WashingMachine(70, 'black')
print(lg.weight)
s = str(lg)
print(s)
lg.weight = 100000
lg.washing(19)
lg.washing(20)
lg.washing(21)
del lg.weight
# print(samsung.weight)
# lg+samsung
# print(lg.weight)
# lg+samsung
# a=6
# print(lg.weight)
# int(lg)
# lg + a not working
# print(lg.count_of_water)
# lg.count_of_water = 20
# print(lg.count_of_water)
# print(lg.color)
# print(lg)
# s = str(lg)
# print(s)
#
# class O:
#     number = 0
#     def __init__(self, number):
#         self.number = number
#     def __add__(self, other):
#         self.number1 = self.number + other.number +1
#         return self.number1
#     def __eq__(self, other):
#         return "Lie"
#     def __str__(self):
#         return str(self.number)
#
# a = O(2)
# b = O(2)
# c = a + b
# print(a == b)
# print(a.number,'+',b, "=", a + b)
print(WashingMachine.color)
print(WashingMachine.id)
print(lg.id)
lg.id = 33
print(lg.id)
print(WashingMachine.id)
print(WashingMachine.electric_count)
print(lg.electric_count)
