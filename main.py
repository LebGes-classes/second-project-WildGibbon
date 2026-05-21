from code.menu_system.menu.decorators.ClosableMenu import ClosableMenu
from code.menu_system.menu.decorators.DeletableMenu import DeletableMenu
from code.menu_system.menu.decorators.ProductMenu import ProductMenuDecorator
from code.menu_system.menu.MenuView import MenuView
from code.entities.product.Product import Product
from code.menu_system.menu.Menu import Menu
from dotenv import load_dotenv

import supabase
import os

load_dotenv()
url = os.environ.get('SUPABASE_URL')
key = os.environ.get('SUPABASE_KEY')


client = supabase.create_client(url, key)
product_table = client.table("Product")
products = [Product("1341", 4134234, 41354 , 53544)]

menu = ProductMenuDecorator(
    DeletableMenu(
        ClosableMenu(
            Menu([], MenuView()))
    ), products)

menu.open()


