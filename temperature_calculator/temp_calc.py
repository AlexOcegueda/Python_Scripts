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


def get_valid_float(user_input):
    try:
        float(user_input)
        return True

    except ValueError:
        error_label = tk.Label(root, text="Must Enter a Number!")
        error_label.pack()


def convert_to_fahrenheit(celsius_input):

    while get_valid_float(celsius_input):
        # this is the fahrenheit formula
        f = (float(celsius_input) * 9 / 5) + 32
        print(f)
        break


def convert_to_celsius(fahrenheit_input):

    while get_valid_float(fahrenheit_input):
        # this is the fahrenheit formula
        c = (float(fahrenheit_input) * 5 / 9) + 32
        print(c)
        break


root = tk.Tk()
root.title("Temperature Converter")
root.geometry("300x300")

temperature_label = tk.Label(root, text="Enter Temperature to Convert ", )
temperature_label.pack()
temperature_entry = tk.Entry(root, width=5)
temperature_entry.pack()

# Takes in amount of hours per week
fahrenheit_label = tk.Button(root, text="Fahrenheit", command=lambda: convert_to_fahrenheit(temperature_entry.get()))
fahrenheit_label.pack()

# Takes in amount of days per week 
celsius_label = tk.Button(root, text="Celsius", command=lambda: convert_to_celsius(temperature_entry.get()))
celsius_label.pack()

root.mainloop()
