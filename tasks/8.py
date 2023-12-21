# Вводится последовательность целых чисел через пробел
# Программа для каждого числа выводит "ДА" в отдельной строке,
# если это число ранее встречалось в последовательности
# или "НЕТ", если не встречалось.
numbers = [int(i) for i in input('Введите числа через пробел: ').split()]

for idx, i in enumerate(numbers):
    if i in numbers[:idx]:
        print('ДА')
    else:
        print('НЕТ')

# 65 10 98 65 43 10

# Option 2
# seen: set[int] = set()
# for n in numbers:
#     if n in seen:
#         print('ДА')
#     else:
#         print('НЕТ')
#         seen.add(n)
