#!/usr/bin/env python3

"""
    Converts your input into celsius or fahrenheit. It only accepts values
    between 0 and 250.

    It uses these formulas: c = (f - 32) * 5 / 9
                           f = (c * 9 / 5) + 32
"""

import tkinter as tk

__program_name__ = "Temperature Converter"
__author__ = 'Alex Ocegueda'
__version__ = '2.0'
__github__ = "https://github.com/AlexOcegueda/Python_Assignments/temp_calc"


def destroy_label(label):
    label.destroy()


# Only returns true if user enters numbers in the range of 0 - 250
def get_valid_range(root, temperature_entry):
    if 0 < float(temperature_entry.get()) < 250:
        return True
    else:
        error_message = tk.Label(root, text='Limit 0 - 250')
        error_message.place(relx=.3, rely=.7)
        root.after(2500, destroy_label, error_message)


# Only returns true if the user entered a string with NO letters or symbols
def get_valid_float(root, temperature_entry):
    try:
        float(temperature_entry.get())
        return True

    except ValueError:
        error_message = tk.Label(root, text="Must Enter a Number!")
        error_message.place(relx=.25, rely=.7)
        root.after(2500, destroy_label, error_message)


# converts celsius to fahrenheit
def convert_to_fahrenheit(root, temperature_entry):
    if get_valid_float(root, temperature_entry):

        if get_valid_range(root, temperature_entry):
            # this is the fahrenheit formula
            f = (float(temperature_entry.get()) * 9 / 5) + 32

            # Displays conversion rounded to 1 decimal place
            output = f'Your F temp is {round(f, 1)}'
            f_output_label = tk.Label(root, text=output)
            f_output_label.place(relx=.25, rely=.6)
            root.after(3000, destroy_label, f_output_label)


# converts fahrenheit to Celsius
def convert_to_celsius(root, temperature_entry):
    if get_valid_float(root, temperature_entry):

        if get_valid_range(root, temperature_entry):
            # this is the fahrenheit formula
            c = (float(temperature_entry.get()) * 5 / 9) + 32

            # Displays conversion rounded to 1 decimal place
            output = f'Your C temp is {round(c, 1)}'

            c_output_label = tk.Label(root, text=output)
            c_output_label.place(relx=.25, rely=.6)
            root.after(3000, destroy_label, c_output_label)


def display_title(root):
    title_font = ("Comic Sans MS", 23, "bold")

    title_label = tk.Label(root, text='Temperature Converter')
    title_label.configure(font=title_font)
    title_label.place(relx=.03, rely=.1)


# displays and returns the user's input
def display_temperature_input(root):
    # Label and button to take input to convert
    temperature_label = tk.Label(root, text="Enter Temperature:", )
    temperature_label.place(relx=.1, rely=.3)
    temperature_entry = tk.Entry(root, width=3)
    temperature_entry.place(relx=.7, rely=.3)
    return temperature_entry


def display_fahrenheit_button(root, user_input):
    fahrenheit_label = tk.Button(root, text="C to F", bg='red', fg='white',
                                 command=lambda: convert_to_fahrenheit(root, user_input))
    fahrenheit_label.place(relx=.2, rely=.4)


def display_celsius_button(root, user_input):
    celsius_label = tk.Button(root, text="F to C", bg='blue', fg='white',
                              command=lambda: convert_to_celsius(root, user_input))
    celsius_label.place(relx=.6, rely=.4)


def main():
    root = tk.Tk()
    root.title("Temperature Converter")
    root.geometry("300x250")
    display_title(root)

    # displays temperature input for users and assigns it
    user_input = display_temperature_input(root)

    # Button which converts celsius input into fahrenheit when clicked
    display_fahrenheit_button(root, user_input)

    # Button which converts fahrenheit input into celsius when clicked
    display_celsius_button(root, user_input)

    root.mainloop()


if __name__ == '__main__':
    main()
