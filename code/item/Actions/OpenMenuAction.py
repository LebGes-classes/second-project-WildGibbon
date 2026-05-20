from code.item.Actions.IAction import IAction


class OpenMenuAction(IAction):
    def __init__(self, product_menu):
        self.menu = product_menu

    def execute(self):
        self.menu.open()