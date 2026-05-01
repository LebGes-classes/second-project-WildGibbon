from HomeWork.Item.Item import Item

from abc import ABC, abstractmethod


class IItemMenu(ABC):
    """
    Абстрактный базовый класс для меню управления товаром.
    """
    @abstractmethod
    def open(self, item: Item) -> None:
        """
        Абстрактный метод для открытия меню для указанного товара.
        """
        pass
