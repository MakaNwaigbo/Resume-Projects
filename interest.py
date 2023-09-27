#Program: interest.py
#Programmer: Nneamaka Nwaigbo
#Date: September 11, 2021
#Description: Lab 2
# ########################################
years = 15
rate = 6
loan = 5000

interest = loan * (rate/100) *years

print(f"Loan amount: \t${loan}")

print(f"Interest rate: \t{rate}%")

print(f"No. of Years: \t{years}") 

print(f"Interest paid: \t${interest:,.2f}")
