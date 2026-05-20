import os

import supabase

from code.item.Actions.DelegateAction import DelegateAction
from code.item.Menu.IMenu import IMenu
from code.item.MenuItem import MenuItem

class ImmutableMenu(IMenu):
    def __init__(self, items: list, view, db_client: supabase.Client):
        self.__items = items.copy()
        self.__client = db_client
        self.__view = view

        self.__items.append(MenuItem("Закрыть меню", DelegateAction(self.__close)))
        self.__is_opened = False


    def open(self):
        self.__is_opened = True

        while self.__is_opened:
            os.system("cls")
            print(self.__view.visualize(self.__items))
            item_num = input("Enter item number: ")

            self.__items[int(item_num) - 1].execute()


    def __close(self):
        self.__is_opened = False



