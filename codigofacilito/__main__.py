import logging

from codigofacilito import unreleased

"""
INFO -> 10
DEBUG -> 20
WARNING -> 30
ERROR -> 40
CRITICAL -> 50
"""

logging.basicConfig(level=logging.INFO)

# Ejecuta todo lo del bloque sí y solo sí, este archivo se ejecuta como principal.
if __name__ == '__main__':
    logging.debug('>>> Estamos comenzando la ejecución del paquete.')
    
    workshops = unreleased()
    # logging.debug(help(unreleased))
    
    logging.debug('>>> Estamos finalizando la ejecución del paquete.')