import pytest
from parsing.PDFParser import PDFParser
from parsing.HTMLParser import HTMLParser
from tests.src.data import pdf_path, url


@pytest.fixture
def pdf_parser():
    return PDFParser(pdf_path)


@pytest.fixture
def html_parser():
    return HTMLParser(url)
