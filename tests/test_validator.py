import logging
import pytest
from validator.validator import get_valid_url, \
    validate_links, check_file_exists, is_valid_url


class TestValidator:

    def test_get_valid_url(self):
        """
        Checking that the function adds "http://"
        to the beginning of the URL
        if it doesn't start with "http://" or "https://"
        :return: "http://" + url
        """

        url = "google.com"
        expected = "http://google.com"
        assert get_valid_url(url) == expected
        logging.info("test_get_valid_url")

    @pytest.mark.required
    def test_validate_links(self):
        """
        Verifying that the function correctly
        separates valid and invalid references
        :return:
        """

        links = ["https://translater.google.com/",
                 "https://uk.lipsum.cor/",
                 "https://www.dyoutuber.com/",
                 "https://medium.com/",
                 "https://www.olx.ua/uk"]
        valid_links, broken_links = validate_links(links)
        expected_valid_links = ["https://medium.com/",
                                "https://www.olx.ua/uk"]
        expected_broken_links = ["https://translater.google.com/",
                                 "https://uk.lipsum.cor/",
                                 "https://www.dyoutuber.com/"]

        assert valid_links == expected_valid_links
        assert broken_links == expected_broken_links

        logging.info("test_validate_links")

    def test_check_file_exists(self):
        """
        Tests that the function returns True if
        the file exists and False if the file does not exist
        :return: True - if the file exists,
        False - if the file does not exist
        """

        existing_file = "src/links.pdf"
        assert check_file_exists(existing_file) is True

        non_existing_file = "non_existing_file.txt"
        assert check_file_exists(non_existing_file) is False

        logging.info("test_check_file_exists")

    def test_is_valid_url(self):
        """
        Verify that the function correctly
        determines whether the URL is valid
        :return: True - if the URL is valid,
        False - if the URL is not valid
        """

        valid_url = "https://medium.com/"
        assert is_valid_url(valid_url) is True

        invalid_url = "/medium.com/"
        assert is_valid_url(invalid_url) is False

        logging.info("test_is_valid_url")
