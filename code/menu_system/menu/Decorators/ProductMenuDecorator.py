from code.menu_system.factories.ImmutableItemFactory import create_immutable_item
from code.menu_system.actions.DelegateAction import DelegateAction
from code.menu_system.menu.MenuItem import MenuItem
from code.entities.product.Product import Product
from code.menu_system.menu.Menu import IMenu


class ProductMenuDecorator(IMenu):
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


    def __build_menu(self):
        self.__menu.insert_item(0, MenuItem("Добавить товар", DelegateAction(self.__add_product)))
        self.__menu.insert_item(0, MenuItem("Удалить товар", DelegateAction(self.__remove_product)))
        self.__menu.insert_item(0, MenuItem("Назад", DelegateAction(self.__close)))

        for product in self.__products:
            product_item = create_immutable_item(product.name,
                                                 product.warehouse,
                                                 product.description,
                                                 product.id)

            self.__menu.append_item(product_item)

    def __add_product(self):
        id = input("Enter ID: ")
        name = input("Enter name: ")
        warehouse_id = input("Enter warehouse: ")
        description = input("Enter description: ")

        product_item = create_immutable_item(name, warehouse_id, description, id)

        self.__products.append(Product(id, name, description, warehouse_id))
        self.__menu.append_item(product_item)

    def __remove_product(self):
        num = input("Enter number: ")
        self.__menu.remove_item(int(num) - 1)

    def __close(self):
        self.__menu.close()