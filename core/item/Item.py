from HomeWork.Item.ItemState import ItemState

from typing import Optional


class Item:
    """
    Карточка товара с его атрибутами и методами для управления.
    """

    def __init__(
        self,
        name: str,
        quantity: int,
        state: ItemState,
        supplier: str,
        manufacturer: str,
        price: float,
        location: str,
        city: str,
        product_id: str,
    ) -> None:
        """
        Инициализирует карточку товара.

        Args:
            name (str): Название товара.
            quantity (int): Количество товара.
            state (ItemState): Состояние товара.
            supplier (str): Поставщик товара.
            manufacturer (str): Производитель товара.
            price (float): Цена товара.
            location (str): Местоположение товара.
            city (str): Город товара.
            product_id (str, optional): Уникальный идентификатор товара.
        """

        self.__name = name
        self.__quantity = quantity
        self.__state = state
        self.__supplier = supplier
        self.__manufacturer = manufacturer
        self.__price = price
        self.__location = location
        self.__city = city
        self.__product_id = product_id

    def get_name(self) -> str:
        """
        Возвращает название товара.

        Returns:
            str: Название товара.
        """

        return self.__name

    def get_quantity(self) -> int:
        """
        Возвращает количество товара.

        Returns:
            int: Количество товара.
        """

        return self.__quantity

    def get_state(self) -> ItemState:
        """
        Возвращает состояние товара.

        Returns:
            ItemState: Состояние товара.
        """

        return self.__state

    def get_supplier(self) -> str:
        """
        Возвращает поставщика товара.

        Returns:
            str: Поставщик товара.
        """

        return self.__supplier

    def get_manufacturer(self) -> str:
        """
        Возвращает производителя товара.

        Returns:
            str: Производитель товара.
        """

        return self.__manufacturer

    def get_price(self) -> float:
        """
        Возвращает цену товара.

        Returns:
            float: Цена товара.
        """

        return self.__price

    def get_location(self) -> str:
        """
        Возвращает местоположение товара.

        Returns:
            str: Местоположение товара.
        """

        return self.__location

    def get_city(self) -> str:
        """
        Возвращает описание товара.

        Returns:
            str: Описание товара.
        """

        return self.__city

    def get_item_id(self) -> Optional[str]:
        """
        Возвращает уникальный идентификатор товара.

        Returns:
            str: Уникальный идентификатор товара.
        """

        return self.__product_id

    def set_price(self, value: float) -> None:
        """
        Устанавливает цену товара с валидацией.

        Args:
            value (float): Новая цена товара.

        Raises:
            ValueError: Если цена не является положительным числом.
        """

        if not isinstance(value, (int, float)) or value <= 0:
            raise ValueError("Price must be positive")

        self.__price = value

    def set_quantity(self, value: int) -> None:
        """
        Устанавливает количество товара с валидацией.

        Args:
            value (int): Новое количество товара.

        Raises:
            ValueError: Если количество не является неотрицательным целым числом.
        """

        if not isinstance(value, int) or value < 0:
            raise ValueError("Quantity must be a non-negative integer")

        self.__quantity = value

    def set_state(self, value: ItemState) -> None:
        """
        Устанавливает состояние товара с валидацией.

        Args:
            value (ItemState): Новое состояние товара.

        Raises:
            TypeError: Если новое состояние не является экземпляром ProductState.
        """

        if not isinstance(value, ItemState):
            raise TypeError("State must be a ProductState")

        self.__state = value

    def set_name(self, value: str) -> None:
        """
        Устанавливает название товара с валидацией.

        Args:
            value (str): Новое название товара.

        Raises:
            ValueError: Если название является пустой строкой.
        """

        if not isinstance(value, str) or value == "":
            raise ValueError("Name cannot be empty")

        self.__name = value

    def set_location(self, value: str) -> None:
        """
        Устанавливает местоположение товара с валидацией.

        Args:
            value (str): Новое местоположение товара.

        Raises:
            ValueError: Если местоположение является пустой строкой.
        """

        if not isinstance(value, str) or value == "":
            raise ValueError("Location cannot be empty")

        self.__location = value

    def set_city(self, value: str) -> None:
        """
        Устанавливает город товара с валидацией.

        Args:
            value (str): Новый город товара.

        Raises:
            TypeError: Если город не является строкой.
        """

        if not isinstance(value, str):
            raise TypeError("Description must be a string")

        self.__city = value

    def set_supplier(self, value: str) -> None:
        """
        Устанавливает поставщика товара с валидацией.

        Args:
            value (str): Новый поставщик товара.

        Raises:
            ValueError: Если поставщик является пустой строкой.
        """

        if not isinstance(value, str) or value == "":
            raise ValueError("Supplier cannot be empty")

        self.__supplier = value

    def set_manufacturer(self, value: str) -> None:
        """
        Устанавливает производителя товара с валидацией.

        Args:
            value (str): Новый производитель товара.

        Raises:
            ValueError: Если производитель является пустой строкой.
        """

        if not isinstance(value, str) or value == "":
            raise ValueError("Manufacturer cannot be empty")

        self.__manufacturer = value

    def set_product_id(self, value: str) -> None:
        """
        Устанавливает уникальный идентификатор товара с валидацией.

        Args:
            value (str): Новый ID товара.

        Raises:
            ValueError: Если ID товара является пустой строкой.
        """

        if not isinstance(value, str) or value == "":

            raise ValueError("Product ID cannot be empty if provided")

        self.__product_id = value

    def write_off(self) -> None:
        """
        Списывает товар, изменяя его состояние на WRITTEN_OFF.

        Raises:
            Exception: Если товар не зарегистрирован.
        """

        if self.__state != ItemState.REGISTERED:
            raise Exception("Item must be registered to write off")

        self.__state = ItemState.WRITTEN_OFF
