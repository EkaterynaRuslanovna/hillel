import json
from parsing_links.argparse_web import args
from parsing_links.parsing.HTMLParser import HTMLParser
from parsing_links.parsing.PDFParser import PDFParser
from parsing_links.parsing.parser import Parser
from parsing_links.validator.validator import get_valid_url, validate_links
from saver.saver import save_to_file
from parsing_links.logger.logger_configuration import logger


class Interface:

    def run(self):
        print('Вітаємо!')
        while True:
            try:
                command = input(
                    'Оберіть, що будемо парсити: (1 - сайт, 2 - PDF документ, 3 - вихід): ')
                if command == "1":
                    html_args = self._add_HTML_args()
                    do_parse = HTMLParser(*html_args)
                    self._get_result(do_parse)
                    print("Лінки успішно записані")
                elif command == "2":
                    pdf_args = self._add_PDF_args()
                    do_parse = PDFParser(pdf_args)
                    self._get_result(do_parse)
                    print("Лінки успішно записані")
                elif command == "3":
                    print("Дякуємо, що обрали нас! До зустрічі:)")
                    break
                else:
                    print('Немає такої опції. Попробуйте знову.')
            except Exception as error:
                logger.critical(error)

    def _add_HTML_args(self):
        url = args.url or input("Введіть посилання, наприклад: 'https://www.google.com': ")
        while not get_valid_url(url):
            url = args.url or input(
                "Введене послилання невалідне, спробуйте запис наприклад: 'https://www.google.com': ")
        endpoint = args.endpoint or input("Введіть ендпоінт, наприклад: '/search': ")
        params_input = args.params or input("Введіть параметр, наприклад: {\"q\": \"Hillel\"} (JSON format): ")
        params = json.loads(params_input) if params_input else {}
        return url, endpoint, params

    def _add_PDF_args(self):
        file_path = args.pdf or input("Введіть шлях до файлу, наприклад: 'files/links.pdf': ")
        return file_path

    def _get_result(self, do_parse: Parser):
        links = do_parse.get_links()
        result = validate_links(links)
        save_to_file(*result)
        logger.info("Записано всі валідні лінки у файл 'valid_links.txt'")
        logger.info("Записано всі не валідні лінки у файл 'broken_links.txt'")
