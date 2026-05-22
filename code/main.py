from data_base.deserialization.SupabaseDeserializer import SupabaseDeserializer
from data_base.serialization.SupabaseSerializer import SupabaseSerializer
from menu_system.actions.OpenMenuAction import OpenMenuAction
from menu_system.menu.item.MenuItem import MenuItem
from menu_system.menu.MenuView import MenuView
from menu_system.menu.decorators import *
from menu_system.menu.Menu import Menu
from dotenv import load_dotenv
from entities import *

import supabase
import os


load_dotenv()
url = os.environ.get('SUPABASE_URL')
key = os.environ.get('SUPABASE_KEY')
client = supabase.create_client(url, key)

deserializer = SupabaseDeserializer()
serializer = SupabaseSerializer()

warehouse_table = client.table("Warehouses")
customer_table = client.table("Customers")
employee_table = client.table("Employees")
product_table = client.table("Products")
store_table = client.table("Stores")

warehouses = deserializer.get_entities(Warehouse, warehouse_table)
employees = deserializer.get_entities(Employee, employee_table)
customers = deserializer.get_entities(Customer, customer_table)
products = deserializer.get_entities(Product, product_table)
stores = deserializer.get_entities(Store, store_table)

employee_menu = EmployeeMenu(
    ClosableMenu(
        Menu([], MenuView())
    ), employees)

customer_menu = CustomerMenu(
    ClosableMenu(
        Menu([], MenuView())
    ), customers)

stores_menu = StoreMenu(
    ClosableMenu(
        Menu([], MenuView())
    ), stores)

product_menu = ProductMenu(
    ClosableMenu(
        Menu([], MenuView())
    ), products, warehouses)

warehouse_menu = WarehouseMenu(
    ClosableMenu(
        Menu([], MenuView())
    ), warehouses)

menu = ClosableMenu(
        Menu(
            [
                MenuItem("Products", OpenMenuAction(product_menu)),
                MenuItem("Warehouses", OpenMenuAction(warehouse_menu)),
                MenuItem("Employees", OpenMenuAction(employee_menu)),
                MenuItem("Customers", OpenMenuAction(customer_menu)),
                MenuItem("Stores", OpenMenuAction(stores_menu)),
            ], MenuView()))

menu.open()

serializer.serialize_entities(warehouses, warehouse_table)
serializer.serialize_entities(employees, employee_table)
serializer.serialize_entities(customers, customer_table)
serializer.serialize_entities(products, product_table)
serializer.serialize_entities(stores, store_table)
