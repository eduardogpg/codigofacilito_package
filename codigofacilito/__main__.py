import argparse
import logging
from enum import Enum

from codigofacilito import unreleased, released, articles
from .config import DEBUG

if DEBUG:
    logging.basicConfig(level=logging.DEBUG)
else:
    logging.basicConfig(level=logging.INFO)


class Items(str, Enum):
    WORSHOPS = "workshops"
    ARTICLES = "articles"


item_choices = [tag.value for tag in Items]


def main(*args, **kwargs):
    if kwargs.get("items", None) == Items.WORSHOPS:
        if kwargs.get("unreleased", False):
            logging.info(unreleased())
        else:
            logging.info(released())
    elif kwargs.get("items", None) == Items.ARTICLES:
        logging.info(articles())
    else:
        logging.error("No valid item selected.")


if __name__ == '__main__':
    logging.debug('>>> Estamos comenzando la ejecución del paquete.')

    logging.debug('>>> Procesando argumentos...')

    parser = argparse.ArgumentParser()
    parser.add_argument(
        '--items',
        help='flag to choose between "workshops" or "articles"',
        type=str,
        required=True,
        choices=item_choices
    )
    parser.add_argument(
        '--unreleased',
        help='flag to return unreleased workshops',
        dest='unreleased',
        action='store_true'
    )
    parser.add_argument(
        '--no-unreleased',
        help='flag to return unreleased workshops',
        dest='unreleased',
        action='store_false'
    )
    parser.set_defaults(unreleased=False)

    args = parser.parse_args()

    logging.debug(f'>>> {args}')

    main(items=args.items, unreleased=args.unreleased)

    logging.debug('>>> Estamos finalizando la ejecución del paquete.')
