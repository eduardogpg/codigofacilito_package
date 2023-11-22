# CodigoFacilito Package

Este paquete nos permite consumir el API de la plataforma [Código Facilito](https://codigofacilito.com/). 🐍

<h1 align="center">
<img src="https://codigofacilito.com/assets/bootcamps/preventa/cody-68f959121284c893ffca099008f2fe4c99c33f332d1de5f040250e59c489b68d.png" width="200">
</h1><br>

[![PyPI Downloads](https://img.shields.io/pypi/dm/codigofacilito.svg?label=PyPI%20downloads)](https://pypi.org/project/codigofacilito/)


- **Source code:** https://github.com/Ange1D/codigofacilito_package
- **Bug reports:** https://github.com/Ange1D/codigofacilito_package/issues

## Características

- Retornar los artículos de CódigoFacilito
- Retornar los workshops
- Retornar los workshops que aun no se han lanzado


## Instalación
```sh
pip install codigofacilito
```

## Uso:
```python
from codigofacilito.articles import articles

articles = articles()
print(articles)
```
Output `Retorna los articulos`

```python
from codigofacilito.workshops import released

workshops = released()
print(workshops)
```
Output `Retorna los workshops`

```python
from codigofacilito.workshops import unreleased

workshops = unreleased()
print(workshops)
```
Output `Retorna los workshops que aun no se han lanzado`

## CLI

| Comando | Descripción | 
| ------------------------ | ------------------------ | 
| pycody --items articles | Retorna los articulos |
| pycody --items workshops | Retorna los workshops |
| pycody --items workshops --unreleased | Retorna los workshops que aun no se han lanzado|



## Testing:
    import codigofacilito
    help(codigofacilito.released)
    help(codigofacilito.unreleased)
    help(codigofacilito.unreleased)

## License

[MIT](https://github.com/Ange1D/codigofacilito_package/blob/master/LICENSE.txt)
