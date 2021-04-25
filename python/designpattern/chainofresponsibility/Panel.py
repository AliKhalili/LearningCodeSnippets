from Component import Component
from Container import Container


class Panel(Container):
    modal_help_text: str

    def show_help(self):
        if self.modal_help_text:
            print(f'panel help text is : {self.modal_help_text}')
        else:
            super().show_help()
