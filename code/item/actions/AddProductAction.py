from code.item.factories.ImmutableItemFactory import create_immutable_item
from code.item.actions.IAction import IAction


class AddProductAction(IAction):
    def __init__(self, db_client):
        self.__db_client = db_client

    def execute(self):
        id = input("Enter ID: ")
        name = input("Enter name: ")
        warehouse = input("Enter warehouse: ")
        description = input("Enter description: ")

        product_item = create_immutable_item(name, warehouse, description, id)

        return product_item