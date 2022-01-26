import tkinter as tk

def calculate_adjusted_salary():
  # calculate adjusted numbers
  print('success')


def main():
  root = tk.Tk()
  root.title("Salary Calculator")
  root.geometry("300x300")

  # Takes in amount of Salary
  salary_label = tk.Label(text="Salary Amount")
  salary_label.pack()
  salary_entry = tk.Entry(root)
  salary_entry.pack()
 

  # Takes in amount of hours per week 
  hours_per_week_label = tk.Label(text="Hours per Week Amount")
  hours_per_week_label.pack()
  hours_per_week_entry = tk.Entry(root)
  hours_per_week_entry.pack()


  # Takes in amount of holiday days off 
  holiday_days_label = tk.Label(text="Holiday days per year off")
  holiday_days_label.pack()
  holiday_days_entry = tk.Entry(root)
  holiday_days_entry.pack()


  # Takes in amount of vacation days off
  vacations_days_label = tk.Label(text="Vacation days per year off")
  vacations_days_label.pack()
  vacation_days_entry = tk.Entry(root)
  vacation_days_entry.pack()


  calculate_button = tk.Button(root, text='Calculate', command=calculate_adjusted_salary)
  calculate_button.pack()


  root.mainloop()


if __name__ == "__main__":
  main()



