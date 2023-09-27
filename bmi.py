# Program: order.py
# Programmer: Nneamaka Nwaigbo
# Date: October 9, 2020
# Description: Lab 5
# ###########################################
names = ["bob", "betty", "liz", "chris"]
heights = [66, 62, 50, 70]
weights = [150, 100, 140, 110]

patient_0 = {'name': 'bob', "height": 66, "weight":150}
patient_1 = {'name': 'betty', "height": 62, "weight":100}
patient_2 = {'name': 'liz', "height": 50, "weight":140}
patient_3 = {'name': 'chris', "height": 70, "weight":110}

patients = [patient_0, patient_1, patient_2, patient_3]

print("BMI Program:\n")
print(f"NAME \tBMI \tCLASSIFICATION")
print()

for patient in patients: 
	bmi = (patient['weight'] * 703) / (patient['height'] * patient['height'])

for value in range(len(names)):
	bmi = (weights[value] * 703) /(heights[value] * heights[value])

	if bmi >= 25:
		classification = "Overweight"
	elif bmi >= 18.5:
		classification = "Healthy"
	elif bmi >= 16:
		classification = "Underweight"
	else:
		classification = "Invalid"

	print(f"{names[value].title()} \t{bmi:.2f} \t{classification}\n")

