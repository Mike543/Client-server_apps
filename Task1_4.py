"""4. Преобразовать слова «разработка», «администрирование», «protocol», «standard»
из строкового представления в байтовое и выполнить обратное преобразование
(используя методы encode и decode)."""

development = "разработка".encode('utf-8')
administration = "администрирование".encode('utf-8')
protocol = "protocol".encode('utf-8')
standard = "standard".encode('utf-8')
print(development, '\n', administration, '\n', protocol, '\n', standard)
development_d = development.decode('utf-8')
administration_d = administration.decode('utf-8')
protocol_d = protocol.decode('utf-8')
standard_d = standard.decode('utf-8')
print(development_d, administration_d, protocol_d, standard_d)
