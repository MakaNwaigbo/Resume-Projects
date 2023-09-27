# Program: bmi_dict.py
# Programmer: Nneamaka Nwaigbo
# Date: October 16, 2020
# Description: Lab 5
# ###########################################
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
	if bmi >= 25:
		classification = "Overweight"
	elif bmi >= 18.5:
		classification = "Healthy"
	elif bmi >= 16:
		classification = "Underweight"
	else:
		classification = "Invalid"

	print(f"{patient['name'].title()} \t{bmi:.2f} \t{classification}\n")

