import sys

al_num = {'A', 1, 'B', 2, 'C', 3}
fruits = {'Kiwi', 'Orange', 'Coconut', 'Pineapple', 'Mandarin'}
browsers = {(1, 'Chrome'), (2, 'Yandex'), (3, 'Firefox'), (4, 'Opera')}

print(f'Размер множества al_num {sys.getsizeof(al_num)} байт')
print(f'Размер множества fruits {sys.getsizeof(fruits)} байт')
print(f'Размер множества browsers {sys.getsizeof(browsers)} байт')
