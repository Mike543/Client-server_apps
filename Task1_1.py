"""1. Каждое из слов «разработка», «сокет», «декоратор» представить в строковом формате
и проверить тип и содержание соответствующих переменных. Затем с помощью онлайн-конвертера
преобразовать строковые представление в формат Unicode и также проверить тип и содержимое переменных."""

development = 'разработка'
socket = 'сокет'
decorator = 'декоратор'

print(development, socket, decorator)
print(type(development), type(socket), type(decorator))


development_u = '\u0440\u0430\u0437\u0440\u0430\u0431\u043e\u0442\u043a\u0430'
socket_u = '\u0441\u043e\u043a\u0435\u0442'
decorator_u = '\u0434\u0435\u043a\u043e\u0440\u0430\u0442\u043e\u0440'
print(development_u, socket_u, decorator_u)
print(type(development_u), type(socket_u), type(decorator_u))


