from abc import ABC, abstractmethod


class IComponentWithContextualHelpHandler(ABC):
    @abstractmethod
    def show_help(self):
        raise NotImplementedError
