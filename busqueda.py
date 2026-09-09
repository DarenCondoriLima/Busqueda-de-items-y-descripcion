"""Utilidades para buscar items por nombre y descripción."""

from __future__ import annotations

import unicodedata
from typing import Any, Iterable


def _normalizar_texto(valor: Any) -> str:
    texto = str(valor or "").strip().lower()
    texto = unicodedata.normalize("NFKD", texto)
    return "".join(caracter for caracter in texto if not unicodedata.combining(caracter))


def buscar_items(items: Iterable[dict[str, Any]], termino: str) -> list[dict[str, Any]]:
    """Filtra items cuyo nombre o descripción contienen el término indicado."""
    termino_normalizado = _normalizar_texto(termino)
    if not termino_normalizado:
        return list(items)

    resultados: list[dict[str, Any]] = []
    for item in items:
        nombre = _normalizar_texto(item.get("item") or item.get("nombre"))
        descripcion = _normalizar_texto(item.get("description") or item.get("descripcion"))
        if termino_normalizado in nombre or termino_normalizado in descripcion:
            resultados.append(item)
    return resultados


def buscar_items_y_descripcion(items: Iterable[dict[str, Any]], termino: str) -> list[dict[str, Any]]:
    """Alias en español de `buscar_items`."""
    return buscar_items(items, termino)


def search_items_by_description(items: Iterable[dict[str, Any]], query: str) -> list[dict[str, Any]]:
    """Alias en inglés de `buscar_items`."""
    return buscar_items(items, query)
