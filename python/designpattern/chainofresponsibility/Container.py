from abc import ABC
from typing import List

from Component import Component


class Container(Component, ABC):
    children: List[Component]

    def __init__(self):
        super().__init__("")
        self.children = []

    def add_children(self, child: Component):
        if not isinstance(child, Component):
            raise TypeError("invalid type for child argument")
        child.container = self
        self.children.append(child)
