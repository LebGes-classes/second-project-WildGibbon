from code.menu_system.factories.LeafItemFactory import create_leaf_item
from code.menu_system.actions.DelegateAction import DelegateAction
from code.menu_system.menu.item.MenuItem import MenuItem
from code.entities.product.Product import Product
from code.menu_system.menu.Menu import IMenu


class ProductMenu(IMenu):
    def __init__(self, menu: IMenu, products):
        self.__products = products
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
        self.__menu.insert_item(0, MenuItem("Добавить товар", DelegateAction(self.__add_product)))
        self.__menu.insert_item(0, MenuItem("Удалить товар", DelegateAction(self.__remove_item)))

        for product in self.__products:
            product_item = create_leaf_item(product.name,
                                            product.warehouse,
                                            product.description,
                                            product.id)

            self.__menu.append_item(product_item)

    def __add_product(self):
        id = input("Enter ID: ")
        name = input("Enter name: ")
        warehouse_id = input("Enter warehouse: ")
        description = input("Enter description: ")

        product_item = create_leaf_item(name, warehouse_id, description, id)

        self.__products.append(Product(id, name, description, warehouse_id))
        self.__menu.append_item(product_item)

    def __remove_item(self):
        num = int(input("Enter number: "))
        self.__menu.remove_item(num - 1)

        self.__products.pop(num - 4)
