import logging

logging.basicConfig(level=logging.INFO, filename="src/loger.txt", filemode="w", format="%(asctime)s %(levelname)s %(message)s")
logger = logging.getLogger()
