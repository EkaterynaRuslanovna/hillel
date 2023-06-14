import logging
import pytest
from parsing.PDFParser import PDFParser


class TestPDFParser:

    @pytest.mark.required
    def test_get_links_returns_list(self, pdf_parser):
        """
        Checking that the get_links() function returns a list
        :param pdf_parser: fixture
        :return: type: list
        """

        links = pdf_parser.get_links()
        assert isinstance(links, list)
        logging.info("test_get_links_returns_list")

    def test_len_list_of_links_more_than_0(self, pdf_parser):
        """
        Checking that the list is not empty
        :param pdf_parser: fixture
        :return: len of list more, than 0
        """

        assert len(pdf_parser.get_links()) > 0
        logging.info("test_len_list_of_links_more_than_0")

    @pytest.mark.required
    def test_get_links_with_exception(self):
        """
        Checking that a FileNotFoundError is raised if the file path is incorrect
        :return: FileNotFoundError
        """

        pdf_parser = PDFParser("/path/to/nonexistent.pdf")

        with pytest.raises(FileNotFoundError):
            pdf_parser.get_links()

        logging.info("test_get_links_with_exception")
