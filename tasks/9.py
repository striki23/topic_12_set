n, m = (int(i) for i in input('Введите целый числа N и M: ').split())
print('\nНомера цветов кубиков Ани')
cube_Ann: set = {int(input(f'Номер {i}-го цвета кубика: ')) for i in range(1, n + 1)}
print('\nНомера цветов кубиков Бори')
cube_Borya: set = {int(input(f'Номер {i}-го цвета кубика: ')) for i in range(1, m + 1)}

general_num: list = sorted(cube_Ann & cube_Borya)
Ann_uniq: list = sorted(cube_Ann - cube_Borya)
Borya_uniq: list = sorted(cube_Borya - cube_Ann)

print(f'Количество номеров, которые есть в обоих наборах: {len(general_num)}')
print(*general_num)
print(f'Количество номеров, которые есть только у Ани: {len(Ann_uniq)}')
print(*Ann_uniq)
print(f'Количество номеров, которые есть только у Бори: {len(Borya_uniq)}')
print(*Borya_uniq)
