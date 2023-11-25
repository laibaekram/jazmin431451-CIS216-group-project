import tkinter as tk
from tkinter import messagebox


class RasterGraphicsEditor:
    def __init__(self, root):
        self.root = root
        self.root.title("OpenStreetMap")

        # Canvas for drawing
        self.canvas = tk.Canvas(self.root, width=800, height=600, bg="white")
        self.canvas.pack(fill=tk.BOTH, expand=True)

        # File Menu
        self.menu = tk.Menu(self.root)
        self.root.config(menu=self.menu)
        self.file_menu = tk.Menu(self.menu, tearoff=0)
        self.menu.add_cascade(label="File", menu=self.file_menu)
        self.file_menu.add_command(label="New", command=self.new_file)
        self.file_menu.add_command(label="Open...", command=self.open_file)
        self.file_menu.add_command(label="Save", command=self.save_file)
        self.file_menu.add_command(label="Save As...", command=self.save_as_file)
        self.file_menu.add_separator()
        self.file_menu.add_command(label="Exit", command=self.exit_program)

        # Help Menu
        self.help_menu = tk.Menu(self.menu, tearoff=0)
        self.menu.add_cascade(label="Help", menu=self.help_menu)
        self.help_menu.add_command(label="About", command=self.about)

    def new_file(self):
        # Logic to create a new file or clear the canvas
        self.canvas.delete("all")  # Clears the canvas

    def open_file(self):
        # Logic to open a file and display it on the canvas
        # This is just a placeholder
        messagebox.showinfo("Open", "Opening a file")

    def save_file(self):
        # Logic to save the current canvas content
        # This is just a placeholder
        messagebox.showinfo("Save", "Saving the file")

    def save_as_file(self):
        # Logic to save the canvas content with a new name/location
        # This is just a placeholder
        messagebox.showinfo("Save As", "Saving as a new file")

    def exit_program(self):
        if messagebox.askokcancel("Quit", "Are you sure you want to quit?"):
            self.root.destroy()

    def about(self):
        messagebox.showinfo("About", "Raster Graphics Editor\nVersion 1.0")


def main():
    root = tk.Tk()
    app = RasterGraphicsEditor(root)
    root.mainloop()


if __name__ == "__main__":
    main()