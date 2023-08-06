"""
Module logger_configuration

This module provides configuration for the logger used in the application.
"""

import logging

logging.basicConfig(level=logging.INFO,
                    filename="src/loger.txt",
                    filemode="w",
                    format="%(asctime)s %(levelname)s %(message)s")
logger = logging.getLogger()
