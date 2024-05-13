"""
write a py program that calclate the gpa of the students based on their grades inthree subjects ; Maths, Sci and Eng

assume grades are on scale of zero to 100 and gpa is calculated as average of these three grades
Requirement:1)Prompt the user to input the grades 
            2)Calculate the Gpa using formular - GPA(maths+science+english)/3
            3)Print the calculated gpa with two decimal points
"""


#Prompt user for the grades
maths_grade =int(input("Enter the Maths Grade: "))
science_grade =int(input("Enter the Science Grade: "))
english_grade =int(input("Enter the English Grade: "))

#Find the total of the three grades
total_grade = maths_grade + science_grade + english_grade

#Print total
print("The total marks are: ")

#Calculating the GPA ((Maths+SCience+English)/3)
students_gpa = total_grade/3

#print the GPA
print("The Student Grade Point Average is: " + str(round(students_gpa,2)))

#interpolating the variable to the string
print(f"The Student Grade Point Average is: {students_gpa:.2f}")

print(format(students_gpa, ".2f"))

