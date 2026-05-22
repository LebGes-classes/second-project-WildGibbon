from code.menu_system.menu.decorators.ClosableMenu import ClosableMenu
from code.menu_system.actions.OpenMenuAction import OpenMenuAction
from code.menu_system.actions.MockAction import MockAction
from code.menu_system.menu.item.MenuItem import MenuItem
from code.menu_system.menu.MenuView import MenuView
from code.menu_system.menu.Menu import Menu


def create_leaf_item(name, *args):
    items = []

    for arg in args:
        items.append(MenuItem(arg, MockAction()))

    product_menu = ClosableMenu(Menu(items, MenuView()))
    product_item = MenuItem(name, OpenMenuAction(product_menu))

    return product_item