# # #lesson 3
# # #if, elif, else
# # print(2+2)
# # print(2/4)
# # #2+2 + оператор, 2 операнд. Операторы бывают бинарные
# # # унарные-2( - оператор, 2 операнд это унарный оператор).
# # #Математические + - * / // % **
# # # Логические > < >= <= == !=
# # #a=5 - занят оператор == - это равно
# # print(5>2)
# # print(4<4)
# # print(4<=4)
# # print(2==2)
# # print(4!=4)
# age = 13#PEP 8 CISCO
# if (age < 18): # True :окончание условия.
#     print('Child')
# if age > 18:
#     print('Adult')
# if True:
#     print('ALWAYS')
# if False:
#     print('NEWER')
# if 1:
#     print(1)
# if 'Something':
#     print('Something')
#
#
#
# age = 18
# if (age < 18):
#     print('Child')
# if age >= 18:
#     print('Adult')
# age = 18
# if (age < 18):
#     print('Child')
# else:
#     print('Adult')



# weight = 120
# if weight < 150:
#     print('Your weight is', weight)
# else:
#     print('Oversize')



# age = 17
# if (age < 0):
#     print('Error-')
# elif age < 13: #else if
#     print('Child')
# elif age < 18:  # else if
#     print('Teen')
# elif age < 135:  # else if
#     print('Super Adult')
# else:
#     print('Error+')

#print ('This will print after all ifs elifs else')


weight = 120
if weight < 0:
    print('error-')
elif weight > 150:
    print('error+')
elif weight < 150:
    print('Your weight is', weight)
elif type(weight) != type(1):
    print('Text type')
else:
    print('Oversize')
##print type(weight) показывает тип str int float bool