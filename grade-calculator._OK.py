# 1-The grade in each subject should be known,
Grade_sub1 = float(input("Enter the grade of the subject 1: "))  # Use float for decimal input
Grade_sub2 = float(input("Enter the grade of the subject 2: "))
Grade_sub3 = float(input("Enter the grade of the subject 3: "))
Grade_sub4 = float(input("Enter the grade of the subject 4: "))
Grade_sub5 = float(input("Enter the grade of the subject 5: "))

# 2-Then we calculate the sum of all grades
sum_grade = Grade_sub1 + Grade_sub2 + Grade_sub3 + Grade_sub4 + Grade_sub5
# 3- Calculate the Average grade of 5 subjects
Average_grade = sum_grade / 5
print(f"Average grade: {Average_grade}")

# Tell the grade of student
if Average_grade >= 90:
    print("The student is: Grade A")
elif Average_grade >= 80:
    print("The student is: Grade B")
elif Average_grade >= 70:
    print("The student is: Grade C")
elif Average_grade >= 60:
    print("The student is: Grade D")
else:
    print("The student is: Grade E - Failed")
