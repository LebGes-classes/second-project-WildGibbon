from code.item.actions.IAction import IAction


class OpenMenuAction(IAction):
    def __init__(self, menu):
        self.menu = menu

    def execute(self):
        self.menu.open()