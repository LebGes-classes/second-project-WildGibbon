from idlelib.mainmenu import menudefs

from code.entities.warehouse.Warehouse import Warehouse
from code.menu_system.factories.LeafItemFactory import create_leaf_item
from code.menu_system.actions.DelegateAction import DelegateAction
from code.menu_system.menu.item.MenuItem import MenuItem
from code.entities.product.Product import Product
from code.menu_system.menu.Menu import IMenu


class WarehouseMenu(IMenu):
    def __init__(self, menu: IMenu, warehouses: list[Warehouse]):
        self.__warehouses = warehouses
        self.__menu = menu

        self.__build_menu()

    def open(self):
        self.__menu.open()

    def close(self):
        self.__menu.close()

    def append_item(self, item):
        self.__menu.append_item(item)

    def insert_item(self, menu_item, index):
        self.__menu.insert_item(index, menu_item)

    def remove_item(self, index):
        self.__menu.remove_item(index)

    def length(self):
        return self.__menu.length()


    def __build_menu(self):
        self.__menu.insert_item(0, MenuItem("Добавить склад", DelegateAction(self.__add_warehouse)))
        self.__menu.insert_item(0, MenuItem("Удалить склад", DelegateAction(self.__remove_warehouse)))

        for warehouse in self.__warehouses:
            product_item = create_leaf_item(warehouse.id,
                                            warehouse.name,
                                            warehouse.location)

            self.__menu.append_item(product_item)

    def __add_warehouse(self):
        id = input("Enter ID: ")
        name = input("Enter name: ")
        location = input("Enter location: ")

        menu_item = create_leaf_item(id, name, location)

        self.__warehouses.append(Warehouse(id, name, location))
        self.__menu.append_item(menu_item)

    def __remove_warehouse(self):
        num = int(input("Enter number: "))
        self.__menu.remove_item(num - 1)
        self.__warehouses.pop(num - 4)
