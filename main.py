import supabase
import os

from code.entities.product.Product import Product
from code.menu_system.menu.Menu import Menu
from code.menu_system.menu.MenuView import MenuView
from dotenv import load_dotenv

from code.menu_system.menu.Decorators.ProductMenuDecorator import ProductMenuDecorator

load_dotenv()
url = os.environ.get('SUPABASE_URL')
key = os.environ.get('SUPABASE_KEY')


client = supabase.create_client(url, key)
product_table = client.table("Product")
products = [Product("1341", 4134234, 41354 , 53544)]

menu = ProductMenuDecorator(Menu([], MenuView()), products)

menu.open()


