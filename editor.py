from tkinter import *

class EditorApp(Canvas):

    def __init__(self, parent):
        super().__init__(parent, width=640, height=480)
        self.create_text((100, 100), text="Test")

if __name__ == "__main__":
    root = Tk()
    app = EditorApp(root)
    app.pack()
    root.mainloop()
