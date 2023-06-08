import logging

logging.basicConfig(level=logging.INFO, filename="files/loger.log", filemode="w", format="%(asctime)s %(levelname)s %(message)s")
logger = logging.getLogger()

# logger.debug("debug")
# logger.info("info")
# logger.warning("warning")
# logger.error("error")
# logger.critical("critical")
