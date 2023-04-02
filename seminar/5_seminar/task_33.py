# Хакер Василий получил доступ к классному журналу и
# хочет заменить все свои минимальные оценки на
# максимальные. Напишите программу, которая
# заменяет оценки Василия, но наоборот: все
# максимальные – на минимальные.
# Input: 5 -> 1 3 3 3 4
# Output: 1 3 3 3 1

from random import randint
def generate_list(n):
    list = []
    for i in range(n):
        list.append(randint(0, n))
    return list
def main(list):
    list_negative = []
    for i in list:
        if i > 3:
            i = 1
            list_negative.append(i)
        else:
            list_negative.append(i)
    return list_negative

x = int(input("Введите размер списка: "))
list = generate_list(x)
print(list)
print(main(list))