import tkinter as tk

class Menus(tk.Tk):
    
    _main_menu = None
    _file_menu = None
    _edit_menu = None
    _view_menu = None
    _tools_and_settings_menu = None
    _navigation_menu = None
    
    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)
        self.menu = tk.Menu(self)
        self._main_menu = MainMenu(self)
        self._file_menu = FileMenu(self)
        self._edit_menu = EditMenu(self)
        self._view_menu = ViewMenu(self)
        self._tools_and_settings_menu = ToolsAndSettingsMenu(self)
        self._navigation_menu = NavigationMenu(self)
        
        
class MainMenu(tk.Menu):         
    
    def __init__(self, root, *args, **kwargs):
        tk.Menu.__init__(self, root, *args, **kwargs)
        self._root = root
        file_menu = FileMenu(root, tearoff=0)
        self.add_cascade(label="File", menu=file_menu)
        edit_menu = EditMenu(root, tearoff=0)
        self.add_cascade(label="Edit", menu=edit_menu)
        view_menu = ViewMenu(root, tearoff=0)
        self.add_cascade(label="View", menu=view_menu)
        tools_and_settings_menu = ToolsAndSettingsMenu(root, tearoff=0)
        self.add_cascade(label="Tools/Settings", menu=tools_and_settings_menu)
        navigation_menu = NavigationMenu(root, tearoff=0)
        self.add_cascade(label="Navigation", menu=navigation_menu)
        root.config(menu=self)

class FileMenu(tk.Menu):
    def __init__(self, root, *args, **kwargs):
        tk.Menu.__init__(self, root, *args, **kwargs)
        self.add_command(label="exit", command=root.destroy)

class EditMenu(tk.Menu):
    def __init__(self, root, *args, **kwargs):
        tk.Menu.__init__(self, root, *args, **kwargs)
        self.add_command(label="Undo")
        self.add_command(label="Redo")
        self.add_command(label="Add Map Marker")
        self.add_command(label="Edit Map")
        self.add_command(label="Upload Map Edit")

class ViewMenu(tk.Menu):
    def __init__(self, root, *args, **kwargs):
        tk.Menu.__init__(self, root, *args, **kwargs)
        self.add_command(label="Zoom In")
        self.add_command(label="Zoom Out")
        self.add_command(label="Layers")
        self.add_command(label="Compass")

class ToolsAndSettingsMenu(tk.Menu):
    def __init__(self, root, *args, **kwargs):
        tk.Menu.__init__(self, root, *args, **kwargs)
        self.add_command(label="Account Settings")
        self.add_command(label="Map Settings")
        self.add_command(label="Language")
        self.add_command(label="Region")

class NavigationMenu(tk.Menu):
    def __init__(self, root, *args, **kwargs):
        tk.Menu.__init__(self, root, *args, **kwargs)
        self.add_command(label="Search")
        self.add_command(label="Directions")
        self.add_command(label="Nearby Places")

    
if __name__ == "__main__":
    root = Menus()
    root.mainloop()
