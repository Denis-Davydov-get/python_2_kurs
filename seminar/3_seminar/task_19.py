# Дана последовательность из N целых чисел и число
# K. Необходимо сдвинуть всю последовательность
# (сдвиг - циклический) на K элементов вправо, K –
# положительное число.
# Input: [1, 2, 3, 4, 5] k = 3
# Output: [4, 5, 1, 2, 3]
# list = [1, 2, 3, 4, 5]
# k = int(input("Введите число на которое нужно сдвинуть список:"))
# print(list[k:] + list[:k])

list_1 = [1, 2, 3, 4, 5]
k = int(input("Введите число на которое нужно сдвинуть список:")) % len(list_1)

for i in range(k):
    num = list_1.pop(-1)
    list_1.insert(0, num)
print(list_1)