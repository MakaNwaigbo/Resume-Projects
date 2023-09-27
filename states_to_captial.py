# Program: states_to_capital.py
# Programmer: Nneamaka Nwaigbo
# Date: October 16, 2020
# Description: Lab 5
# ###########################################
states_to_capitals = {'texas': 'austin',
					'new york': 'albany',
					'louisiana': 'baton rouge',
					'georgia': 'atlanta'}

print("State Capitals Listing:\n")

for key, value in states_to_capitals.items():
	print(f"The captial of {key.title()} is {value.title()}.")

print(f"\nNumber of states in this report: {len(states_to_capitals)}")

print("\nDelete New York.")
del states_to_capitals['new york']
print(f"Number of states in this report: {len(states_to_capitals)}")

states_to_capitals['michigan'] = 'lansing'

print("\nAdding Michigan and relisting.")

print()
for key, value in states_to_capitals.items():
	print(f"The captial of {key.title()} is {value.title()}.")

print(f"\nNumer of states in this report: {len(states_to_capitals)}")
print()