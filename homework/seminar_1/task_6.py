def sum_numbers(numbers):
    n1 = numbers % 10
    n2 = (numbers % 100) // 10
    n3 = numbers // 100
    return n1 + n2 + n3

bilet = input("Введите шестизначный номер билета: ")
if 5 < len(bilet):
    bilet = int(bilet)
    bilet_right = bilet % 1000
    bilet_left = bilet // 1000
    if bilet_left == bilet_right:
        print("Ура! Билет выйграл!")
    else:
        print("Билет проиграл!")
else:
    print("Вы ввели не шестизначное число")