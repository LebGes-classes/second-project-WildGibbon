from code.file_management.Deserialization.SupabaseDeserializer import SupabaseDeserializer
from code.menu_system.menu.decorators.ProductMenu import ProductMenu
from code.menu_system.menu.decorators.DeletableMenu import DeletableMenu
from code.menu_system.menu.decorators.ClosableMenu import ClosableMenu
from code.menu_system.menu.MenuView import MenuView
from code.menu_system.menu.Menu import Menu
from dotenv import load_dotenv

import supabase
import os

load_dotenv()
url = os.environ.get('SUPABASE_URL')
key = os.environ.get('SUPABASE_KEY')
client = supabase.create_client(url, key)

deserializer = SupabaseDeserializer(client)

product_table = client.table("Product")
products = deserializer.get_products()

menu = ProductMenu(
    DeletableMenu(
        ClosableMenu(
            Menu([], MenuView()))
    ), products)

menu.open()


