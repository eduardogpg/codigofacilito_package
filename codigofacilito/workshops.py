import requests


def unreleased():
    """Retorna los próximos talleres en CódigoFacilito.

    >>> type(unreleased()) == type(list())
    True
    """

    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.76 Safari/537.36', "Upgrade-Insecure-Requests": "1","DNT": "1","Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8","Accept-Language": "en-US,en;q=0.5","Accept-Encoding": "gzip, deflate"}
    response = requests.get('https://codigofacilito.com/api/v2/workshops/unreleased',headers)

    if response.status_code == 200:
        payload = response.json()
        workshops = payload['data']['workshops']

        # Flat workshops
        return [item["workshop"] for item in workshops]
    else:
        return 'Request failed!'


def released():
    """Retorna los talleres ya realizados en CódigoFacilito.

    >>> type(released()) == type(list())
    True
    """
    
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.76 Safari/537.36', "Upgrade-Insecure-Requests": "1","DNT": "1","Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8","Accept-Language": "en-US,en;q=0.5","Accept-Encoding": "gzip, deflate"}
    response = requests.get('https://codigofacilito.com/api/v2/workshops',headers)

    if response.status_code == 200:
        payload = response.json()
        return payload['data']
    else:
        return 'Request failed!'