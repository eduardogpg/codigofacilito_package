import requests


def unreleased():
    """Retorna los próximos talleres en CódigoFacilito.

    >>> type(unreleased()) == type(list())
    True
    """
    response = requests.get('https://codigofacilito.com/api/v2/workshops/unreleased')

    if response.status_code == 200:
        payload = response.json()
        workshops = payload['data']['workshops']

        # Flat workshops
        return [item["workshop"] for item in workshops]


def released():
    """Retorna los talleres ya realizados en CódigoFacilito.

    >>> type(released()) == type(list())
    True
    """
    response = requests.get('https://codigofacilito.com/api/v2/workshops')

    if response.status_code == 200:
        payload = response.json()
        return payload['data']
