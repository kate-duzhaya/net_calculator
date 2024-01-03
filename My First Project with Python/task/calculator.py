print("Earned amount:")
earned_amount = {'Bubblegum': 202, 'Toffee': 118, 'Ice cream': 2250, 'Milk chocolate': 1680,
                 'Doughnut': 1075, 'Pancake': 80}
total_income = 0
for key, value in earned_amount.items():
    print(f"{key}: ${value}")
    total_income += value
print()
print(f"Income: ${round(total_income, 2)}")
staff_expenses = input("Staff expenses:\n")
other_expenses = input("Other expenses:\n")
net_income = total_income - int(staff_expenses) - int(other_expenses)
print(f"Net income: ${net_income}")