import os
import pytest
from saver.saver import save_to_file


@pytest.fixture
def valid_links():
    return ['https://www.google.com', 'https://jobs.dou.ua/']


@pytest.fixture
def invalid_links():
    return ['https://www.invalidlink.com', 'https://www.google', 'https://www.googlecom', 'https://www.google.com', 'https://google.com', 'www.google.com' ]


class TestSaver:

    def test_save_to_file(self, valid_links, invalid_links):
        """
        Перевіряємо, що шлях файлів існує та функція save_to_file() записує у них лінки
        :param valid_links: list (список з валідними лінками)
        :param invalid_links: list (список з не валідними лінками)
        :return: у файл "valid_links.txt" записуються валідні лінки, у файл "broken_links.txt" записуються не валідні лінки
        """
        save_to_file(valid_links, invalid_links)

        directory = os.path.dirname(os.path.abspath(__file__))
        valid_file_path = os.path.join(directory, "..", "saver", "files", "valid_links.txt")
        invalid_file_path = os.path.join(directory, "..", "saver", "files", "broken_links.txt")

        assert os.path.exists(valid_file_path)
        assert os.path.exists(invalid_file_path)

        with open(valid_file_path, "r", encoding="utf-8") as valid_file:
            saved_valid_links = valid_file.read().splitlines()
            assert saved_valid_links == valid_links

        with open(invalid_file_path, "r", encoding="utf-8") as invalid_file:
            saved_invalid_links = invalid_file.read().splitlines()
            assert saved_invalid_links == invalid_links
