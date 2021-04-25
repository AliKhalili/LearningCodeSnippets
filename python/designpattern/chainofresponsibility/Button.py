from Component import Component


class Button(Component):
    def __init__(self, tool_tip_text: str):
        super().__init__(tooltip_text=tool_tip_text)