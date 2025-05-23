# Prompt the user for income and expenses
monthly income = float(input("Enter your monthly income: "))
monthly expenses = float(input("Enter your total monthly expenses: "))

# Calculate monthly savings
monthly_savings = monthly income - monthly expenses

# Calculate projected annual savings with 5% interest
annual_savings = monthly_savings * 12
projected_savings = annual_savings + (annual_savings * 0.05)

# Print the results
print(f"Your monthly savings are ${monthly_savings:.2f}.")
print(f"Projected savings after one year, with interest, is: ${projected_savings:.2f}.")
