import requests
from urllib.parse import urlparse


def get_valid_url(url):
    if not url.startswith('http://') and not url.startswith('https://'):
        url = 'http://' + url
    return url


def validate_links(links):
    valid_links = []
    broken_links = []

    for link in links:
        link = get_valid_url(link)
        if urlparse(link).netloc:
            try:
                response = requests.get(link)
                if response.status_code == 200:
                    valid_links.append(link)
                    # logging.info('Valid link: %s', link)
                else:
                    broken_links.append(link)
                    # logging.warning('Broken link: %s', link)
            except:
                broken_links.append(link)
                # logging.error('Error occurred while checking link: %s', link)

    return valid_links, broken_links
