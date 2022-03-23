#!/usr/bin/env python3

import tkinter as tk

'''''

    Takes in your Salary per hour, total hours worked per week, how many days you work, and 
    your holidays and vacations. It will display your salary before and after holidays are 
    deducted.
'''''

__program_name__ = "Salary Calculator"
__author__ = "Alex Ocegueda"
__version__ = "2.0"
__github__ = "https://github.com/AlexOcegueda/Python_Assignments/salary_calculator"


def calculate_unadjusted_salary(salary, total_hours_per_week, days_per_week):
    # hours worked on an average day
    daily_hours = int(total_hours_per_week) / int(days_per_week)

    # This assumes 5 working day schedule for the year
    working_days_per_year = 52 * int(days_per_week)

    unadjusted_salary = int(salary) * int(daily_hours) * int(working_days_per_year)

    return unadjusted_salary


def calculate_adjusted_salary(salary, total_hours_per_week, days_per_week, holidays, vacations):
    # hours worked on an average day
    daily_hours = int(total_hours_per_week) / int(days_per_week)

    # This assumes 5 working day schedule for the year
    working_days_per_year = 52 * int(days_per_week)

    adjusted_days_off = int(working_days_per_year) - (int(holidays) + int(vacations))

    adjusted_salary = int(salary) * int(daily_hours) * int(adjusted_days_off)

    return adjusted_salary


# Calculates their unadjusted salary and adjusted salary and displays it on screen
def calculate(salary, total_hours_per_week, days_per_week, holidays, vacations, root):
    adjusted_salary_label = tk.Label(root, text="Your adjusted salary is")
    adjusted_salary = tk.Label(root,
                               text=calculate_adjusted_salary(salary, total_hours_per_week, days_per_week, holidays,
                                                              vacations))
    unadjusted_salary_label = tk.Label(root, text="Your unadjusted salary is")
    unadjusted_salary = tk.Label(root, text=calculate_unadjusted_salary(salary, total_hours_per_week, days_per_week))

    adjusted_salary_label.pack()
    adjusted_salary.pack()
    unadjusted_salary_label.pack()
    unadjusted_salary.pack()


def main():
    root = tk.Tk()
    root.title("Salary Calculator")
    root.geometry("300x300")

    # Takes in amount of Salary
    salary_per_hour_label = tk.Label(root, text="Salary per Hour")
    salary_per_hour_label.pack()
    salary_per_hour_entry = tk.Entry(root)
    salary_per_hour_entry.pack()

    # Takes in amount of hours per week
    total_hours_per_week_label = tk.Label(root, text="Hours per Week")
    total_hours_per_week_label.pack()
    total_hours_per_week_entry = tk.Entry(root)
    total_hours_per_week_entry.pack()

    # Takes in amount of days per week
    days_per_week_label = tk.Label(root, text="Days per Week")
    days_per_week_label.pack()
    days_per_week_entry = tk.Entry(root)
    days_per_week_entry.pack()

    # Takes in amount of holiday days off
    holidays_off_per_year_label = tk.Label(root, text="Holiday per year")
    holidays_off_per_year_label.pack()
    holidays_off_per_year_entry = tk.Entry(root)
    holidays_off_per_year_entry.pack()

    # Takes in amount of vacation days off
    vacation_days_off_per_year_label = tk.Label(root, text="Vacation days per year")
    vacation_days_off_per_year_label.pack()
    vacation_days_entry = tk.Entry(root)
    vacation_days_entry.pack()

    calculate_button = tk.Button(root, text='Calculate',
                                 command=lambda: calculate(salary_entry.get(), total_hours_per_week_entry.get(),
                                                           days_per_week_entry.get(), holiday_entry.get(),
                                                           vacation_days_entry.get(), root))
    calculate_button.pack()

    root.mainloop()


if __name__ == '__main__':
    main()

