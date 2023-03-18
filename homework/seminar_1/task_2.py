numbers = input("Введите трехзначное число - ")
if 2 != len(numbers):
    numbers = int(numbers)
    number_copy = numbers
    n1 = numbers % 10
    n2 = (numbers % 100) // 10
    n3 = numbers // 100
    result = n1 + n2 + n3
    print(number_copy, "->", result, "(", n3, "+", n2, "+", n1, ")")
else:
    print("Вы ввели не трехзначное число")