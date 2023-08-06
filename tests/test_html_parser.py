import logging
import pytest
import requests
from parsing.html_parser import HtmlParser
from tests.src.data import invalid_links_list


class TestHTMLParser:

    @pytest.mark.required
    def test_get_links_returns_list(self, html_parser):
        """
        Checking that the get_links() function returns a list
        :param html_parser: fixture
        :return: type: list
        """

        links = html_parser.get_links()
        logging.info("test_get_links_returns_list")
        assert isinstance(links, list)

    def test_len_list_of_links_more_than_0(self, html_parser):
        """
        Checking that the list is not empty
        :param html_parser: fixture
        :return: list: len of list more, than 0
        """

        logging.info("test_len_list_of_links_more_than_0")
        assert len(html_parser.get_links()) > 0

    @pytest.mark.required
    @pytest.mark.parametrize("url", invalid_links_list)
    def test_invalid_url(self, url):
        """
        Checking that a RequestException is thrown if the reference is invalid
        :param url: str (invalid)
        :return: requests.exceptions.RequestException
        """

        parser = HtmlParser(url)
        parser.get_links()

        with pytest.raises(requests.exceptions.RequestException):
            parser._get_response()

        logging.info("test_invalid_url")
