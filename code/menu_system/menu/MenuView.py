from code.menu_system.menu.item.MenuItem import MenuItem
from typing import List


class MenuView:
    def visualize(self, items: List[MenuItem]):
        items_list = ""
        for i in range(len(items)):
            items_list += f"║ {i + 1}: {items[i].get_label()}".ljust(40) + "║\n"

        result = (f"╔═══════════════════════════════════════╗" + "\n" +
                  items_list +
                  f"╠═══════════════════════════════════════╣" + "\n" +
                  f"║           ВЫБЕРИТЕ ЭЛЕМЕНТ            ║" + "\n" +
                  f"╚═══════════════════════════════════════╝" + "\n")

        return result