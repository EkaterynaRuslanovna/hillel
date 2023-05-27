from urllib.parse import urljoin
import requests
from bs4 import BeautifulSoup


def get_response(url: str, endpoint: str = "", params=None):
    if params is None:
        params = {}
    response = requests.get(url + endpoint, params)
    if response.status_code == 200:
        return response


def parse_html(response: requests.models.Response):
    html_parser = BeautifulSoup(response.text, "html.parser")
    links = []
    for link in html_parser.find_all('a'):
        href_attribute = link.get("href")
        if href_attribute:
            links.append(href_attribute)
    return links


def format_link(link: str, url: str):
    if link.startswith("/url?q="):
        link = link[7:]
    if link.startswith("/"):
        link = urljoin(url, link)
    return link


def validate_links(links: list, url: str):
    valid_links = []
    invalid_links = []
    for link in links:
        link = format_link(link, url)
        response = requests.get(link)
        if response.status_code == 200:
            valid_links.append(link)
        else:
            invalid_links.append(link)
    return valid_links, invalid_links


def save_to_file(valid_links: list, invalid_links: list):
    with open("valid_links.txt", "w", encoding="utf-8") as valid_file:
        valid_file.write("\n".join(valid_links))

    with open("broken_links.txt", "w", encoding="utf-8") as invalid_file:
        invalid_file.write("\n".join(invalid_links))
    print("Лінки успішно провалідовані")


def main(url: str, endpoint: str = "", params=None):
    print("Будь ласка, зачекайте. (Асинхронність і потоки не вийшло реалізувати на даному етапі :( ...)")
    response = get_response(url, endpoint, params)
    links = parse_html(response)
    valid_links, invalid_links = validate_links(links, url)
    save_to_file(valid_links, invalid_links)
