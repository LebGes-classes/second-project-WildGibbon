from code.menu_system.factories.ImmutableItemFactory import create_immutable_item
from code.menu_system.actions.AddProductAction import AddProductAction
from code.menu_system.MenuItem import MenuItem
from code.menu_system.menu.Menu import IMenu
from postgrest import SyncRequestBuilder


class ProductMenuDecorator(IMenu):
    def __init__(self, menu: IMenu, products, db_table: SyncRequestBuilder):
        self.__products = products
        self.__table = db_table
        self.__menu = menu

    def open(self):
        self.__menu.add_item(MenuItem("Добавить товар", AddProductAction))

    def __add_product(self):
        id = input("Enter ID: ")
        name = input("Enter name: ")
        warehouse_id = input("Enter warehouse: ")
        description = input("Enter description: ")

        product_item = create_immutable_item(name, warehouse_id, description, id)
        self.__table.insert(
            {"id": int(id),
             "name": name,
             "warehouse_id": int(warehouse_id),
             "description": description}
        ).execute()

        return product_item