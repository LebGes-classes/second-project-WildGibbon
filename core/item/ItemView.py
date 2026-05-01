from HomeWork.Item.Item import Item
from HomeWork.Item.ItemState import ItemState


class ItemView:
    """
    Класс для визуализации информации о товаре.
    """
    def visualize(self, item: Item) -> str:
        """
        Создает текстовое представление карточки товара.

        Args:
            item (Item): Объект товара для визуализации.

        Returns:
            str: Строка с форматированной информацией о товаре.
        """
        card_state = ""

        if item.get_state() == ItemState.TEMPORARY_UNAVAILABLE:
            card_state = "Временно недоступно"

        if item.get_state() == ItemState.WRITTEN_OFF:
            card_state = "Списано"

        if item.get_state() == ItemState.REGISTERED:
            card_state = "Состоит на учете"

        result = (f"╔═══════════════════════════════════════╗" + "\n" +
                  f"║ 1.ID: {item.get_item_id()}".ljust(40) + "║\n" +
                  f"║ 2.Название: {item.get_name()}".ljust(40) + "║\n" +
                  f"║ 3.Количество: {item.get_quantity()}".ljust(40) + "║\n" +
                  f"║ 4.Состояние: {card_state}".ljust(40) + "║\n" +
                  f"║ 5.Поставщик: {item.get_supplier()}".ljust(40) + "║\n" +
                  f"║ 6.Производитель: {item.get_manufacturer()}".ljust(40) + "║\n" +
                  f"║ 7.Цена: {item.get_price()}".ljust(40) + "║\n" +
                  f"║ 8.Местоположение: {item.get_location()}".ljust(40) + "║\n" +
                  f"║ 9.Город: {item.get_city()}".ljust(40) + "║\n" +
                  f"╠═══════════════════════════════════════╣" + "\n" +
                  f"║              ДЕЙСТВИЯ                 ║" + "\n" +
                  f"╠═══════════════════════════════════════╣" + "\n" +
                  f"║ 10. Выйти из карточки товара          ║" + "\n"
                  f"╚═══════════════════════════════════════╝" + "\n")

        return result
