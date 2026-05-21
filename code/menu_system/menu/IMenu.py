from abc import ABC


class IMenu(ABC):
    def open(self):
        pass

    def add_item(self, menu_item):
        pass

    def remove_item(self, menu_item):
        pass