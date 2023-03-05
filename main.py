import tkinter as tk
from tkinter import filedialog
from PIL import Image

root = tk.Tk()
root.title('Easy WebP to JPEG Converter')
root.geometry('400x200')

select_label = tk.Label(root, text="Click 'Select File' and choose the WebP you wish to convert")

select_button = tk.Button(root, text='Select File', font=('verdana', 12))


def select_file():
    file_path = filedialog.askopenfilename(title="Select a WebP file",
                                           filetypes=(("WebP files", "*.webp"), ("all files", "*.*")))
    if file_path:
        convert_file(file_path)


def convert_file(file_path):
    webp_image = Image.open(file_path)
    jpg_file_path = filedialog.asksaveasfilename(title="Save converted file",
                                                 initialfile=file_path.split("/")[-1].replace(".webp", ".jpg"),
                                                 filetypes=(("JPEG files", "*.jpg"), ("all files", "*.*")))
    if jpg_file_path:
        webp_image.save(jpg_file_path, "JPEG")
        select_label.config(text=f"Converted {file_path} to {jpg_file_path}")
        root.destroy()


select_button['command'] = select_file

select_label.pack()

select_button.pack()

root.mainloop()
