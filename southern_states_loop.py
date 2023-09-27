# Program: southern_states_loop.py
# Programmer: Nneamaka Nwaigbo
# Date: October 30, 2021
# Description: Lab 7
# ##################################################################
southern_states = ['virginia', 'tennessee', 'arkansas', 'louisiana',
				 'north carolina', 'south carolina', 'mississippi', 
				 'alabama', 'georgia', 'florida', 'texas']

print("Report - Southern United States\n")

print("UNSORTED:\n")
for state in southern_states:
	print(state.title())

print(f"\nLast state on this unsorted list: {southern_states[-1].title()}\n")

print("SORTED:\n")
southern_states.sort()

current_state = 0
while current_state < len(southern_states):
	print(f"{southern_states[current_state].title()}")
	current_state = current_state + 1

print(f"\nLast state on this ordered list: {southern_states[-1].title()}\n")

print(f"Number of Southern States: {len(southern_states)}")

print("\nSource: simple.wikipedia.org/wiki/Southern_United_States")
print()