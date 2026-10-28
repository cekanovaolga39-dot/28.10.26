#   Вложенные списки
matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

print(matrix[0])       # [1, 2, 3] — первая строка
print(matrix[1][2])    # 6 — вторая строка, третий элемент
print(matrix[2][0])    # 7

#   Строки
items = input("Введите элементы через пробел: ").split()
print(items)  # ['яблоко', 'банан', 'вишня']
#
text = input("Введи числа через пробел: ")   # например: 5 10 15 20
parts = text.split()                          # ['5', '10', '15', '20']
numbers = []
for p in parts:
    numbers.append(int(p))
print(numbers)     # [5, 10, 15, 20]