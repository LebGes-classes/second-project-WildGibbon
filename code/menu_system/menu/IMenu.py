from abc import ABC


class IMenu(ABC):
    def open(self):
        pass

    def append_item(self, item):
        pass

    def insert_item(self, index, menu_item):
        pass

    def remove_item(self, index):
        pass

    def close(self):
        pass