from abc import ABC, abstractmethod


class Parser(ABC):
    @abstractmethod
    def get_links(self):
        pass
