from random import randint
size = randint(6, 10)
bushes = [randint(1, 10) for _ in range(size)]
print(bushes)

max_blueberries = bushes[-1] + bushes[-2] + bushes[0]
sum_tree_bushes = max_blueberries

for i in range(size - 1):
    sum_tree_bushes = bushes[i] + bushes[i - 1] + bushes[i + 1]
    if sum_tree_bushes > max_blueberries:
        max_blueberries = sum_tree_bushes
    print(max_blueberries)
