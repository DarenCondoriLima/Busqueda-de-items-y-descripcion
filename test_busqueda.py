import unittest

from busqueda import buscar_items, buscar_items_y_descripcion, search_items_by_description


ITEMS = [
    {"item": "Manzana", "description": "Fruta roja y dulce"},
    {"item": "Pan", "description": "Producto de harina"},
    {"item": "Queso", "description": "Lácteo curado"},
]


class BusquedaItemsTests(unittest.TestCase):
    def test_busca_por_nombre(self) -> None:
        resultado = buscar_items(ITEMS, "pan")
        self.assertEqual(resultado, [ITEMS[1]])

    def test_busca_por_descripcion(self) -> None:
        resultado = buscar_items(ITEMS, "fruta")
        self.assertEqual(resultado, [ITEMS[0]])

    def test_busqueda_sin_acentos(self) -> None:
        resultado = buscar_items(ITEMS, "lacteo")
        self.assertEqual(resultado, [ITEMS[2]])

    def test_termino_vacio_retorna_todo(self) -> None:
        resultado = buscar_items(ITEMS, " ")
        self.assertEqual(resultado, ITEMS)

    def test_aliases(self) -> None:
        self.assertEqual(buscar_items_y_descripcion(ITEMS, "pan"), [ITEMS[1]])
        self.assertEqual(search_items_by_description(ITEMS, "pan"), [ITEMS[1]])


if __name__ == "__main__":
    unittest.main()
