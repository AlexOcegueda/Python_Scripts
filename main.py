from functools import partial
import tkinter as tk
from turtle import onclick

def calculate_unadjusted_salary(Salary, hours_per_week):
  
  # This assumes 5 working day schedule for the year
  working_days_per_year = 52*5
  
  unadjusted_salary = Salary*hours_per_week*working_days_per_year

  return unadjusted_salary

def calculate(Salary, hours_per_week, holidays, vacations):
  
  # calculate adjusted numbers
  print('Success')
  


def main():
  root = tk.Tk()
  root.title("Salary Calculator")
  root.geometry("300x300")


  # Takes in amount of Salary
  salary_label = tk.Label(text="Salary Amount per Hour")
  salary_label.pack()
  salary_entry = tk.Entry(root)
  salary_entry.pack()
 

  # Takes in amount of hours per week 
  hours_per_week_label = tk.Label(text="Hours per Week")
  hours_per_week_label.pack()
  hours_per_week_entry = tk.Entry(root)
  hours_per_week_entry.pack()


  # Takes in amount of holiday days off 
  holiday_label = tk.Label(text="Holiday per year")
  holiday_label.pack()
  holiday_entry = tk.Entry(root)
  holiday_entry.pack()


  # Takes in amount of vacation days off
  vacations_days_label = tk.Label(text="Vacation days per year")
  vacations_days_label.pack()
  vacation_days_entry = tk.Entry(root)
  vacation_days_entry.pack()


  calculate_button = tk.Button(root, text='Calculate', command=partial(calculate, salary_entry, hours_per_week_entry, holiday_entry, vacation_days_entry))
  calculate_button.pack()


  root.mainloop()


if __name__ == "__main__":
  main()



