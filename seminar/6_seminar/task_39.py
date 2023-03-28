# Даны два массива чисел. Требуется вывести те элементы
# первого массива (в том порядке, в каком они идут в первом
# массиве), которых нет во втором массиве
import random
def generate_array_random():
    array = []
    start = int(input("min number array:"))
    finish = int(input("max number array:"))
    size = int(input("Size array:"))
    for i in range(size):
        array.append(random.randint(start, finish))
    return array

array_1 = generate_array_random()
array_2 = generate_array_random()

def sort_list(list_1, list_2):
    result_list = []
    for i in list_1:
        if i not in list_2:
            result_list.append(i)
    return result_list

print(array_1)
print(array_2)
print(sort_list(array_1, array_2))
