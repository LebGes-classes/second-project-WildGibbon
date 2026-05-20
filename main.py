import supabase
import os

from code.item.actions.AddProductAction import AddProductAction
from code.item.menu.Menu import Menu
from code.item.menu.MenuView import MenuView
from dotenv import load_dotenv


load_dotenv()
url = os.environ.get('SUPABASE_URL')
key = os.environ.get('SUPABASE_KEY')


client = supabase.create_client(url, key)

items = []
menu = Menu(items, AddProductAction(client), MenuView(), client)

menu.open()


