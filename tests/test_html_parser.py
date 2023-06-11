import pytest
import requests
from parsing.HTMLParser import HTMLParser
from tests.src.data import url


class TestHTMLParser:

    @pytest.fixture
    def html_parser(self):
        return HTMLParser(url)

    def test_get_links_returns_list(self, html_parser):
        """
        Перевіряємо, що функція get_links() вертає список
        :param html_parser: fixture
        :return: type: list
        """

        links = html_parser.get_links()
        assert isinstance(links, list)

    def test_len_list_of_links_more_than_0(self, html_parser):
        """
        Перевіряємо, що список не пустий
        :param html_parser: fixture
        :return: list: len of list more, than 0
        """

        assert len(html_parser.get_links()) > 0

    @pytest.mark.parametrize("url", ["google", "google.com", "www.google.com", "https://www.google.", "http//google.com"])
    def test_invalid_url(self, url):
        """
        Перевіряємо, що при невірному посиланні викликається RequestException
        :param url: str (invalid)
        :return: requests.exceptions.RequestException
        """

        parser = HTMLParser(url)
        parser.get_links()

        with pytest.raises(requests.exceptions.RequestException):
            parser._get_response()
