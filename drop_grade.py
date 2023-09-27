#Program: drop_grade.py
#Programmer: Nneamaka Nwaigbo
#Date: October 1, 2021
#Description: Lab 4
# ########################################

grades = [100, 80, 70, 60, 90]

print("DROP LOWEST GRADE PROGRAM \n")

print("Grades:")
for grade in grades:
	print(grade) 

total = sum(grades)
average = total/len(grades)

print(f'Number of grades: {len(grades)}')
print(f'Average: {average:,.2f}')

lowest_grade = min(grades)
print(f'Lowest Grade: {lowest_grade}')
grade_lowest_index = grades.index(lowest_grade)
del grades[grade_lowest_index]


print("\nLOWEST GRADE DROPPED:")
print("\nGrades:")
for grade in grades:
	print(grade) 

total = sum(grades)
average = total/len(grades)

print(f'Number of grades: {len(grades)}')
print(f'Average: {average:,.2f}')

lowest_grade = min(grades)
print(f'Lowest Grade: {lowest_grade}')
print()

