from HomeWork.Item.Item import Item
from HomeWork.Item.ItemState import ItemState
from HomeWork.Item.ItemView import ItemView

import os


class ItemMenu:
    """
    Представляет меню для взаимодействия с карточкой товара.
    """

    def __init__(self, item_view: ItemView) -> None:
        """
        Инициализирует меню товара.

        Args:
            item_view (ItemView): Представление для отображения информации о товаре.
        """
        self.item_view = item_view
        self.__menu_opened = False

    def open(self, item: Item) -> None:
        """
        Запускает цикл меню для взаимодействия с товаром.

        Args:
            item (Item): Товар, с которым нужно взаимодействовать.
        """

        self.__menu_opened = True

        while self.__menu_opened:
            os.system("cls")

            print(self.item_view.visualize(item))

            self.__handle_input(item)

    def __handle_input(self, item: Item) -> None:
        """
        Обрабатывает ввод пользователя в меню.

        Args:
            item (Item): Товар, которым управляет меню.
        """
        choice = input("Выберите действие: ")

        match choice:
            case "1":
                new_value = input("Введите новое ID: ")

                try:
                    item.set_product_id(new_value)
                except ValueError as e:
                    print(f"Ошибка: {e}")

            case "2":
                new_value = input("Введите новое название: ")

                try:
                    item.set_name(new_value)
                except ValueError as e:
                    print(f"Ошибка: {e}")

            case "3":
                new_value = input("Введите новое количество: ")

                try:
                    item.set_quantity(int(new_value))
                except ValueError as e:
                    print(f"Ошибка: {e}")

            case "4":
                print("Список состояний:\n"
                      "1. Временно недоступно\n"
                      "2. Списано\n"
                      "3. Состоит на учете")

                new_value = input("Введите новое состояние (1-3): ")

                try:
                    state_value = int(new_value)

                    if state_value == 1:
                        item.set_state(ItemState.TEMPORARY_UNAVAILABLE)
                    elif state_value == 2:
                        item.set_state(ItemState.WRITTEN_OFF)
                    elif state_value == 3:
                        item.set_state(ItemState.REGISTERED)
                    else:
                        print("Ошибка: Неверный выбор состояния. Введите число от 1 до 3.")

                except ValueError as e:
                    print(f"Ошибка: {e}")

            case "5":
                new_value = input("Введите нового поставщика: ")

                try:
                    item.set_supplier(new_value)
                except ValueError as e:
                    print(f"Ошибка: {e}")

            case "6":
                new_value = input("Введите нового производителя: ")

                try:
                    item.set_manufacturer(new_value)
                except ValueError as e:
                    print(f"Ошибка: {e}")

            case "7":
                new_value = input("Введите новую цену: ")

                try:
                    item.set_price(float(new_value))
                except ValueError as e:
                    print(f"Ошибка: {e}")

            case "8":
                new_value = input("Введите новое местоположение: ")

                try:
                    item.set_location(new_value)
                except ValueError as e:
                    print(f"Ошибка: {e}")

            case "9":
                new_value = input("Введите новый город: ")

                try:
                    item.set_city(new_value)
                except ValueError as e:
                    print(f"Ошибка: {e}")

            case "10":
                self.__menu_opened = False

            case _:
                print("Неверный выбор действия.")


