import urllib
from urllib.parse import urljoin
import requests
from parsing_links.argparse_web import args


def is_valid_url(url: str):
    parsed_url = urllib.parse.urlparse(url)
    return all([parsed_url.scheme, parsed_url.netloc])


def format_link(link: str, url: str):
    if link.startswith("/url?q="):
        link = link[7:]
    if link.startswith("/"):
        link = urljoin(url, link)
    return link


def validate_links(links: list, url: str = args.url):
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
