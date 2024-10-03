import tkinter as tk
#from tkinter import ttk
import ttkbootstrap as ttk

def milesConvert():
    print("mile")
    miles = float(entry_int.get())
    kilometers = 1.609344 * miles
    output_string.set(kilometers)

def kilometersConvert():
    print("kilo")
    kilometers = float(entry_int.get())
    miles = kilometers * 0.621371
    output_string.set(miles)

def swap():
    if title_string.get() == "Miles to kilometers":
        title_string.set("Kilometers to miles")
        button.config(command = kilometersConvert)
    else:
        title_string.set("Miles to kilometers")
        button.config(command = milesConvert)



#create a window
window = ttk.Window(themename = 'journal')
window.title('Demo')
window.geometry('400x150')

# title
title_string = tk.StringVar(value = 'Miles to kilometers')
title_label = ttk.Label(master = window, textvariable = title_string, font = "Ariel 24 bold")
title_label.pack()

#input field
input_frame = ttk.Frame(master = window)
entry_int = tk.DoubleVar()
entry = ttk.Entry(master = input_frame, textvariable = entry_int)
button = ttk.Button(master = input_frame, text = "convert", command = milesConvert)
entry.pack(side = 'left', padx = 10, pady = 10)
button.pack(side = 'left', padx = 10, pady = 10)
input_frame.pack()

output_frame = ttk.Frame(master = window)
output_string = tk.StringVar()
output_label = ttk.Label(master = output_frame, textvariable = output_string)
swap_button = ttk.Button(master = output_frame, text = "swap", command = swap)
output_frame.pack()
output_label.pack(side = 'left', padx = (10,40), pady = 10)
swap_button.pack(side = 'left', pady = 10)


#main loop
window.mainloop()

