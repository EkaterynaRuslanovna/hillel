import logging
import os
import pytest
from tests.src.data import data_valid_links, data_invalid_links
from saver.saver import save_to_file


class TestSaver:

    @pytest.mark.required
    def test_save_to_file(self):
        """
        Checking that the file path exists and the save_to_file() function writes links to them
        :param data_valid_links: list (list with valid links)
        :param data_invalid_links: list (list with invalid links)
        :return: valid links are written to the "valid_links.txt" file, invalid links are written to the "broken_links.txt" file
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
