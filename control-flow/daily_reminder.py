task = input("Enter your task: ").lower()
priority = input("Priority (high/medium/low): ").lower()
time_bound = input("Is it time-bound? (yes/no)").lower()

match priority:
   case a if priority == "high":
      if time_bound == "yes":
         print(f"Reminder: '{task}' is a {priority} priority task that requires immediate attention today!")
   case a if priority == "low":
      if time_bound == "no":
         print(f"Note: '{task}' is a {priority} priority task. Consider completing it when you have free time.")
   case _:
      print("It is not low nor high in terms of priority")