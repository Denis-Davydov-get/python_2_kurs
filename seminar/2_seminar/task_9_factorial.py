n = int(input("Введите число: "))  # множитель
factorial = 1  # множимое
x = n # copy input
while n > 1:
    factorial *= n #
    n -= 1 # вычесть из множителя  1
print("Факториал введенного числа", x, "-", factorial)
