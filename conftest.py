import pytest

url = "https://www.lamoda.ru/"


@pytest.fixture(scope='session')
def base_url(url):
    return url
