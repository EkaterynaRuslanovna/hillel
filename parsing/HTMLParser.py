import requests
from bs4 import BeautifulSoup
from parsing.parser import Parser
from logger.logger_configuration import logger


class HTMLParser(Parser):

    def __init__(self, url: str):
        self.url = url

    def get_links(self):
        try:
            response = self._get_response()
            if response.status_code == 200:
                logger.info("Got all the links from the link")
                return self._parse(response)
        except requests.exceptions.RequestException as error:
            logger.error(f"Error executing the request: {str(error)}")
        return []

    def _get_response(self):
        try:
            response = requests.get(self.url)
            return response
        except requests.exceptions.RequestException as error:
            logger.error(f"Error executing the request: {str(error)}")
            raise requests.exceptions.RequestException(str(error))

    def _parse(self, response: requests.models.Response):
        try:
            html_parser = BeautifulSoup(response.text, "html.parser")
            links = []
            for link in html_parser.find_all('a'):
                href_attribute = link.get("href")
                if href_attribute:
                    links.append(href_attribute)
            return links
        except Exception as error:
            logger.error(f"HTML parsing error: {str(error)}")
            return []
