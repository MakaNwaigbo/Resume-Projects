def determine_season(input_temp):
	"""Recieved temp and returns probable season"""
	season = ""

	if input_temp > 130 or input_temp < -20:
		season = "invalid"
	elif input_temp >= 90:
		season = "summer"
	elif input_temp >= 70 and input_temp < 90:
		season = "spring"
	elif input_temp >= 50 and input_temp < 70:
		season = "fall"
	elif input_temp < 50:
		season = "winter"
	else:
		season = ""
    
	return season

temp = ('131', '90', '70', '50', '49')

print("Program - Determine Season")

repeat = True 

while repeat:
    temp = float(f"\nEnter the tempature (in Farenheit): ")
    output = f"\nBased on the tempature of {temp}, it is most likely {determine_season(temp)}"

print(output)