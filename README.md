# Busqueda-de-items-y-descripcion

Implementa búsqueda de items por nombre o descripción, sin diferenciar mayúsculas/minúsculas ni acentos.

## Uso rápido

```python
from busqueda import buscar_items

items = [
    {"item": "Manzana", "description": "Fruta roja y dulce"},
    {"item": "Pan", "description": "Producto de harina"},
]

print(buscar_items(items, "fruta"))
```