# Program: interest_due.py
# Programmer: Nneamaka Nwaigbo
# Date: October 30, 2021
# Description: Lab 7
# ###########################################
print("Program - Calculate Interest on Loan:")

repeat = True

while repeat:
    amount = input("\nHow many dollars do you wish to borrow? ")
    amount = float(amount)
    interest_rate = float(input("What is the interest rate? "))
    years = int(input("How many years would you take the loan? "))

    total_interest = amount * (interest_rate/100) * years

    output = f"\nIf you borrow ${amount:,.2f} at an interest rate of {interest_rate}%"
    output += f"\nfor {years} years, you will pay ${total_interest:,.2f} in interest."

    print(output)

    again = input("\nWould you like to run another calculation? (y/n)")
    if again == 'n':
        repeat = False

print("\nThanks for using the program. Goodbye!")