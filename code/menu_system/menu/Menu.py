from code.menu_system.menu.IMenu import IMenu
import os


class Menu(IMenu):
    def __init__(self, items: list, add_item_action, view):
        self.__add_item_action = add_item_action
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


    def add_item(self, item):
         self.__items.append(item)

    def remove_item(self, item_number):
        self.__items.pop(item_number)

    def close(self):
        self.__is_opened = False



