"""

Створити програму яка парсить HTML сторінку
залежно від параметрів виклику, виклик формату:
python main.py -url www.google.com
Якщо не вказано шлях зробити запит у користувача
Перевірка чи валідна лінка
Знайти всі лінки на сторінці
(Перевірити що лінка валідна requests.get
(status code == 200))
Посилання у яких статус код 200 зберегти в окремий файл,
всі інші у файл з назвою broken_links.txt
Окремий репозиторій, посилання на нього мені в приват.
(Частину роботи ми виконали на уроці 12)

"""
from interface import Interface
from logger.logger_configuration import logger


if __name__ == "__main__":
    try:
        parsing_session = Interface()
        parsing_session.run()
    except Exception as error:
        logger.critical(error)
