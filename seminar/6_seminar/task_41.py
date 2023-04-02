# Дан массив, состоящий из целых чисел. Напишите
# программу, которая в данном массиве определит
# количество элементов, у которых оба соседних элемента меньше данного.
import random
def generate_array_random():
    array = []
    min_number = int(input("Min number array:"))
    max_number = int(input("Max number array:"))
    size = int(input("Size array:"))
    for i in range(size):
        array.append(random.randint(min_number, max_number))
    return array

array_1 = generate_array_random()
print(array_1)
def sort_list(list):
    count = 0
    for i in range(1, len(list) - 1):
        if list[i - 1] < list[i] > list[i + 1]:
            count += 1
    return count

print(sort_list(array_1))
