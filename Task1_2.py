"""2. Каждое из слов «class», «function», «method» записать в байтовом типе без
преобразования в последовательность кодов (не используя методы encode и decode)
и определить тип, содержимое и длину соответствующих переменных."""

clas = b'class'
funct = b'function'
meth = b'method'

print(type(clas), type(funct), type(meth))
print(clas, funct, meth)
print(len(clas), len(funct), len(meth))


