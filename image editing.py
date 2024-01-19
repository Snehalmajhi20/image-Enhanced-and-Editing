import tkinter as tk
from tkinter import filedialog
from PIL import Image, ImageTk, ImageEnhance, ImageFilter

class ImageEditor:
    def __init__(self, master):
        self.master = master
        self.master.title("Advanced Image Editor")

        self.original_image = None
        self.image = None

        self.background_color = "lightgray"

        # Create menu bar
        self.menu_bar = tk.Menu(master, bg=self.background_color, fg="black")
        master.config(menu=self.menu_bar)

        # Create File menu
        self.file_menu = tk.Menu(self.menu_bar, tearoff=0, bg=self.background_color, fg="black")
        self.menu_bar.add_cascade(label="File", menu=self.file_menu)
        self.file_menu.add_command(label="Open", command=self.open_image)
        self.file_menu.add_command(label="Save As", command=self.save_image)
        self.file_menu.add_separator()
        self.file_menu.add_command(label="Exit", command=master.destroy)

        # Create Edit menu
        self.edit_menu = tk.Menu(self.menu_bar, tearoff=0, bg=self.background_color, fg="black")
        self.menu_bar.add_cascade(label="Edit", menu=self.edit_menu)
        self.edit_menu.add_command(label="Enhance Contrast", command=self.enhance_contrast)
        self.edit_menu.add_command(label="Blur", command=self.apply_blur)
        self.edit_menu.add_command(label="Rotate 90 degrees", command=self.rotate_image)

        # Create View menu for background color customization
        self.view_menu = tk.Menu(self.menu_bar, tearoff=0, bg=self.background_color, fg="black")
        self.menu_bar.add_cascade(label="View", menu=self.view_menu)
        self.view_menu.add_command(label="Set Background Color", command=self.set_background_color)

        # Create canvas for displaying the image
        self.canvas = tk.Canvas(master, bg=self.background_color)
        self.canvas.pack(expand=tk.YES, fill=tk.BOTH, pady=10)

        # Create Enhance Scale
        self.enhance_scale = tk.Scale(master, label="Enhance Factor", from_=1, to=3, orient=tk.HORIZONTAL, resolution=0.1,
                                      bg=self.background_color, fg="black")
        self.enhance_scale.pack(pady=10)

    def open_image(self):
        file_path = filedialog.askopenfilename(filetypes=[("Image files", "*.png;*.jpg;*.jpeg;*.gif")])
        if file_path:
            self.original_image = Image.open(file_path)
            self.image = ImageTk.PhotoImage(self.original_image)
            self.canvas.config(width=self.image.width(), height=self.image.height())
            self.canvas.create_image(0, 0, anchor=tk.NW, image=self.image)

    def save_image(self):
        if self.original_image:
            file_path = filedialog.asksaveasfilename(defaultextension=".png", filetypes=[("PNG files", "*.png")])
            if file_path:
                self.original_image.save(file_path)

    def enhance_contrast(self):
        if self.original_image:
            factor = self.enhance_scale.get()
            enhanced_image = ImageEnhance.Contrast(self.original_image).enhance(factor)
            self.image = ImageTk.PhotoImage(enhanced_image)
            self.canvas.create_image(0, 0, anchor=tk.NW, image=self.image)

    def apply_blur(self):
        if self.original_image:
            blurred_image = self.original_image.filter(ImageFilter.BLUR)
            self.image = ImageTk.PhotoImage(blurred_image)
            self.canvas.create_image(0, 0, anchor=tk.NW, image=self.image)

    def rotate_image(self):
        if self.original_image:
            rotated_image = self.original_image.rotate(90)
            self.image = ImageTk.PhotoImage(rotated_image)
            self.canvas.create_image(0, 0, anchor=tk.NW, image=self.image)

    def set_background_color(self):
        new_color = tk.colorchooser.askcolor()[1]  # Open color chooser dialog
        if new_color:
            self.background_color = new_color
            self.menu_bar.config(bg=self.background_color, fg="black")
            self.file_menu.config(bg=self.background_color, fg="black")
            self.edit_menu.config(bg=self.background_color, fg="black")
            self.view_menu.config(bg=self.background_color, fg="black")
            self.canvas.config(bg=self.background_color)
            self.enhance_scale.config(bg=self.background_color, fg="black")

if __name__ == "__main__":
    root = tk.Tk()
    app = ImageEditor(root)
    root.mainloop()
