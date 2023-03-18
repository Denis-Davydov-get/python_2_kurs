k = int(input('Выберите количество долек: '))
n = int(input('Выберите 1-ю сторону: '))
m = int(input('Выберите 2-ю сторону: '))
if k % n == 0 or k % m == 0:
    print('Yes')
else:
    print('No')