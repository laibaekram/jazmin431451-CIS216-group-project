import tkinter as tk
import webbrowser
import re
from tkinter import messagebox


class MapApp(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title('OpenStreetMap')
        self._create_menus()
        self._create_widgets()

    def _create_menus(self):
        self.menu_bar = tk.Menu(self)
        self.config(menu=self.menu_bar)

        self.file_menu = tk.Menu(self.menu_bar, tearoff=0)
        self.file_menu.add_command(label="Exit", command=self.quit)
        self.menu_bar.add_cascade(label="File", menu=self.file_menu)

        self.view_menu = tk.Menu(self.menu_bar, tearoff=0)
        self.view_menu.add_command(label="Show Map by Coordinates", command=self.show_map_by_coordinates_dialog)
        self.menu_bar.add_cascade(label="View", menu=self.view_menu)

    def _create_widgets(self):
        self.label = tk.Label(self, text="Enter Location:")
        self.label.pack()

        self.location_entry = tk.Entry(self)
        self.location_entry.pack()

        self.search_button = tk.Button(self, text="Search", command=self.search_location)
        self.search_button.pack()

        self.map_canvas = tk.Canvas(self, width=600, height=400, bg="white")
        self.map_canvas.pack()

    def search_location(self):
        location = self.location_entry.get()
        if location:
            map_url = f"https://www.openstreetmap.org/search?query={location}"
            webbrowser.open(map_url)

    def show_map_by_coordinates_dialog(self):
        dialog = CustomDialog(self)
        self.wait_window(dialog)

        if dialog.result:
            try:
                lat, lon = self._parse_coordinates(dialog.text)
                self.show_map(lat, lon)
            except ValueError as e:
                messagebox.showerror("Error", str(e))

    def show_map(self, lat, lon):
        # Placeholder for map display functionality
        # This could be a function to update the map_canvas with a map image
        # For example, using a static map API
        pass

    @staticmethod
    def _parse_coordinates(coord_str):
        pattern = r'^\s*([-+]?\d*\.\d+|\d+)\s*,\s*([-+]?\d*\.\d+|\d+)\s*$'
        match = re.match(pattern, coord_str)
        if not match:
            raise ValueError("Invalid coordinate format. Please enter as 'latitude, longitude'.")
        return float(match.group(1)), float(match.group(2))


class CustomDialog(tk.Toplevel):
    def __init__(self, parent):
        super().__init__(parent)
        self.title("Enter Coordinates")

        self.result = False
        self.text = None
        self._add_widgets()

    def _add_widgets(self):
        label = tk.Label(self, text="Enter Latitude, Longitude (comma-separated):")
        label.grid(row=0, column=0)

        self.entry = tk.Entry(self)
        self.entry.grid(row=1, column=0)

        ok_button = tk.Button(self, text="OK", command=self._ok_click)
        ok_button.grid(row=2, column=0)

        cancel_button = tk.Button(self, text="Cancel", command=self._cancel_click)
        cancel_button.grid(row=2, column=1)

        self.bind("<Return>", self._ok_click)
        self.bind("<Escape>", self._cancel_click)

    def _cancel_click(self, event=None):
        self.destroy()

    def _ok_click(self, event=None):
        self.text = self.entry.get()
        self.result = True
        self.destroy()


if __name__ == "__main__":
    app = MapApp()
    app.mainloop()
