import tkinter as tk
import webbrowser


class MapApp(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title('OpenStreetMap')

        self.menu_bar = tk.Menu(self)
        self.config(menu=self.menu_bar)

        self.file_menu = tk.Menu(self.menu_bar, tearoff=0)
        self.file_menu.add_command(label="Exit", command=self.quit)
        self.menu_bar.add_cascade(label="File", menu=self.file_menu)

        self.view_menu = tk.Menu(self.menu_bar, tearoff=0)
        self.view_menu.add_command(label="Show Map by Coordinates", command=self.show_map_by_coordinates_dialog)
        self.menu_bar.add_cascade(label="View", menu=self.view_menu)

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

        # Perform the search logic (for example, open a map in a web browser)
        if location:
            map_url = f"https://www.openstreetmap.org/search?query={location}"
            webbrowser.open(map_url)

    def show_map_by_coordinates_dialog(self):
        dialog = CustomDialog(self)
        self.wait_window(dialog)

        if dialog.result:
            coordinates = dialog.text.split(",")
            if len(coordinates) == 2:
                lat, lon = coordinates
                lat = float(lat.strip())
                lon = float(lon.strip())
                self.show_map(lat, lon)

    def show_map(self, lat, lon):
        # Implement your map display logic here
        pass


class CustomDialog(tk.Toplevel):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.title("Enter Coordinates")

        self._result = False
        self._text = None

        self._add_widgets()

    @property
    def result(self):
        return self._result

    @property
    def text(self):
        return self._text

    def _add_widgets(self):
        label = tk.Label(self, text="Enter Latitude, Longitude (comma-separated):")
        label.grid(row=0, column=0)

        self.entry = tk.Entry(self)
        self.entry.grid(row=1, column=0)

        ok_button = tk.Button(self, text="OK", command=self._ok_click)
        ok_button.grid(row=0, column=1)

        cancel_button = tk.Button(self, text="Cancel", command=self._cancel_click)
        cancel_button.grid(row=1, column=1)

        self.bind("<Return>", self._ok_click)
        self.bind("<Escape>", self._cancel_click)

    def _cancel_click(self, event=None):
        self._text = None
        self._result = False
        self.destroy()

    def _ok_click(self, event=None):
        self._text = self.entry.get()
        self._result = True
        self.destroy()


if __name__ == "__main__":
    app = MapApp()
    app.mainloop()