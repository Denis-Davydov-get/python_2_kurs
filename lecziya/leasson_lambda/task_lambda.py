# в списке хранятся числа. Нужно выбрать только четные числа и составить список пар(число, квадрат числа)
# input: 1,2,3,5,8,15,23,38
# output[(2,4), (8,64), 38, 1444]
# spisok = [1,2,3,5,8,15,23,38]
# def sort_list(spisok):
#     list_result = list()
#     for i in spisok:
#         if i % 2 == 0:
#             list_result.append((i, i*i))
#     return list_result
# print(sort_list(spisok))
def select(f, col):
    return [f(x) for x in col]

def where(f, col):
    return [x for x in col if f(x)]

spisok = [1,2,3,5,8,15,23,38]
res = select(int, spisok)
print(res)
res = where(lambda x: x % 2 == 0, res)
print(res)