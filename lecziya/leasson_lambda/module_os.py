import os
os.chdir('d:/Мой диск/geekbrains/2 курс/seminar/lecziya/leasson_lambda') # сменить текущую директорию
print(os.getcwd()) # узнать текущую директорию
print(os.path.basename('d:/Мой диск/geekbrains/2 курс/seminar/lecziya/leasson_lambda/func_filtr.py'))
# вернет название файла в котором работаем func_filtr.py

print(os.path.abspath('module_os.py')) # вернет путь по которому лежит файл