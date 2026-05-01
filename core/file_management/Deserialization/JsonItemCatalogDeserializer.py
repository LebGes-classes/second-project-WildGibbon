from HomeWork.FileManagement.Deserialization.IItemCatalogDeserializer import IItemCatalogDeserializer
from HomeWork.Item.Item import Item
from HomeWork.Item.ItemState import ItemState
from HomeWork.ItemCatalog.ItemCatalog import ItemCatalog

import json


class JsonItemCatalogDeserializer(IItemCatalogDeserializer):
    """
    Класс для десериализации каталога товаров из файла JSON.
    """
    def deserialize(self, file_path: str) -> ItemCatalog:
        """
        Десериализует каталог товаров из файла JSON.

        Args:
            file_path (str): Путь к файлу JSON для десериализации.

        Returns:
            ItemCatalog: Объект каталога товаров.
        """
        with open(file_path, 'r', encoding='utf-8') as file:
            data = json.load(file)
            items = []

            for item_data in data['items']:
                item_data['state'] = ItemState(item_data['state'])
                item = Item(**item_data)
                items.append(item)

            return ItemCatalog(items)
