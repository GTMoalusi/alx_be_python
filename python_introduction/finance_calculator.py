#User inputs
monthly_income = int(input(""Enter your monthly income: ))
monthly_expenses = int(input("Enter your total monthly expenses: "))

#Calculate monthly savings
monthly_savings = monthly_income - monthly_expenses

#Project annual savings
rate = (5/100)
year = 12 #1 year is equal to 12 month
projected_savings = monthly_savings * year + (monthly_savings * year * rate)

#Output
print(f"Projected savings after one year, with interest, is ${projected_savings}.")
