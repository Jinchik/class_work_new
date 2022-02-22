# ООП
# a = int(5)
# b = str('Hello')
# c = list([1, 3, 5])
#
#
# # 2 + 2 = 5
#
# class Box:
#     v = 5  # Поле класса(Field), атрибут класса, поле класса, переменная класса, аргумент класса.
#
#     # Параметры класса: Что? Сколько? Какой? Где? Существительное
#     def open(self, count):  # Метод класса, method, функция класса.
#         print(f'Open {count} box')  # Глагол: что сделать, как сделать?
#
#
# lanch = Box()
# print(lanch.v)
# lanch.open()
#
# tools = Box()
# tools.open()

class Borsch:
    volume = 3
    color = 'red'
    componts = ['Beetroot', 'Tomato', 'Meat', 'Potato']
    temperature = 20.5
    vegeterian = False
    create_date = '22/02/2022'
    life_period = 480

    def heating(self):
        self.temperature = self.temperature + 5

    def show_heat(self):
        return self.temperature

    def more_borsch(self):
        self.volume = self.volume + 1

    def show_volume(self):
        return self.volume
    def change_color(self,new_color):
        self.color = new_color
# self.color = new.color

andrii_borsch = Borsch()
print(andrii_borsch.show_heat())
print((andrii_borsch.show_volume()))
andrii_borsch.more_borsch()
andrii_borsch.heating()
andrii_borsch.heating()
andrii_borsch.heating()
print(andrii_borsch.show_heat())
print((andrii_borsch.show_volume()))


sten_borsch = Borsch()
sten_borsch.color = 'green'

print(andrii_borsch.color)
print(sten_borsch.color)
andrii_borsch.change_color('yellow')
print(andrii_borsch.color)
print(sten_borsch.color)