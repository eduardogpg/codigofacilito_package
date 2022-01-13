import requests


def articles():
    """Retorna los artículos en CódigoFacilito.

    >>> type(articles()) == type(list())
    True
    """
    response = requests.get('https://codigofacilito.com/api/v2/articles')

    if response.status_code == 200:
        payload = response.json()
        return payload['data']['articles']
