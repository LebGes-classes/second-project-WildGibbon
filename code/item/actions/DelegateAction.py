from code.item.actions.IAction import IAction


class DelegateAction(IAction):
    def __init__(self, delegate):
        self.__delegate = delegate

    def execute(self):
        return self.__delegate()