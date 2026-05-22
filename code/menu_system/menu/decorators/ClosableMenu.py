from code.menu_system.actions.DelegateAction import DelegateAction
from code.menu_system.menu.item.MenuItem import MenuItem
from code.menu_system.menu.IMenu import IMenu


class ClosableMenu(IMenu):
    def __init__(self, menu):
        self.__menu = menu
        self.__menu.insert_item(0, MenuItem("Назад", DelegateAction(self.close)))


    def open(self):
        self.__menu.open()

    def close(self):
        self.__menu.close()

    def append_item(self, item):
        self.__menu.append_item(item)

    def insert_item(self, index, menu_item):
        self.__menu.insert_item(index, menu_item)

    def remove_item(self, index):
        self.__menu.remove_item(index)

    def length(self):
        return self.__menu.length()