
from enum import Enum


class ItemState(Enum):
    """
    Перечисление, представляющее возможные состояния товара.
    """
    TEMPORARY_UNAVAILABLE = 1
    WRITTEN_OFF = 2
    REGISTERED = 3
