from abc import ABC, abstractmethod


class Item(ABC):
    def __init__(self, name, description):
        self.name = name
        self.description = description

    @abstractmethod
    def use(self, message_box):
        pass

    def __eq__(self, other):
        if isinstance(other, Item):
            return self.name == other.name
        return False
