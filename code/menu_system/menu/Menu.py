from code.menu_system.menu.IMenu import IMenu
import os


class Menu(IMenu):
    def __init__(self, items: list, view):
        self.__items = items.copy()
        self.__view = view

        self.__is_opened = False


    def open(self):
        self.__is_opened = True

        while self.__is_opened:
            os.system("cls")
            print(self.__view.visualize(self.__items))
            item_num = input("Enter element number: ")

            self.__items[int(item_num) - 1].execute()

    def append_item(self, item):
        self.__items.append(item)

    def insert_item(self, index, item):
         self.__items.insert(index, item)

    def remove_item(self, index):
        self.__items.pop(index)

    def close(self):
        self.__is_opened = False



