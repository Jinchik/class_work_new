#Файлы
import random
import time

# f = open('test.txt','wt') #t -text, /b - binary,w открыть файл на запись, r открыть файл на чтение.
# #open('fff','rt')
# f.write('My name is Andrey\nHow are you')
# # time.sleep(15)
# f.close()
# # random.randint()
# f = open('test.txt','rt')
# print(f.read())
# f.close()
# f = open('test.txt','rt')
# print(f.read()) #Считывает файл целиком не безопасен.
# f.close()
# f = open('test.txt','rt')
# print(f.readline()) # Читывает файл построчно, как итерируемый объект
# print(f.readline())
# print(f.readline())
# print(f.readline())
# f.close()
# f = open('test.txt','rt')
# print(f.readlines())# Считывает целеком как список

# #Write
# f = open('test.txt','wt')
# f.write('My name is Andrey\nHow are you')
# f.close
#a add открыть файл на запись, если нет файла, создать, если есть файл, добавить в конец.
# f = open('test.txt','at')
# f.write('My name is Andrey\nHow are you\n')
# f.close

#X открывает файл на запись, если файл есть ошибка, если нет создает.
# f = open('test.txt1','xt')
# f.write('Hey\nHow are you\n')
# f.close
#+ = открытие файла на чтение и запись
# f = open('test.txt1','rt+')
# f.write('Hey\nHow are you\n')
# f.close


# Режим	Обозначение
# 'r'	открытие на чтение (является значением по умолчанию).
# 'w'	открытие на запись, содержимое файла удаляется, если файла не существует, создается новый.
# 'x'	открытие на запись, если файла не существует, иначе исключение.
# 'a'	открытие на дозапись, информация добавляется в конец файла.
# 'b'	открытие в двоичном режиме.
# 't'	открытие в текстовом режиме (является значением по умолчанию).
# '+'	открытие на чтение и запись


# file = open("text.txt", "w")
# file.write("Your text goes here")
# file.close()
# 'r' open for reading (default)
# 'w' open for writing, truncating the file first
# 'x' open for exclusive creation, failing if the file already exists
# 'a' open for writing, appending to the end of the file if it exists


# import random
# f = open('numbers1.txt','wt')
# for i in range(10):
#     for j in range(10):
#         f.write(str(random.randint(1,9)))
#     f.write('\n')
# f.close()
#
# import random
# f = open('numbers2.txt','wt')
# for i in range(10):
#     for j in range(10):
#         f.write(str(random.randint(1,9)))
#     f.write('\n')
# f.close()


n1 = open('numbers1.txt','rt')
n2 = open('numbers2.txt','rt')
n3 = open('numbers3.txt','wt')
ln1 = n1.readline()
ln2 = n2.readline()
while ln1 or ln2:
    n3.write(ln1)
    n3.write(ln2)
    ln1 = n1.readline()
    ln2 = n2.readline()
n3.close()
