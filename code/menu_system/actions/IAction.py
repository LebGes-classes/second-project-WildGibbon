import abc


class IAction(abc.ABC):
    @abc.abstractmethod
    def execute(self):
        pass
