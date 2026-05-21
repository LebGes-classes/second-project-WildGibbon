from postgrest import SyncRequestBuilder

from code.menu_system.factories.LeafItemFactory import create_leaf_item
from code.menu_system.actions.IAction import IAction


class AddProductAction(IAction):
    def __init__(self, db_table: SyncRequestBuilder):
        self.__table = db_table

    def execute(self):
        id = input("Enter ID: ")
        name = input("Enter name: ")
        warehouse_id = input("Enter warehouse: ")
        description = input("Enter description: ")

        product_item = create_leaf_item(name, warehouse_id, description, id)
        print(self.__table.insert({"id": int(id), "name": name, "warehouse_id": int(warehouse_id), "description": description}).execute())

        return product_item