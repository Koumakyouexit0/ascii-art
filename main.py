from PIL import Image
import os
import tkinter as tk
from tkinter import filedialog

def image_to_ascii(image_path, output_txt_path):
    chars = "@%#*+=-:. "
    img = Image.open(image_path)
    
    # resize imager 
    width, height = img.size
    aspect_ratio = height / width
    scale_factor = 0.1  # down 10%
    char_aspect_ratio = 2.0  
    
    new_width = max(1, int(width * scale_factor))
    new_height = max(1, int((height * scale_factor) / char_aspect_ratio))
    img = img.resize((new_width, new_height))
    
    # convert image to grayscale
    img = img.convert('L')
    
    # pixel to ascii
    ascii_art = "".join(chars[pixel // 32] for pixel in img.getdata())
    
    # ascii format
    ascii_art = "\n".join(
        ascii_art[i:(i + new_width)] for i in range(0, len(ascii_art), new_width)
    )
    
    # covert to txt
    with open(output_txt_path, 'w', encoding='utf-8') as f:
        f.write(ascii_art)
    
    print(f"ASCII art save in {output_txt_path}")
    return ascii_art

def select_file():
    root = tk.Tk()
    root.withdraw()
    return filedialog.askopenfilename(title="Select PNG", filetypes=[("PNG Files", "*.png")])

def select_save_location():
    root = tk.Tk()
    root.withdraw()
    return filedialog.asksaveasfilename(title="Save as", defaultextension=".txt", filetypes=[("Text Files", "*.txt")])

def main():
    print("=== PNG to ASCII Converter ===")
    image_path = select_file()
    if not image_path or not os.path.exists(image_path):
        print("ERROR: File not found!.")
        return
    
    output_txt_path = select_save_location()
    if not output_txt_path:
        print("ERROR: No save location selected.")
        return
    
    image_to_ascii(image_path, output_txt_path)

if __name__ == "__main__":
    main()
