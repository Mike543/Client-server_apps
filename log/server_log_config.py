import logging

LEVEL = logging.DEBUG

SERVER_LOGGER = logging.getLogger('server')

FILE_HANDLER = logging.FileHandler("server.log", encoding='utf-8')
FILE_HANDLER.setLevel(LEVEL)

FORMATTER = logging.Formatter("%(asctime)s | %(levelname)-8s | %(module)-12s | %(message)s ")
FILE_HANDLER.setFormatter(FORMATTER)

SERVER_LOGGER.addHandler(FILE_HANDLER)
SERVER_LOGGER.setLevel(LEVEL)



# SERVER_LOGGER.critical('critical')