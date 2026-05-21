from code.menu_system.actions.OpenMenuAction import OpenMenuAction
from code.menu_system.menu.ImmutableMenu import ImmutableMenu
from code.menu_system.actions.MockAction import MockAction
from code.menu_system.menu.MenuView import MenuView
from code.menu_system.MenuItem import MenuItem


def create_immutable_item(name, *args):
    items = []

    for arg in args:
        items.append(MenuItem(arg, MockAction()))

    product_menu = ImmutableMenu(items, MenuView())
    product_item = MenuItem(name, OpenMenuAction(product_menu))

    return product_item