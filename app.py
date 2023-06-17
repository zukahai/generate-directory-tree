import tkinter as tk
from tkinter import filedialog
# import main.py
from mainv2 import save_file

def select_folder():
    root = tk.Tk()
    root.withdraw()
    folder_path = filedialog.askdirectory()
    if folder_path:
        print("Thư mục đã chọn:", folder_path)
        save_file(folder_path, "output.txt")
    else:
        print("Không có thư mục được chọn.")

# Gọi hàm để chọn thư mục
select_folder()
