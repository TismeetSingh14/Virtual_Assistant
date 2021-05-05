import tkinter as tk
from tkinter import filedialog
from PIL import Image

def jpegToPng():
    root = tk.Tk()
    root.withdraw()
    file_path = filedialog.askopenfilename()
    image = Image.open(file_path)
    format_inp = input("Input File Format here")
    image.save("Image." + (str(format_inp)))