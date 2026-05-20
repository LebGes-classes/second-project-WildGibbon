from code.item.actions.OpenMenuAction import OpenMenuAction
from code.item.menu.ImmutableMenu import ImmutableMenu
from code.item.actions.MockAction import MockAction
from code.item.menu.MenuView import MenuView
from code.item.MenuItem import MenuItem


def create_immutable_item(name, *args):
    items = []

    for arg in args:
        items.append(MenuItem(arg, MockAction()))

    product_menu = ImmutableMenu(items, MenuView())
    product_item = MenuItem(name, OpenMenuAction(product_menu))

    return product_item