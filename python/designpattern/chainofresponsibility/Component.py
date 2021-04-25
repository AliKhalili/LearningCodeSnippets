
from IComponentWithContexualHelpHandler import IComponentWithContextualHelpHandler


class Component(IComponentWithContextualHelpHandler):
    container: IComponentWithContextualHelpHandler
    tooltip_text: str

    def __init__(self, tooltip_text: str):
        self.tooltip_text = tooltip_text

    def show_help(self):
        if self.tooltip_text:
            print(f'component help text is : {self.tooltip_text}')
        else:
            self.container.show_help()
