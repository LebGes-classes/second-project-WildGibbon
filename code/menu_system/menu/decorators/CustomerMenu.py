from code.entities.customer.Customer import Customer
from code.menu_system.factories.LeafItemFactory import create_leaf_item
from code.menu_system.actions.DelegateAction import DelegateAction
from code.menu_system.menu.item.MenuItem import MenuItem
from code.menu_system.menu.Menu import IMenu


class CustomerMenu(IMenu):
    def __init__(self, menu: IMenu, customers: list[Customer]):
        self.__customers = customers
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
        self.__menu.insert_item(0, MenuItem("Добавить покупателя", DelegateAction(self.__add_customer)))
        self.__menu.insert_item(0, MenuItem("Удалить покупателя", DelegateAction(self.__remove_customer)))

        for customer in self.__customers:
            product_item = create_leaf_item(customer.id,
                                            customer.name,
                                            customer.email)

            self.__menu.append_item(product_item)

    def __add_customer(self):
        id = input("Enter ID: ")
        name = input("Enter name: ")
        email = input("Enter email: ")

        menu_item = create_leaf_item(name, id, email)

        self.__customers.append(Customer(id, name, email))
        self.__menu.append_item(menu_item)

    def __remove_customer(self):
        num = int(input("Enter number: "))
        self.__menu.remove_item(num - 1)
        self.__customers.pop(num - 4)
