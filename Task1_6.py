"""6. Создать текстовый файл test_file.txt, заполнить его тремя строками:
«сетевое программирование», «сокет», «декоратор». Проверить кодировку файла
по умолчанию. Принудительно открыть файл в формате Unicode и вывести его содержимое."""
import locale

test_string = ['сетевое программирование', 'сокет', 'декоратор']

with open('test_file.txt', 'w+') as f_n:
    for i in test_string:
        f_n.write(i + '\n')
    f_n.seek(0)

print(f_n)

file_coding = locale.getpreferredencoding()

with open('test_file.txt', 'r', encoding=file_coding) as f_n:
    for i in f_n:
        print(i)

    f_n.seek(0)