orbits = [(1, 3), (2.5, 10), (7, 2), (6, 6), (4, 3)]

orbits_exceptions = [(a, b) for (a, b) in orbits if a != b] #все кроме одинаковых
spase = [a*b for (a,b) in orbits_exceptions] # перемножаем оставшиеся из списка друг на друга
print(orbits_exceptions [spase.index(max(spase))]) #выводим индекс максимального значения из перемноженного списка
