from argparse_web import args
from parsing.HTMLParser import HTMLParser
from parsing.PDFParser import PDFParser
from parsing.parser import Parser
from validator.validator import validate_links, check_file_exists, is_valid_url
from saver.saver import save_to_file
from logger.logger_configuration import logger


class Interface:

    def run(self):
        print('Welcome!')
        while True:
            try:
                print('Choose what you want to parse: (1 - site, 2 - PDF document, 3 - exit):')
                command = input()
                if command == "1":
                    html_args = self._add_HTML_args()
                    do_parse = HTMLParser(html_args)
                    self._get_result(do_parse)
                    print("Links have been saved successfully")
                elif command == "2":
                    pdf_args = self._add_PDF_args()
                    do_parse = PDFParser(pdf_args)
                    self._get_result(do_parse)
                    print("Links have been saved successfully")
                elif command == "3":
                    print("Thank you for choosing us! Bye:)")
                    break
                else:
                    print('There is no such option. Try again.')
            except Exception as error:
                logger.critical(error)

    def _add_HTML_args(self):
        if args.url:
            url = args.url
        else:
            print("Enter the link, for example: 'https://www.google.com':")
            url = input()
        while not is_valid_url(url):
            print("The entered link is invalid, try an entry for example: 'https://www.google.com':")
            url = input()
            is_valid_url(url)
        return url

    def _add_PDF_args(self):
        if args.pdf:
            file_path = args.pdf
        else:
            print("Enter the file path, for example: 'src/links.pdf':")
            file_path = input()
        while not check_file_exists(file_path):
            print("The entered file does not exist, try writing for example: 'src/links.pdf':")
            file_path = input()
        return file_path

    def _get_result(self, do_parse: Parser):
        links = do_parse.get_links()
        result = validate_links(links)
        save_to_file(*result)
        logger.info("All valid links are recorded in the file 'valid_links.txt'")
        logger.info("Written all invalid links in the file 'broken_links.txt'")
