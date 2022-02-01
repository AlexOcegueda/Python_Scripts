from functools import partial
import tkinter as tk

def calculate_unadjusted_salary(salary, hours_per_week):
  
  # This assumes 5 working day schedule for the year
  working_days_per_year = 52*5
  
  unadjusted_salary = int(salary)*int(hours_per_week)*int(working_days_per_year)

  return unadjusted_salary

def calculate_adjusted_salary(salary, hours_per_week, holidays, vacations):
  
  # This assumes 5 working day schedule for the year
  working_days_per_year = 52*5
  
  adjusted_days_off = int(holidays) + int(vacations)

  adjusted_salary = int(salary)*int(hours_per_week)*(int(working_days_per_year) - int(adjusted_days_off))

  return adjusted_salary

# Calculates their unadjusted salary and adjusted salary
def calculate(salary, hours, holidays, vacations):
  
  print(calculate_unadjusted_salary(salary, hours))
  print(calculate_adjusted_salary(salary, hours, holidays, vacations))


root = tk.Tk()
root.title("Salary Calculator")
root.geometry("300x300")


# Takes in amount of Salary
salary_label = tk.Label(root, text="Salary Amount per Hour")
salary_label.place(rely=.25, relx=.30, anchor=tk.CENTER)
salary_entry = tk.Entry(root)
salary_entry.place(width=100, rely=.25, relx=.75, anchor=tk.CENTER)


# Takes in amount of hours per week 
hours_per_week_label = tk.Label(root, text="Hours per Week")
#hours_per_week_label.pack()
hours_per_week_entry = tk.Entry(root)
#hours_per_week_entry.pack()


# Takes in amount of holiday days off 
holiday_label = tk.Label(root, text="Holiday per year")
#holiday_label.pack()
holiday_entry = tk.Entry(root)
#holiday_entry.pack()


# Takes in amount of vacation days off
vacations_days_label = tk.Label(root, text="Vacation days per year")
#vacations_days_label.pack()
vacation_days_entry = tk.Entry(root)
#vacation_days_entry.pack()


calculate_button = tk.Button(root, text='Calculate', command=lambda: calculate(salary_entry.get(), hours_per_week_entry.get(), holiday_entry.get(), vacation_days_entry.get()))
#calculate_button.pack()


root.mainloop()




