import re
import pdfplumber
from parsing_links.parsing.parser import Parser


class PDFParser(Parser):

    def __init__(self, file_path: str):
        self.file_path = file_path

    def get_links(self):
        links = []
        with pdfplumber.open(self.file_path) as pdf:
            for page in pdf.pages:
                text = page.extract_text()
                link_pattern = r'(https?://\S+)'
                founded_links = re.findall(link_pattern, text)
                links.extend(founded_links)
        return links


# a = PDFParser("links.pdf")
# c = a.get_links()
# print(c)
