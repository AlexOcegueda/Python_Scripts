#!/usr/bin/env python3

import tkinter as tk

'''''
  Name: Temperature Calculator
  Programmer: Alex Ocegueda -> Git: https://github.com/AlexOcegueda/Salary_Calculator
  Version: 1.0
  Description: Converts your input into celsius or fahrenheit. It uses these
                formulas:   c = (f - 32) * 5 / 9
                            f = c * 9 / 5 + 32
'''''

# Only returns true 
def get_valid_float(user_input):
    
    try:
        float(user_input)
        return True 
        
    except ValueError:
        error_label = tk.Label(root, text="Must Enter a Number!")
        error_label.place(relx=.25, rely=.7)



def convert_to_fahrenheit(celsius_input):
    blank = tk.Label(root, text='         ')
    blank.place(relx=.2, rely=.6)

    while get_valid_float(celsius_input):
        # this is the fahrenheit formula
        f = (float(celsius_input) * 9 / 5) + 32
        
        output = (f'Your Fahrenheit temp is {round(f, 1)}')
        f_output_label = tk.Label(root, text=output)
        f_output_label.place(relx=.2, rely=.6)
        break


def convert_to_celsius(fahrenheit_input):

    while get_valid_float(fahrenheit_input):
        # this is the fahrenheit formula
        c = (float(fahrenheit_input) * 5 / 9) + 32
        output = (f'Your Celsius temp is {round(c, 1)}')
        c_output_label = tk.Label(root, text=output)
        c_output_label.place(relx=.2, rely=.6)
        break

Font_tuple = ("Comic Sans MS", 23, "bold")

root = tk.Tk()
root.title("Temperature Converter")
title_label = tk.Label(root, text='Temperature Converter')
title_label.configure(font=Font_tuple)
title_label.place(relx=.03, rely=.1)
root.geometry("300x250")

temperature_label = tk.Label(root, text="Enter Temperature:", )
temperature_label.place(relx=.1, rely=.3)
temperature_entry = tk.Entry(root, width=3)
temperature_entry.place(relx=.6, rely=.3)

# Button which converts celsius input into fahrenheit
fahrenheit_label = tk.Button(root, text="C to F", bg='red', fg='white', command=lambda: convert_to_fahrenheit(temperature_entry.get()))
fahrenheit_label.place(relx=.2, rely=.4)

# Button which converts fahrenheit input into celsius
celsius_label = tk.Button(root, text="F to C", bg='blue', fg='white', command=lambda: convert_to_celsius(temperature_entry.get()))
celsius_label.place(relx=.6, rely=.4)

root.mainloop()
