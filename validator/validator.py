import urllib
import requests
from urllib.parse import urlparse
from logger.logger_configuration import logger
import os


def get_valid_url(url):
    if not url.startswith('http://') and not url.startswith('https://'):
        url = 'http://' + url
    return url


def validate_links(links):
    valid_links = []
    broken_links = []

    for link in links:
        link = get_valid_url(link)
        if urlparse(link).netloc:
            try:
                response = requests.get(link)
                if response.status_code == 200:
                    valid_links.append(link)
                    logger.info('Валідна лінка: %s', link)
                else:
                    broken_links.append(link)
                    logger.warning('Не валідна лінка: %s', link)
            except:
                broken_links.append(link)
                logger.error('Неочікувана помилка, лінка не валідна: %s', link)
    return valid_links, broken_links


def check_file_exists(file_path):
    return os.path.isfile(file_path)


def is_valid_url(url: str):
    parsed_url = urllib.parse.urlparse(url)
    return all([parsed_url.scheme, parsed_url.netloc])