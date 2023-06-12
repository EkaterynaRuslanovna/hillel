import logging
import os
import pytest
from tests.src.data import data_valid_links, data_invalid_links
from saver.saver import save_to_file


class TestSaver:

    @pytest.mark.required
    def test_save_to_file(self):
        """
        Перевіряємо, що шлях файлів існує та функція save_to_file() записує у них лінки
        :param data_valid_links: list (список з валідними лінками)
        :param data_invalid_links: list (список з не валідними лінками)
        :return: у файл "valid_links.txt" записуються валідні лінки, у файл "broken_links.txt" записуються не валідні лінки
        """
        save_to_file(data_valid_links, data_invalid_links)

        directory = os.path.dirname(os.path.abspath(__file__))
        valid_file_path = os.path.join(directory, "..", "src", "valid_links.txt")
        invalid_file_path = os.path.join(directory, "..", "src", "broken_links.txt")

        assert os.path.exists(valid_file_path)
        assert os.path.exists(invalid_file_path)

        with open(valid_file_path, "r", encoding="utf-8") as valid_file:
            saved_valid_links = valid_file.read().splitlines()
            assert saved_valid_links == data_valid_links

        with open(invalid_file_path, "r", encoding="utf-8") as invalid_file:
            saved_invalid_links = invalid_file.read().splitlines()
            assert saved_invalid_links == data_invalid_links

        logging.info("test_save_to_file")
