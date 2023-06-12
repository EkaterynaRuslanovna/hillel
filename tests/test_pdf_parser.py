import logging
import pytest
from parsing.PDFParser import PDFParser


class TestPDFParser:

    @pytest.mark.required
    def test_get_links_returns_list(self, pdf_parser):
        """
        Перевіряємо, що функція get_links() вертає список
        :param pdf_parser: fixture
        :return: type: list
        """

        links = pdf_parser.get_links()
        assert isinstance(links, list)
        logging.info("test_get_links_returns_list")

    def test_len_list_of_links_more_than_0(self, pdf_parser):
        """
        Перевіряємо, що список не пустий
        :param pdf_parser: fixture
        :return: len of list more, than 0
        """

        assert len(pdf_parser.get_links()) > 0
        logging.info("test_len_list_of_links_more_than_0")

    @pytest.mark.required
    def test_get_links_with_exception(self):
        """
        Перевіряємо, що при невірному шляху до файлу викликається FileNotFoundError
        :return: FileNotFoundError
        """

        pdf_parser = PDFParser("/path/to/nonexistent.pdf")

        with pytest.raises(FileNotFoundError):
            pdf_parser.get_links()

        logging.info("test_get_links_with_exception")