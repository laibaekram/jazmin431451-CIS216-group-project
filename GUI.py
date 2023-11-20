import tkinter


class Root(tkinter.Tk):
    
    _scroll_vertical = None
    _scroll_horizontal = None
    _main_menu = None
    
    def __init__(self, *args, **kwargs):
        tkinter.Tk.__init__(self, *args, **kwargs)
        self.title('Map Application')
        self.geometry('700x700')
        
        self._scroll_vertical = ScrollVertical(self)
        self._scroll_vertical.pack(side = 'right')
        self._scroll_horizontal = ScrollHorizontal(self)
        self._scroll_horizontal.pack(side='bottom')
        self._main_menu = MainMenu(self)
    
class ScrollVertical(tkinter.Scrollbar):
    @property
    def root(self):
        return self._root
    
    def __init__(self, root, *args, **kwargs):
        tkinter.Scrollbar.__init__(self, root, *args, **kwargs, orient='vertical')


class ScrollHorizontal(tkinter.Scrollbar):
    @property
    def root(self):
        return self._root
    
    def __init__(self, root, *args, **kwargs):
        tkinter.Scrollbar.__init__(self, root, *args, **kwargs, orient='horizontal')

class MainMenu(tkinter.Menu):
    @property
    def root(self):
        return self._root
    
    def __init__(self, root, *args, **kwargs):
        tkinter.Menu.__init__(self, root, *args, **kwargs)
        
        self._root = root
        
        menu_1 = Menu_1(self, tearoff=0)
        menu_2 = Menu_2(self, tearoff=0)
        menu_3 = Menu_3(self, tearoff=0)
        self.add_cascade(label='Menu 1', menu=menu_1)
        self.add_cascade(label='Menu 2', menu=menu_2)
        self.add_cascade(label='Menu 3', menu=menu_3)
        root.config(menu=self)
        

class Menu_1(tkinter.Menu):
    def __init__(self, root, *args, **kwargs):
        tkinter.Menu.__init__(self, root, *args, **kwargs)
        self.add_command(label='Option 1', command=self.master.quit)
        self.add_command(label='Option 2')
        self.add_command(label='Option 3')
        self.add_command(label='Option 4')
        self.add_command(label='Option 5')
        
class Menu_2(tkinter.Menu):
    def __init__(self, root, *args, **kwargs):
        tkinter.Menu.__init__(self, root, *args, **kwargs)
        self.add_command(label='Option 1')
        self.add_command(label='Option 2')
        self.add_command(label='Option 3')

class Menu_3(tkinter.Menu):
    def __init__(self, root, *args, **kwargs):
        tkinter.Menu.__init__(self, root, *args, **kwargs)
        self.add_command(label='Option 1')
        self.add_command(label='Option 2')
        self.add_command(label='Option 3')

if __name__ == "__main__":
    root = Root()
    root.mainloop()
