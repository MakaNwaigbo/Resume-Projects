# Program: souther_states.py
# Programmer: Nneamaka Nwaigbo
# Date: September 17, 2021
# Description: Lab 3
# #############################################
southern_states = ['virginia', 'tennessee', 'arkansas', 'louisiana',
				 'north carolina', 'south carolina', 'mississippi', 
				 'alabama', 'georgia', 'florida', 'texas']

print("Report - Southern United States\n")

print("UNSORTED:\n")
print(f"{southern_states[0].title()}")
print(f"{southern_states[1].title()}")
print(f"{southern_states[2].title()}")
print(f"{southern_states[3].title()}")
print(f"{southern_states[4].title()}")
print(f"{southern_states[5].title()}")
print(f"{southern_states[6].title()}")
print(f"{southern_states[7].title()}")
print(f"{southern_states[8].title()}")
print(f"{southern_states[9].title()}")
print(f"{southern_states[10].title()}")

print(f"\nLast state on this unsorted list: {southern_states[-1].title()}\n")

southern_states.sort()
print("SORTED:\n")
print(f"{southern_states[0].title()}")
print(f"{southern_states[1].title()}")
print(f"{southern_states[2].title()}")
print(f"{southern_states[3].title()}")
print(f"{southern_states[4].title()}")
print(f"{southern_states[5].title()}")
print(f"{southern_states[6].title()}")
print(f"{southern_states[7].title()}")
print(f"{southern_states[8].title()}")
print(f"{southern_states[9].title()}")
print(f"{southern_states[10].title()}")

print(f"\nLast state on this sorted list: {southern_states[-1].title()}\n")

print(f"\nNumber of Southern States: {len(southern_states)}")

print("\nSource: simple.wikipedia.org/wiki/Southern_United_States")
print()