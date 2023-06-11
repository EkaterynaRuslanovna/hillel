from validator.validator import get_valid_url, validate_links, check_file_exists, is_valid_url


class TestValidator:

    def test_get_valid_url(self):
        """
        Перевіряємо, що функція додає "http://" до початку URL, якщо він не починається з "http://" або "https://"
        :return: "http://" + url
        """

        url = "google.com"
        expected = "http://google.com"
        assert get_valid_url(url) == expected

    def test_validate_links(self):
        """
        Перевіряємо, що функція правильно розділяє валідні та невалідні посилання
        :return:
        """

        links = ["https://translater.google.com/", "https://uk.lipsum.cor/", "https://www.dyoutuber.com/",
                 "https://medium.com/", "https://www.olx.ua/uk"]
        valid_links, broken_links = validate_links(links)
        expected_valid_links = ["https://medium.com/", "https://www.olx.ua/uk"]
        expected_broken_links = ["https://translater.google.com/", "https://uk.lipsum.cor/", "https://www.dyoutuber.com/"]

        assert valid_links == expected_valid_links
        assert broken_links == expected_broken_links

    def test_check_file_exists(self):
        """
        Перевіряємо, що функція повертає True, якщо файл існує, і False, якщо файл не існує
        :return: True - якщо існує файл, False - якщо не існує файлу
        """

        existing_file = "src/links.pdf"
        assert check_file_exists(existing_file) is True

        non_existing_file = "non_existing_file.txt"
        assert check_file_exists(non_existing_file) is False

    def test_is_valid_url(self):
        """
        Перевіряємо, що функція правильно визначає, чи є URL дійсним
        :return: True - якщо URL є дійсним, False - якщо URL не є дійсним
        """

        valid_url = "https://medium.com/"
        assert is_valid_url(valid_url) is True

        invalid_url = "/medium.com/"
        assert is_valid_url(invalid_url) is False
