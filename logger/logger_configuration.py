import logging

logging.basicConfig(level=logging.INFO, filename="files/loger.txt", filemode="w", format="%(asctime)s %(levelname)s %(message)s")
logger = logging.getLogger()
