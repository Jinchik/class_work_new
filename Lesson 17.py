# l = [1, 2, 3] - list
# t = (1, 2, 3) - tuple
# d = {'a': 1, } - dict
# s = {1, 2, 3, 4} - set
# fs = {1, 2, 3} - frozenset
#
#
# for element in l:
#     print(element)
#
#
#
# for i in range(len(l)):
#     print(l[i])
#
# a = [i for i in range(10)]  #in line
# print (a)
#
# # Without if dict
# n1 = 2
# command = '+'
# n2 = 2
# calc = {'+': n1 + n2, '-': n1-n2}
# print(calc[command])

#Многомерные массивы
# l2 = [[1,2,3],[4,5,6],[7,8,9]]
# print(l2)
# for i in range(len(l2)):
#     for j in range(len(l2[i])):
#         print(l2[i][j],end=' ')
#     print()
# print(l2[0][1], l2[1][1], l2[2][1])



# tictactoe_board = [[1,2,3],[4,5,6],[7,8,9]]
# for y in range(9):
#     turn = int(input("Enter number of cell: "))
#     for i in range(len(tictactoe_board)):
#         for j in range(len(tictactoe_board[i])):
#             if tictactoe_board[i][j] == turn:
#                 tictactoe_board[i][j] = 'X'
#     for i in range(len(tictactoe_board)):
#         for j in range(len(tictactoe_board[i])):
#             print(tictactoe_board[i][j], end=' ')
#         print()


# d = {'a': 1, 'b': 2, 'c':3}

# s = set('asdasdasd')
# print(s)
# s = set([1,2,3,3,3,4,4,4])
# print(s)
# s = set((1,2,3,4,5,5,5))
# print(s)
# s = set({'a': 1, 'b': 2, 'c': 3})
# print(s)
# some_list = [9,1,2,3,4,3,4,5,6,7,8,8,4,2,1,7,0,9]
# some_list = list(set(some_list))
# print(some_list)

s = 'a+s+d+s+d+f+s+d+f+f+f+f+a'
s = s.split('+')#-преобразует строку в список символов
print(s)


fs = {1,2,3,4,5} # frozenset кортеж множества, неименный.