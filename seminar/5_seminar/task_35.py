# Дано натуральное число 
# . Выведите все числа от 1 до n
def fun(n):
    if n != 1: 
        fun(n - 1)
    print(n+1)
n = int(input("input number: "))
fun(n)