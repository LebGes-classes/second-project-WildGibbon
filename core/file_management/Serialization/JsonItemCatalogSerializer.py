from HomeWork.FileManagement.Serialization.IItemCatalogSerializer import IItemCatalogSerializer
from HomeWork.ItemCatalog.ItemCatalog import ItemCatalog

from typing import Dict, Any, List


class JsonItemCatalogSerializer(IItemCatalogSerializer):
    """
    Класс для сериализации каталога товаров в формат JSON.
    """
    def serialize(self, item_catalog: ItemCatalog) -> Dict[str, List[Dict[str, Any]]]:
        """
        Сериализует каталог товаров в формат JSON.

        Args:
            item_catalog (ItemCatalog): Каталог товаров для сериализации.

        Returns:
            dict: Словарь, представляющий каталог товаров в формате JSON.
        """
        items = []

        for item in item_catalog.get_items():
            items.append({'name': item.get_name(),
                          'quantity': item.get_quantity(),
                          'state': item.get_state().value,
                          'supplier': item.get_supplier(),
                          'manufacturer': item.get_manufacturer(),
                          'price': item.get_price(),
                          'location': item.get_location(),
                          'city': item.get_city(),
                          'product_id': item.get_item_id()})

        return {"items": items}
