"""

Створити програму яка парсить HTML сторінку залежно від параметрів виклику, виклик формату:
python main.py -url www.google.com
Якщо не вказано шлях зробити запит у користувача
Перевірка чи валідна лінка
Знайти всі лінки на сторінці(Перевірити що лінка валідна requests.get (status code == 200))
Посилання у яких статус код 200 зберегти в окремий файл, всі інші у файл з назвою broken_links.txt
Окремий репозиторій, посилання на нього мені в приват. (Частину роботи ми виконали на уроці 12)

"""
import json
import urllib.parse
from html_parsing_links.argparse_web import args
from html_parsing_links.html_links import parse_html, get_response, save_to_file, main


def is_valid_url(url: str):
    parsed_url = urllib.parse.urlparse(url)
    return all([parsed_url.scheme, parsed_url.netloc])


if __name__ == "__main__":
    url = args.url or input("Введіть посилання, наприклад: 'https://www.google.com': ")
    while not is_valid_url(url):
        url = args.url or input("Введене послилання невалідне, спробуйте запис наприклад: 'https://www.google.com': ")
    endpoint = args.endpoint or input("Введіть ендпоінт, наприклад: '/search': ")
    params_input = args.params or input("Введіть параметр, наприклад: {\"q\": \"Hillel\"} (JSON format): ")
    params = json.loads(params_input) if params_input else {}

    main(url, endpoint, params)
