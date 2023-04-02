def len_letters(text):
    text = text.replace(' ', '-').split()
    list_1 = []
    for word in text:
        sum_letters = 0
        for i in word:
            if i in 'аеёиоуыэюя':
                sum_letters += 1
        list_1.append(sum_letters)
    return len(list_1) == list_1.count(list_1[0])


text = input("Введите текст для проверки рифмы: ")

if len_letters(text):
    print(text)
    print('Парам пам-пам')
else:
    print(text)
    print('Пам парам')

