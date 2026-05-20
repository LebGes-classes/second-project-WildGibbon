from code.item.actions.IAction import IAction


class MenuItem:
    def __init__(self, label, action: IAction):
        self.__action = action
        self.__label = label

    def execute(self):
        self.__action.execute()

    def get_label(self):
        return self.__label
