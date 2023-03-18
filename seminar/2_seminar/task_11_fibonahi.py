# 0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, 233, 377, 610, 987, 1597, 2584, 4181, 6765, 10946, 17711
n = int(input("Номер элемента ряда Фибоначчи: "))
n1 = 0
n2 = 1
i = 3
number_fibonashi = []
while n2 < n:
    n1 , n2 = n2, n1 + n2
    number_fibonashi.append(n2)
    i+=1
if n2 == n:
    print(number_fibonashi)
    print(i)
else:
    print(-1)

print("Значение этого элемента:", n2)