import requests
from bs4 import BeautifulSoup
from parsing.parser import Parser
from logger.logger_configuration import logger


class HTMLParser(Parser):

    def __init__(self, url: str):
        self.url = url

    def get_links(self):
        response = self._get_response()
        if response.status_code == 200:
            logger.info("Отримано всі лінки з посилання")
            return self._parse(response)
        return []

    def _get_response(self):
        response = requests.get(self.url)
        return response

    def _parse(self, response: requests.models.Response):
        html_parser = BeautifulSoup(response.text, "html.parser")
        links = []
        for link in html_parser.find_all('a'):
            href_attribute = link.get("href")
            if href_attribute:
                links.append(href_attribute)
        return links
