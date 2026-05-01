from HomeWork.FileManagement.Deserialization.IItemCatalogDeserializer import IItemCatalogDeserializer
from HomeWork.Item.Item import Item
from HomeWork.Item.ItemState import ItemState
from HomeWork.ItemCatalog.ItemCatalog import ItemCatalog


class CsvItemCatalogDeserializer(IItemCatalogDeserializer):
    """
    Класс для десериализации каталога товаров из файла CSV.
    """
    def deserialize(self, file_path: str) -> ItemCatalog:
        """
        Десериализует каталог товаров из файла CSV.

        Args:
            file_path (str): Путь к файлу CSV для десериализации.

        Returns:
            ItemCatalog: Объект каталога товаров.
        """
        items = []

        with open(file_path, encoding='utf-8') as file:
            for row in file.read().splitlines():
                data = row.split(',')
                item = Item(
                    data[1],
                    int(data[2]),
                    ItemState(int(data[3])),
                    data[4],
                    data[5],
                    int(data[6]),
                    data[7],
                    data[8],
                    data[0],
                )

                items.append(item)

        return ItemCatalog(items)
