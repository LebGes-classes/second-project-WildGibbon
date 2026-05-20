import supabase

from code.item.actions.DelegateAction import DelegateAction
from code.item.menu.IMenu import IMenu
from code.item.MenuItem import MenuItem
import os


class Menu(IMenu):
    def __init__(self, items: list, add_item_action, view, db_client: supabase.Client):
        self.__add_item_action = add_item_action
        self.__items = items.copy()
        self.__client = db_client
        self.__view = view

        self.__items.append(MenuItem("Добавить элемент", DelegateAction(self.__add_item)))
        self.__items.append(MenuItem("Удалить элемент", DelegateAction(self.__delete_item)))
        self.__items.append(MenuItem("Закрыть меню", DelegateAction(self.__close)))
        self.__is_opened = False


    def open(self):
        self.__is_opened = True

        while self.__is_opened:
            os.system("cls")
            print(self.__view.visualize(self.__items))
            item_num = input("Enter item number: ")

            self.__items[int(item_num) - 1].execute()


    def __add_item(self):
         item = self.__add_item_action.execute()
         self.__items.insert(-3, item)

    def __delete_item(self):
        item_num = input("Enter item number: ")
        self.__items.pop(int(item_num) - 1)

    def __close(self):
        self.__is_opened = False



