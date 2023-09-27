# Program: Sales.py
# Programmer: Nneamaka Nwaigbo
# Date: September 17, 2021
# Description: Lab 3
# #############################################
days_of_week = ['Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat','Sun']

daily_sales = [1000, 2000, 3000, 4000, 5000, 6000, 7000]

print("Current Sales:\n")
print()
print(f"{days_of_week[0].title()}: \t${daily_sales[0]:,.2f}")
print(f"{days_of_week[1].title()}: \t${daily_sales[1]:,.2f}")
print(f"{days_of_week[2].title()}: \t${daily_sales[2]:,.2f}")
print(f"{days_of_week[3].title()}: \t${daily_sales[3]:,.2f}")
print(f"{days_of_week[4].title()}: \t${daily_sales[4]:,.2f}")
print(f"{days_of_week[5].title()}: \t${daily_sales[5]:,.2f}")
print(f"{days_of_week[6].title()}: \t${daily_sales[6]:,.2f}")
print()

print("Projected 5% Increase:")
print()

print(f"{days_of_week[0].title()}: \t${daily_sales[0] *1.05:,.2f}")
print(f"{days_of_week[1].title()}: \t${daily_sales[1] *1.05:,.2f}")
print(f"{days_of_week[2].title()}: \t${daily_sales[2] *1.05:,.2f}")
print(f"{days_of_week[3].title()}: \t${daily_sales[3] *1.05:,.2f}")
print(f"{days_of_week[4].title()}: \t${daily_sales[4] *1.05:,.2f}")
print(f"{days_of_week[5].title()}: \t${daily_sales[5] *1.05:,.2f}")
print(f"{days_of_week[6].title()}: \t${daily_sales[6] *1.05:,.2f}")
print()