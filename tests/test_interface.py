from unittest.mock import patch
from io import StringIO


def test_welcome_message(interface):
    """
    Перевіряємо вітальне повідомлення при запуску програми
    :param interface: екземпляр класу Interface
    :return: "Вітаємо!"
    """
    with patch('sys.stdout', new=StringIO()) as output:
        user_input = '3\n'
        with patch('builtins.input', side_effect=user_input.split()):
            interface.run()
        expected_output = "Вітаємо!"
        assert expected_output in output.getvalue().strip()


def test_options(interface):
    """
    Перевіряємо, що виводиться повідомлення з вибором опцій
    :param interface: екземпляр класу Interface
    :return: "Оберіть, що будемо парсити: (1 - сайт, 2 - PDF документ, 3 - вихід): "
    """
    with patch('sys.stdout', new=StringIO()) as output:
        user_input = '3\n'
        with patch('builtins.input', side_effect=user_input.split()):
            interface.run()
        expected_output = "Оберіть, що будемо парсити: (1 - сайт, 2 - PDF документ, 3 - вихід): "
        assert expected_output in output.getvalue().strip()


def test_invalid_option(interface):
    """
    Перевіряємо, що при введені невірної опції користувачем, виводиться повідомлення:
    "Немає такої опції. Попробуйте знову."
    :param interface: екземпляр класу Interface
    :return: "Немає такої опції. Попробуйте знову."
    """
    with patch('sys.stdout', new=StringIO()) as output:
        user_input = '4\n3\n'
        with patch('builtins.input', side_effect=user_input.split()):
            interface.run()
        expected_output = "Немає такої опції. Попробуйте знову."
        assert expected_output in output.getvalue().strip()


def test_html_option(interface):
    """
    Перевіряємо, що при виборі опції "1", виводиться повідомлення:
    "Введіть посилання, наприклад: 'https://www.google.com': "
    :param interface: екземпляр класу Interface
    :return: "Введіть посилання, наприклад: 'https://www.google.com': "
    """
    with patch('sys.stdout', new=StringIO()) as output:
        user_input = '1\nhttps://www.google.com\n3\n'
        with patch('builtins.input', side_effect=user_input.split()):
            interface.run()
        expected_output = "Введіть посилання, наприклад: 'https://www.google.com': "
        assert expected_output in output.getvalue().strip()


def test_invalid_html_link(interface):
    """
    Перевіряємо, що введені невірного посилання, виводиться повідомлення:
    "Введене послилання невалідне, спробуйте запис наприклад: 'https://www.google.com': "
    :param interface: екземпляр класу Interface
    :return: "Введіть посилання, наприклад: 'https://www.google.com': "
    """
    with patch('sys.stdout', new=StringIO()) as output:
        user_input = '1\ngoogle\nhttps://www.google.com\n3\n'
        with patch('builtins.input', side_effect=user_input.split()):
            interface.run()
        expected_output = "Введене послилання невалідне, спробуйте запис наприклад: 'https://www.google.com': "
        assert expected_output in output.getvalue().strip()


def test_pdf_option(interface):
    """
    Перевіряємо, що при виборі опції "2", виводиться повідомлення:
    "Введіть шлях до файлу, наприклад: 'src/links.pdf': "
    :param interface: екземпляр класу Interface
    :return: "Введіть шлях до файлу, наприклад: 'src/links.pdf': "
    """
    with patch('sys.stdout', new=StringIO()) as output:
        user_input = '2\nsrc/links.pdf\n3\n'
        with patch('builtins.input', side_effect=user_input.split()):
            interface.run()
        expected_output = "Введіть шлях до файлу, наприклад: 'src/links.pdf': "
        assert expected_output in output.getvalue().strip()


def test_invalid_pdf_path(interface):
    """
    Перевіряємо, що введені невірного шляху до файлу, виводиться повідомлення:
    "Введений файл не існує, спробуйте запис наприклад: 'src/links.pdf': "
    :param interface: екземпляр класу Interface
    :return: "Введений файл не існує, спробуйте запис наприклад: 'src/links.pdf': "
    """
    with patch('sys.stdout', new=StringIO()) as output:
        user_input = '2\ngoogle\nsrc/links.pdf\n3\n'
        with patch('builtins.input', side_effect=user_input.split()):
            interface.run()
        expected_output = "Введений файл не існує, спробуйте запис наприклад: 'src/links.pdf': "
        assert expected_output in output.getvalue().strip()


def test_links_successfully_saved(interface):
    """
    Перевіряємо повідомлення про успішний запис лінок
    :param interface: екземпляр класу Interface
    :return: "Лінки успішно записані"
    """
    with patch('sys.stdout', new=StringIO()) as output:
        user_input = '1\nhttps://www.google.com\n3\n'
        with patch('builtins.input', side_effect=user_input.split()):
            interface.run()
        expected_output = "Лінки успішно записані"
        assert expected_output in output.getvalue().strip()
