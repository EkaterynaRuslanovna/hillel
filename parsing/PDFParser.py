import re
import pdfplumber
from parsing.parser import Parser
from logger.logger_configuration import logger


class PDFParser(Parser):

    def __init__(self, file_path: str):
        self.file_path = file_path

    def get_links(self):
        links = []
        with pdfplumber.open(self.file_path) as pdf:
            for page in pdf.pages:
                text = page.extract_text()
                link_pattern = r'(https?://\S+[^\s\"\)\,\.])'
                founded_links = re.findall(link_pattern, text)
                for link in founded_links:
                    if link.count("http") > 1:
                        split_links = link.split("/.")
                        links.extend(split_links)
                    else:
                        links.append(link)
        logger.info("Отримано всі лінки з pdf файлу")
        return links
