from code.data_base.deserialization.SupabaseDeserializer import SupabaseDeserializer
from code.data_base.serialization.SupabaseSerializer import SupabaseSerializer
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
serializer = SupabaseSerializer(client)

product_table = client.table("Product")
products = deserializer.get_products()

menu = ProductMenu(
        ClosableMenu(
            Menu([], MenuView())
        ), products)

menu.open()

response = client.table("Product") \
            .delete() \
            .neq("id", "0") \
            .execute()


serializer.serialize_products(products)


