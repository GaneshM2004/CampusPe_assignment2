print("Grade Calculator")
print("=" * 50)

# enter marks for 5 subjects (usually out of 100)
subject1 = float(input("Enter marks for English: "))
subject2 = float(input("Enter marks for Kannada: "))
subject3 = float(input("Enter marks for Maths: "))
subject4 = float(input("Enter marks for Science: "))
subject5 = float(input("Enter marks for Social Studies: "))

# calculate total and percentage
totalmarks = subject1 + subject2 + subject3 + subject4 + subject5
percentage = (totalmarks / 500) * 100

#use conditional statement to check grades
if percentage >= 90:
    grade = "A+"
    gradename = "Outstanding"
elif percentage >= 80:
    grade = "A"
    gradename = "Excellent"
elif percentage >= 70:
    grade = "B"
    gradename = "Good"
elif percentage >= 60:
    grade = "C"
    gradename = "Average"
elif percentage >= 50:
    grade = "D"
    gradename = "Pass"
else:
    grade = "F"
    gradename = "Fail"

# fail if under 40 in any subject
if subject1 >= 40 and subject2 >= 40 and subject3 >= 40 and subject4 >= 40 and subject5 >= 40:
    result = "PASS"
else:
    result = "FAIL"

# print output
print("\n" + "=" * 50)
print("Results")
print("=" * 50)
print("English: ",(subject1))
print("Kannada: ",(subject2))
print("Maths: ",(subject3))
print("Science: ",(subject4))
print("Social Studies: ",(subject5))
print("-" * 50)
print("Total Marks: ",(totalmarks))
print("Percentage: ",round(percentage,2),"%")
print("Grade: ",grade,"-",gradename)
print("Result:",result)
print("=" * 50)
