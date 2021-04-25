from Button import Button
from Dialog import Dialog
from Panel import Panel


def main():
    dialog = Dialog()
    panel = Panel()
    ok = Button("Ok")
    cancel = Button("Cancel")
    panel.add_children(ok)
    panel.add_children(cancel)
    dialog.add_children(panel)

    ok.show_help()


if __name__ == '__main__':
    main()
