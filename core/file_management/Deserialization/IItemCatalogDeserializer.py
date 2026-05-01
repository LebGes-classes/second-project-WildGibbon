from HomeWork.ItemCatalog.ItemCatalog import ItemCatalog

from abc import ABC, abstractmethod


class IItemCatalogDeserializer(ABC):
    """
    Абстрактный базовый класс для десериализации каталога товаров.
    """
    @abstractmethod
    def deserialize(self, file_path: str) -> ItemCatalog:
        """
        Абстрактный метод для десериализации каталога товаров из файла.

        Args:
            file_path (str): Путь к файлу для десериализации.
        """
        pass
