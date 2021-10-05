def solve(meal_cost, tip_percent, tax_percent):
    tips = meal_cost * tip_percent / 100
    tax = meal_cost * tax_percent / 100
    total = round(meal_cost + tips + tax)
    return total

meal_cost = float(input())
tip_percent = int(input())
tax_percent = int(input())
result = solve(meal_cost, tip_percent, tax_percent)
print(result)
