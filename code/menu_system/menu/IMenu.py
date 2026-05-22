from abc import ABC, abstractmethod


class IMenu(ABC):
    @abstractmethod
    def open(self):
        pass

    @abstractmethod
    def length(self):
        pass

    @abstractmethod
    def append_item(self, item):
        pass

    @abstractmethod
    def insert_item(self, index, menu_item):
        pass

    @abstractmethod
    def remove_item(self, index):
        pass

    @abstractmethod
    def close(self):
        pass