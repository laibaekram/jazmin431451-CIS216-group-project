from flask import Flask
import folium
import webbrowser
import threading
import tkinter as tk

app = Flask(__name__)

def create_map(location, tiles='OpenStreetMap', zoom_start=13):
    m = folium.Map(location=location, tiles=tiles, zoom_start=zoom_start)
    folium.Marker(location, popup="<b>User Selected Location</b>").add_to(m)
    return m._repr_html_()

@app.route("/")
def base():
    return create_map([45.52336, -122.6750])

@app.route("/open-street-map")
def open_street_map():
    return create_map([45.52336, -122.6750], tiles='Stamen Toner')

@app.route("/map-marker")
def map_marker():
    m = folium.Map(location=[45.52336, -122.6750], tiles='Stamen Terrain', zoom_start=12)
    folium.Marker(location=[45.52336, -122.6750], popup="<b>Marker here</b>", tooltip="Click Here!").add_to(m)
    folium.Marker(location=[45.53236, -122.8750], popup="<b>Marker 2 here</b>", tooltip="Click Here!", icon=folium.Icon(color='green')).add_to(m)
    folium.Marker(location=[45.54236, -122.8750], popup="<b>Marker 3 here</b>", tooltip="Click Here!", icon=folium.Icon(color='red')).add_to(m)
    return m._repr_html_()

@app.route("/custom-map/<coords>")
def custom_map(coords):
    try:
        lat, lon = map(float, coords.split(','))
        return create_map([lat, lon])
    except ValueError:
        return "Invalid coordinates", 400

def start_flask():
    app.run(debug=False, use_reloader=False)

def open_browser():
    webbrowser.open('http://127.0.0.1:5000/')

def create_tkinter_window():
    root = tk.Tk()
    root.title("Flask and Tkinter Integration")

    tk.Label(root, text="Latitude:").pack()
    lat_entry = tk.Entry(root)
    lat_entry.pack()

    tk.Label(root, text="Longitude:").pack()
    lon_entry = tk.Entry(root)
    lon_entry.pack()

    def open_custom_map():
        lat = lat_entry.get()
        lon = lon_entry.get()
        webbrowser.open(f'http://127.0.0.1:5000/custom-map/{lat},{lon}')

    custom_map_button = tk.Button(root, text="Custom Map", command=open_custom_map)
    custom_map_button.pack()

    button1 = tk.Button(root, text="Base Map", command=lambda: webbrowser.open('http://127.0.0.1:5000/'))
    button1.pack()

    button2 = tk.Button(root, text="Open Street Map", command=lambda: webbrowser.open('http://127.0.0.1:5000/open-street-map'))
    button2.pack()

    button3 = tk.Button(root, text="Map Marker", command=lambda: webbrowser.open('http://127.0.0.1:5000/map-marker'))
    button3.pack()

    root.mainloop()

if __name__ == "__main__":
    flask_thread = threading.Thread(target=start_flask)
    flask_thread.start()
    create_tkinter_window()
