from Container import Container


class Dialog(Container):
    wiki_page_url: str

    def show_help(self):
        if self.wiki_page_url:
            print(f'dialog help text is : {self.wiki_page_url}')
        else:
            super().show_help()
