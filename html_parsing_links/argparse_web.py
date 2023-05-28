import argparse

parser = argparse.ArgumentParser(description="Парсінг сайту")

parser.add_argument("--url", type=str, required=False, help="Аргумент URL, наприклад: http://www.google.com")
parser.add_argument("--endpoint", type=str, required=False, help="Ендпоінт, наприклад: '/search'")
parser.add_argument("--params", type=str, required=False, help="Параметри пошуку (пошуковий запит(JSON format) наприклад: {\"q\": \"Hillel\"})")

args = parser.parse_args()
