import tkinter as tk
#from tkinter import ttk
import ttkbootstrap as ttk

def convert():
    miles = float(entry_int.get())
    kilometers = 1.609344 * miles
    output_string.set(kilometers)

#create a window
window = ttk.Window(themename = 'journal')
window.title('Demo')
window.geometry('400x150')

# title
title_label = ttk.Label(master = window, text = "Miles to kilometers", font = "Ariel 24 bold")
title_label.pack()

#input field
input_frame = ttk.Frame(master = window)
entry_int = tk.IntVar()
entry = ttk.Entry(master = input_frame, textvariable = entry_int)
button = ttk.Button(master = input_frame, text = "convert", command = convert)
entry.pack(side = 'left', padx = 10, pady = 10)
button.pack(side = 'left', padx = 10, pady = 10)
input_frame.pack()

output_string = tk.StringVar()
output_label = ttk.Label(master = window, textvariable = output_string)
output_label.pack()

#main loop
window.mainloop()

