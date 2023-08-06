import pytest
from parsing.pdf_parser import PdfParser
from parsing.html_parser import HtmlParser
from tests.src.data import pdf_path, url
from interface import Interface


@pytest.fixture
def pdf_parser():
    return PdfParser(pdf_path)


@pytest.fixture
def html_parser():
    return HtmlParser(url)


@pytest.fixture
def interface():
    return Interface()
