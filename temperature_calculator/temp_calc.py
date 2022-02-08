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

def calculate_adjusted_salary(salary, total_hours_per_week, days_per_week, holidays, vacations):

    print('Null')

# Calculates their unadjusted salary and adjusted salary and displays it on screen
def calculate(salary, total_hours_per_week, days_per_week, holidays, vacations, root):
  
  print('Null')

def convert_to_celsius():

    print("cel")

root = tk.Tk()
root.title("Temperature Converter")
root.geometry("300x300")


temperature_label = tk.Label(root, text="Enter Temperature to Convert ")
temperature_label.pack()
temperature_entry = tk.Entry(root, width=5)
temperature_entry.pack()


# Takes in amount of hours per week 
fahrenheit_label = tk.Button(root, text="Fahrenheit")
fahrenheit_label.pack()

# Takes in amount of days per week 
celsius_label = tk.Button(root, text="Celsius")
celsius_label.pack()

calculate_button = tk.Button(root, text='Calculate', command=lambda: print('gt'))
calculate_button.pack()


root.mainloop()




