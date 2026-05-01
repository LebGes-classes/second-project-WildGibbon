from HomeWork.ItemCatalog.ItemCatalog import ItemCatalog

from abc import ABC, abstractmethod
from typing import Any


class IItemCatalogSerializer(ABC):
    """
    Абстрактный базовый класс для сериализации каталога товаров.
    """
    @abstractmethod
    def serialize(self, item_catalog: ItemCatalog) -> Any:
        """
        Абстрактный метод для сериализации каталога товаров.

        Args:
            item_catalog (ItemCatalog): Каталог товаров для сериализации.
        """
        pass
