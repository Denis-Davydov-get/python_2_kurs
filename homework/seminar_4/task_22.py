# Задача 22: Даны два неупорядоченных набора целых чисел
# (может быть, с повторениями). Выдать без повторений в порядке возрастания все те числа,
# которые встречаются в обоих наборах.
# Пользователь вводит 2 числа.
# n - кол-во элементов первого множества.
# m - кол-во элементов второго множества.
# Затем пользователь вводит сами элементы множеств.
def generate_array(x):
    array = set()
    while x > 0:
        number = int(input("Введите номер для множества : "))
        array.add(number)
        x -= 1
    return array

n = int(input("Количество элементов списка n: "))
m = int(input("количество элемнетов списка m: "))
array_n = generate_array(n)
array_m = generate_array(m)

result_array = set()
for i in array_n:
    for j in array_m:
        if i == j:
            result_array.add(i)
print(f"Множество m", array_m)
print(f"Множество n", array_n)
print(sorted(result_array))
