PATH_FILE_GENERAL = r"general.txt"

#Добавление с удалением в файл
def change_file():
    with open(PATH_FILE_GENERAL, 'w', encoding='utf-8') as f:
        text = input("Предыдущие записи удалятся. Что добавить?: ")
        f.writelines(text)

#давление данных из пользовательсого ввода в файл фио
def append_in_file():
    with open(PATH_FILE_GENERAL, 'a', encoding='utf-8') as f:
        f.writelines('\n' + input("Напишите ФИО для доваления: "))

#чтение данных из файла фио
def read_file():
    with open(PATH_FILE_GENERAL, 'r', encoding='utf-8') as f:
        for line in f:
            return line.strip()

# поиск данных из пользовательсого ввода в файл фио
def find_file():
    with open(PATH_FILE_GENERAL, 'r', encoding='utf-8') as f:
        find = input("Кого ищем?: ")
        for line in f:
            if find.casefold() in line.casefold():
                return line
            return print("Не нашли такое")
def input_user():
    number = int(input("что вы хотете сделать с файлом? \n\
    1 - прочитать данные с файла\n\
    2 - добавить информацию в файл\n\
    3 - найти что-то в файле\n\
    4 - перезаписать информацию в файле\n\
    Введите цифру: "))

    if number == 1:
        print(read_file())
    elif number == 2:
        print(append_in_file())
    elif number == 3:
        print(find_file())
    elif number == 4:
        print(change_file())
    else:
        print("Вы ввели что-то не так. Попробуйте еще раз.")
        input_user()
input_user()