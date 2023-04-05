# Создать телефонный справочник с возможностью импорта и экспорта данных в формате .txt.
# Фамилия, имя, отчество, номер телефона - данные, которые должны находиться в файле.
# 1. Программа должна выводить данные
# 2. Программа должна сохранять данные в текстовом файле
# 3. Пользователь может ввести одну из характеристик для поиска определенной
# записи(Например имя или фамилию человека)
# 4. Использование функций. Ваша программа не должна быть линейной

PATH_FILE_FIO = r"D:\Мой диск\geekbrains\2 курс\seminar\seminar\8_seminar\fio.txt"
PATH_FILE_PHONE = r"D:\Мой диск\geekbrains\2 курс\seminar\seminar\8_seminar\phone.txt"
PATH_FILE_GENERAL = r"D:\Мой диск\geekbrains\2 курс\seminar\seminar\8_seminar\general.txt"


def write_file():
    with open(PATH_FILE_FIO, 'a', encoding='utf-8') as f:
        f.writelines('\n' + input("Что добавить в ФИО?: "))


print(write_file())


def read_file():
    with open(PATH_FILE_FIO, 'r', encoding='utf-8') as f:
        for line in f:
            print(line.strip())


read_file()


def find_file():
    with open(PATH_FILE_FIO, 'r', encoding='utf-8') as f:
        find = input("Что ищем? ")
        for line in f:
            if find.casefold() in line.casefold():
                print(line)


print(find_file())
