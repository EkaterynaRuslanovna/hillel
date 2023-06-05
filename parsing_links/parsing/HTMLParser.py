import requests
from bs4 import BeautifulSoup
from parsing_links.parsing.parser import Parser


class HTMLParser(Parser):

    def __init__(self, url: str, endpoint: str = "", params=None):
        self.url = url
        self.endpoint = endpoint
        self.params = params if params is not None else {}

    def get_links(self):
        response = self._get_response()
        if response.status_code == 200:
            return self._parse(response)
        return []

    def _get_response(self):
        response = requests.get(self.url + self.endpoint, self.params)
        return response

    def _parse(self, response: requests.models.Response):
        html_parser = BeautifulSoup(response.text, "html.parser")
        links = []
        for link in html_parser.find_all('a'):
            href_attribute = link.get("href")
            if href_attribute:
                links.append(href_attribute)
        return links


# a = HTMLParser("https://www.google.com", '/search', {"q": "Hillel"})
# c = a.get_links()
# print(c)
