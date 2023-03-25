def fbnci(fin):
    if fin == 1 or fin == 0:
        return 1
    return fbnci(fin - 1) + fbnci(fin - 2)

numbers = int(input("Inter number: "))
print(fbnci(numbers))