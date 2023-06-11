import argparse

parser = argparse.ArgumentParser(description="Парсінг сайту або PDF для валідації лінок")

parser.add_argument("--url", type=str, required=False, help="Аргумент URL, наприклад: http://www.google.com")
parser.add_argument("--pdf", type=str, required=False, help="Шлях до PDF файлу, наприклад: 'src/links.pdf': ")

args = parser.parse_args()
