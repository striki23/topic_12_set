# Вводится два списка целых чисел каждый с новой строки
# Программа выводит числа (в порядке возрастания), кот входят в оба списка

numbers_1: set = {int(i) for i in input('Введите элементы 1-го списка: ').split()}
numbers_2: set = {int(i) for i in input('Введите элементы 2-го списка: ').split()}

general_num = numbers_1 & numbers_2
print(*sorted(general_num))

# 89 12 45 87 20 97 21 24 54 76 23 56 7
# 23 98 15 97 34 12 56 23 78 8 74 81 21 89
