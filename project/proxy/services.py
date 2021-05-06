import requests
from bs4 import BeautifulSoup
from urllib.parse import urlparse
from django.conf import settings


def inject_prepositions_to_text(input_text):
    """Inject preposition to all six letters words."""
    for word in set(input_text.split(' ')):
        if len(word) == 6:
            input_text = input_text.replace(word, word + settings.PREPOSITION)
            continue
    return input_text


def is_valid_text_elem(elem):
    """Check valid text element."""
    return elem.string and elem.string.strip() and elem.parent.name not in ('script', 'style')


def is_target_link(url):
    """Check is target link."""
    return 'habr' in url


def get_edited_html(path, *args, **kwargs):
    """Get edited habr article html."""
    html_data = requests.get(f'{settings.TARGET_SITE}{path}').text
    soup = BeautifulSoup(html_data, 'html.parser')
    text_elements = soup.find_all(text=True)
    for elem in text_elements:
        if is_valid_text_elem(elem):
            elem.string.replace_with(inject_prepositions_to_text(elem.string))

    links = soup.find_all('a', href=True)
    for link in links:
        target_link = link.get('href')
        if target_link and is_target_link(target_link):
            path = urlparse(target_link).path
            link['href'] = f'{settings.MAIN_URL}{path}'

    return soup.html
