# Вводится два списка целых чисел каждый с новой строки
# Программа проверяет есть ли у них хотя бы один общий элемент

numbers_1: set = {int(i) for i in input('Введите элементы первого списка: ').split()}
numbers_2: set = {int(i) for i in input('Введите элементы второго списка: ').split()}

general_num = numbers_1 & numbers_2
if not general_num:
    print('Списки не имеют общих элементов')
else:
    print('Да, списки имеют общий элемент:', general_num)

# 1 2 3 4 5
# 5 6 7 8 9
