import supabase

from code.item.Actions.MockAction import MockAction
from code.item.Actions.OpenMenuAction import OpenMenuAction
from code.item.Menu.ImmutableMenu import ImmutableMenu
from code.item.Menu.Menu import Menu
from code.item.Menu.MenuView import MenuView
from code.item.MenuItem import MenuItem

def action():
    pass

url = "https://siltyccneevvpfpcwnfv.supabase.co"
key = ""

client = supabase.create_client(url, key)

product_menu = ImmutableMenu([MenuItem("POL", MockAction()), MenuItem("POL2", MockAction())], MenuView(), client)

items = [
    MenuItem("gay", OpenMenuAction(product_menu))
]

menu = Menu(items, MockAction(), MenuView(), client)

menu.open()


