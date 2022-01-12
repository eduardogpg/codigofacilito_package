import logging

from codigofacilito import unreleased

"""
INFO -> 10
DEBUG -> 20
WARNING -> 30
ERROR -> 40
CRITICAL -> 50
"""

logging.basicConfig(level=logging.WARNING)

if __name__ == '__main__':
    logging.debug('>>> Estamos comenzando la ejecución del paquete.')
    
    workshops = unreleased()
    logging.debug(workshops)
    
    logging.debug('>>> Estamos finalizando la ejecución del paquete.')