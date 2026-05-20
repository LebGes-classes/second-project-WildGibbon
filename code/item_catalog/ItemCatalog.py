from code.item.Product import Product

from typing import List, Tuple


class ItemCatalog:
    """
    Представляет каталог товаров.
    """
    def __init__(self, items: List[Product]) -> None:
        """
        Инициализирует каталог товаров.

        Args:
            items (list[item]): Список товаров для инициализации каталога.
        """
        self.__items = items

    def get_items(self) -> Tuple[Product, ...]:
        """
        Возвращает кортеж всех товаров в каталоге.

        Returns:
            tuple: Кортеж товаров.
        """
        return tuple(self.__items)

    def append(self, item: Product) -> None:
        """
        Добавляет товар в каталог.

        Args:
            item (item): Товар для добавления.
        """
        self.__items.append(item)

    def pop(self, index: int) -> None:
        """
        Удаляет товар из каталога по индексу.

        Args:
            index (int): Индекс товара для удаления.
        """
        self.__items.pop(index)
