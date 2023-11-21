import tkinter
import flask
import folium
import requests

# you can change some the coding if you think no right
app = flask.Flask(__name__)

def generate_base_map():
    map = folium.Map(location=[45.5236, -122.6750], zoom_start=10)
    return map._repr_html_()

def generate_open_street_map():
    map = folium.Map(location=[45.52336, -122.6750], tiles="Stamen Toner", zoom_start=13)
    folium.Marker(location=[45.52336, -122.6750], popup="<b>Marker here</b>", tooltip="Click Here!").add_to(map)
    return map._repr_html_()

def generate_base_map():
    map = folium.Map(location=[45.5236, -122.6750], zoom_start=10)
    return map._repr_html_()

def generate_open_street_map():
    map = folium.Map(location=[45.52336, -122.6750], tiles="Stamen Toner", zoom_start=13)
    folium.Marker(location=[45.52336, -122.6750], popup="<b>Marker here</b>", tooltip="Click Here!").add_to(map)
    return map._repr_html_()

def generate_map_with_markers():
    map = folium.Map(location=[45.52336, -122.6750], tiles="Stamen Terrain", zoom_start=12)
    folium.Marker(location=[45.52336, -122.6750], popup="<b>Marker here</b>", tooltip="Click Here!").add_to(map)
    folium.Marker(location=[45.55736, -122.8750], popup="<b>Marker 2 here</b>", tooltip="Click Here!", icon=folium.Icon(color="green")).add_to(map)
    folium.Marker(location=[45.53236, -122.8750], popup="<b>Marker 3 here</b>", tooltip="Click Here!", icon=folium.Icon(color="red")).add_to(map)
    return map._repr_html_()

# Flask route to render the map@app.route('/map')
@app.route('/')
def show_map():
    return generate_base_map()  # Use the desired map generation function here

def run_flask():
    app.run()
class Root(tkinter.Tk):
    def __init__(self, *args, **kwargs):
        tkinter.Tk.__init__(self, *args, **kwargs)
        self.title('Map Application')
        self.geometry('700x700')

        self._scroll_vertical = ScrollVertical(self)
        self._scroll_vertical.pack(side='right')
        self._scroll_horizontal = ScrollHorizontal(self)
        self._scroll_horizontal.pack(side='bottom')
        self._main_menu = MainMenu(self)

        # Use a label to display the fetched web content
        self.map_label = tkinter.Label(self, text="Map will appear here")
        self.map_label.pack()

    # Method to update the web content in the Tkinter interface
    def update_web_content(self, content):
        self.map_label.configure(text=content)

class ScrollVertical(tkinter.Scrollbar):
    def __init__(self, root, *args, **kwargs):
        tkinter.Scrollbar.__init__(self, root, *args, **kwargs, orient='vertical')

class ScrollHorizontal(tkinter.Scrollbar):
    def __init__(self, root, *args, **kwargs):
        tkinter.Scrollbar.__init__(self, root, *args, **kwargs, orient='horizontal')

class MainMenu(tkinter.Menu):
    def __init__(self, root, *args, **kwargs):
        tkinter.Menu.__init__(self, root, *args, **kwargs)
        
        self._root = root
        menu_1 = Menu_1(self, tearoff=0)
        self.add_cascade(label='Map Application', menu=menu_1)
        root.config(menu=self)

class Menu_1(tkinter.Menu):
    def __init__(self, root, *args, **kwargs):
        tkinter.Menu.__init__(self, root, *args, **kwargs)
        self.root = root
        self.add_command(label='Show Map', command=self.show_map)

    def show_map(self):
        response = requests.get('http://127.0.0.1:5000/')  # Assuming you have Flask server is running locally

        if response.status_code == 200:
            # Update the Tkinter GUI with the received web content
            self.root.master.update_web_content(response.text)
        else:
            self.root.master.update_web_content("Failed to load map")

if __name__ == "__main__":
    root = Root()
    root.mainloop()
