from unittest.mock import patch
from io import StringIO
import logging
import pytest


@pytest.mark.required
def test_welcome_message(interface):
    """
    Checking the welcome message when starting the program
    :param interface: instance of the Interface class
    :return: "Welcome!"
    """
    with patch('sys.stdout', new=StringIO()) as output:
        user_input = '3\n'
        with patch('builtins.input', side_effect=user_input.split()):
            interface.run()
        expected_output = "Welcome!"
        logging.info("test_welcome_message")
        assert expected_output in output.getvalue().strip()


@pytest.mark.required
def test_options(interface):
    """
    Checking that the message with the selection of options is displayed
    :param interface: еinstance of the Interface class
    :return: "Choose what you want to parse: (1 - site, 2 - PDF document, 3 - exit):"
    """
    with patch('sys.stdout', new=StringIO()) as output:
        user_input = '3\n'
        with patch('builtins.input', side_effect=user_input.split()):
            interface.run()
        expected_output = "Choose what you want to parse: (1 - site, 2 - PDF document, 3 - exit):"
        logging.info("test_options")
        assert expected_output in output.getvalue().strip()


def test_invalid_option(interface):
    """
    Checking that when the user enters an incorrect option, a message is displayed:
    "There is no such option. Try again."
    :param interface: instance of the Interface class
    :return: "There is no such option. Try again."
    """
    with patch('sys.stdout', new=StringIO()) as output:
        user_input = '4\n3\n'
        with patch('builtins.input', side_effect=user_input.split()):
            interface.run()
        expected_output = "There is no such option. Try again."
        logging.info("test_invalid_option")
        assert expected_output in output.getvalue().strip()


@pytest.mark.required
def test_html_option(interface):
    """
    Checking that when you select option "1", the message is displayed:
    "Enter the link, for example: 'https://www.google.com':"
    :param interface: instance of the Interface class
    :return: "Enter the link, for example: 'https://www.google.com':"
    """
    with patch('sys.stdout', new=StringIO()) as output:
        user_input = '1\nhttps://www.google.com\n3\n'
        with patch('builtins.input', side_effect=user_input.split()):
            interface.run()
        expected_output = "Enter the link, for example: 'https://www.google.com':"
        logging.info("test_html_option")
        assert expected_output in output.getvalue().strip()


def test_invalid_html_link(interface):
    """
    Checking that an incorrect link has been entered, the following message is displayed:
    "The entered link is invalid, try an entry for example: 'https://www.google.com':"
    :param interface: instance of the Interface class
    :return: "The entered link is invalid, try an entry for example: 'https://www.google.com':"
    """
    with patch('sys.stdout', new=StringIO()) as output:
        user_input = '1\ngoogle\nhttps://www.google.com\n3\n'
        with patch('builtins.input', side_effect=user_input.split()):
            interface.run()
        expected_output = "The entered link is invalid, try an entry for example: 'https://www.google.com':"
        logging.info("test_invalid_html_link")
        assert expected_output in output.getvalue().strip()


@pytest.mark.required
def test_pdf_option(interface):
    """
    Checking that when selecting option "2", the message is displayed:
    "Enter the file path, for example: 'src/links.pdf':"
    :param interface: instance of the Interface class
    :return: "Enter the file path, for example: 'src/links.pdf':"
    """
    with patch('sys.stdout', new=StringIO()) as output:
        user_input = '2\nsrc/links.pdf\n3\n'
        with patch('builtins.input', side_effect=user_input.split()):
            interface.run()
        expected_output = "Enter the file path, for example: 'src/links.pdf':"
        logging.info("test_pdf_option")
        assert expected_output in output.getvalue().strip()


def test_invalid_pdf_path(interface):
    """
    Checking that the wrong path to the file is entered, the following message is displayed:
    "The entered file does not exist, try writing for example: 'src/links.pdf':"
    :param interface: instance of the Interface class
    :return: "The entered file does not exist, try writing for example: 'src/links.pdf':"
    """
    with patch('sys.stdout', new=StringIO()) as output:
        user_input = '2\ngoogle\nsrc/links.pdf\n3\n'
        with patch('builtins.input', side_effect=user_input.split()):
            interface.run()
        expected_output = "The entered file does not exist, try writing for example: 'src/links.pdf':"
        logging.info("test_invalid_pdf_path")
        assert expected_output in output.getvalue().strip()


@pytest.mark.required
def test_links_successfully_saved(interface, capsys):
    """
    Checking the message about the successful recording of links
    :param interface: instance of the Interface class
    :param capsys: fixture capsys from pytest
    :return: "Links have been saved successfully"
    """
    user_input = '1\nhttps://www.google.com\n3\n'
    with patch('builtins.input', side_effect=user_input.split()):
        interface.run()

    captured = capsys.readouterr()
    assert "Links have been saved successfully" in captured.out.strip()