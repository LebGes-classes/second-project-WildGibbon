from code.file_management.Deserialization.IItemCatalogDeserializer import IItemCatalogDeserializer
from code.item_catalog.ItemCatalog import ItemCatalog
from code.item.ItemState import ItemState
from code.item.Product import Product


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
                item = Product(
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
