from code.entities.store.Store import Store
from code.menu_system.factories.LeafItemFactory import create_leaf_item
from code.menu_system.actions.DelegateAction import DelegateAction
from code.menu_system.menu.item.MenuItem import MenuItem
from code.menu_system.menu.Menu import IMenu


class StoreMenu(IMenu):
    def __init__(self, menu: IMenu, stores: list[Store]):
        self.__stores = stores
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
        self.__menu.insert_item(0, MenuItem("Добавить магазин", DelegateAction(self.__add_store)))
        self.__menu.insert_item(0, MenuItem("Удалить магазин", DelegateAction(self.__remove_store)))

        for store in self.__stores:
            product_item = create_leaf_item(store.id,
                                            store.name,
                                            store.address)

            self.__menu.append_item(product_item)

    def __add_store(self):
        id = input("Enter ID: ")
        name = input("Enter name: ")
        address = input("Enter address: ")

        menu_item = create_leaf_item(name, id, address)

        self.__stores.append(Store(id, name, address))
        self.__menu.append_item(menu_item)

    def __remove_store(self):
        num = int(input("Enter number: "))
        self.__menu.remove_item(num - 1)
        self.__stores.pop(num - 4)
