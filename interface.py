from argparse_web import args
from parsing.HTMLParser import HTMLParser
from parsing.PDFParser import PDFParser
from parsing.parser import Parser
from validator.validator import validate_links, check_file_exists, is_valid_url
from saver.saver import save_to_file
from logger.logger_configuration import logger


class Interface:

    def run(self):
        print('Вітаємо!')
        while True:
            try:
                print('Оберіть, що будемо парсити: (1 - сайт, 2 - PDF документ, 3 - вихід): ')
                command = input()
                if command == "1":
                    html_args = self._add_HTML_args()
                    do_parse = HTMLParser(html_args)
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
        if args.url:
            url = args.url
        else:
            print("Введіть посилання, наприклад: 'https://www.google.com': ")
            url = input()
        while not is_valid_url(url):
            print("Введене послилання невалідне, спробуйте запис наприклад: 'https://www.google.com': ")
            url = input()
            is_valid_url(url)
        return url

    def _add_PDF_args(self):
        if args.pdf:
            file_path = args.pdf
        else:
            print("Введіть шлях до файлу, наприклад: 'src/links.pdf': ")
            file_path = input()
        while not check_file_exists(file_path):
            print("Введений файл не існує, спробуйте запис наприклад: 'src/links.pdf': ")
            file_path = input()
        return file_path

    def _get_result(self, do_parse: Parser):
        links = do_parse.get_links()
        result = validate_links(links)
        save_to_file(*result)
        logger.info("Записано всі валідні лінки у файл 'valid_links.txt'")
        logger.info("Записано всі не валідні лінки у файл 'broken_links.txt'")
