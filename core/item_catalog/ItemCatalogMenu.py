from HomeWork.Item.Item import Item
from HomeWork.Item.ItemState import ItemState
from HomeWork.Item.Menu.IItemMenu import IItemMenu
from HomeWork.ItemCatalog.ItemCatalog import ItemCatalog
from HomeWork.ItemCatalog.ItemCatalogMenuView import ItemCatalogMenuView

from os import system


class ItemCatalogMenu:
    """
    Представляет меню для взаимодействия с каталогом товаров.
    """
    def __init__(self, catalog: ItemCatalog, catalog_menu_view: ItemCatalogMenuView, item_menu: IItemMenu) -> None:
        """
        Инициализирует меню каталога товаров.

        Args:
            catalog (ItemCatalog): Каталог товаров.
            catalog_menu_view (ItemCatalogMenuView): Представление для отображения меню каталога.
            item_menu (IItemMenu): Меню для взаимодействия с отдельным товаром.
        """
        self._view = catalog_menu_view
        self.__item_menu = item_menu
        self.__menu_opened = False
        self.__catalog = catalog

    def open(self) -> None:
        """
        Запускает цикл меню для взаимодействия с каталогом товаров.
        """

        self.__menu_opened = True

        while self.__menu_opened:
            system("cls")

            print(self._view.visualize(self.__catalog.get_items()))

            length = len(self.__catalog.get_items())
            choice = self.__handle_input(0, length + 2)

            if choice == 0:
                self.__menu_opened = False

            elif choice == length + 1:
                self.__catalog.append(Item("default", 0, ItemState.REGISTERED, "default",
                                           "default", 1, "default", "default", "default"))

            elif choice == length + 2:
                print("Выберите карточку которую нужно удалить")

                card_choice = self.__handle_input(1, length)
                self.__catalog.pop(card_choice - 1)

            else:
                choice_item = self.__catalog.get_items()[choice - 1]
                choice_item_old_id = choice_item.get_item_id()

                self.__item_menu.open(choice_item)

                if any(choice_item.get_item_id() == item.get_item_id() for item in self.__catalog.get_items()):
                    choice_item.set_product_id(choice_item_old_id)
                    print("Такой id уже есть, старый id был оставлен")

    def __handle_input(self, lower_limit: int, upper_limit: int) -> int:
        """
        Обрабатывает ввод пользователя и проверяет его на корректность.

        Args:
            lower_limit (int): Нижняя граница допустимого значения.
            upper_limit (int): Верхняя граница допустимого значения.

        Returns:
            int: Корректный выбор пользователя.
        """

        valid_input = False
        choice = 0

        while not valid_input:
            try:
                choice = int(input())

                if not lower_limit <= choice <= upper_limit:
                    raise ValueError

                valid_input = True

            except ValueError:
                print(f"Введите число от {lower_limit} до {upper_limit}")

        return choice
