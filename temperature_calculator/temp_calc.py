#!/usr/bin/env python3


import tkinter as tk

'''''
  Name: Temperature Calculator
  Programmer: Alex Ocegueda -> Git: https://github.com/AlexOcegueda/Salary_Calculator
  Version: 1.0
  Description: Converts your input into celsius or fahrenheit. It only accepts values 
                between 0 and 250. 

                It uses these formulas: c = (f - 32) * 5 / 9
                                        f = (c * 9 / 5) + 32
'''''


def destroy_label(label):
    label.destroy()


def get_valid_range():

    if 0 < float(temperature_entry.get()) < 250:
        return True
    else:
        error_message = tk.Label(root, text='Limit 0 - 250')
        error_message.place(relx=.3, rely=.7)
        root.after(2500, destroy_label, error_message)


# Only returns true if the
def get_valid_float():
    try:
        float(temperature_entry.get())
        return True

    except ValueError:
        error_message = tk.Label(root, text="Must Enter a Number!")
        error_message.place(relx=.25, rely=.7)
        root.after(2500, destroy_label, error_message)


# converts celsius to fahrenheit
def convert_to_fahrenheit():
    if get_valid_float():

        if get_valid_range():
            # this is the fahrenheit formula
            f = (float(temperature_entry.get()) * 9 / 5) + 32

            # Displays conversion rounded to 1 decimal place
            output = f'Your F temp is {round(f, 1)}'
            f_output_label = tk.Label(root, text=output)
            f_output_label.place(relx=.25, rely=.6)
            root.after(4000, destroy_label, f_output_label)


# converts fahrenheit to Celsius
def convert_to_celsius():
    if get_valid_float():

        if get_valid_range():
            # this is the fahrenheit formula
            c = (float(temperature_entry.get()) * 5 / 9) + 32

            # Displays conversion rounded to 1 decimal place
            output = f'Your C temp is {round(c, 1)}'

            c_output_label = tk.Label(root, text=output)
            c_output_label.place(relx=.25, rely=.6)
            root.after(4000, destroy_label, c_output_label)


def main():
    
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
    temperature_entry.place(relx=.7, rely=.3)

    # Button which converts celsius input into fahrenheit
    fahrenheit_label = tk.Button(root, text="C to F", bg='red', fg='white', command=convert_to_fahrenheit)
    fahrenheit_label.place(relx=.2, rely=.4)

    # Button which converts fahrenheit input into celsius
    celsius_label = tk.Button(root, text="F to C", bg='blue', fg='white', command=convert_to_celsius)
    celsius_label.place(relx=.6, rely=.4)

    root.mainloop()


if __name__ == '__main__':
    main()



