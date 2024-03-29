##A-Program
# 1-Ask for grades for 5 subjects and convert them to integers
Grade_sub1 = int(input("Enter the grade of the subject 1: "))
Grade_sub2 = int(input("Enter the grade of the subject 2: "))
Grade_sub3 = int(input("Enter the grade of the subject 3: "))
Grade_sub4 = int(input("Enter the grade of the subject 4: "))
Grade_sub5 = int(input("Enter the grade of the subject 5: "))

# 2-Calculate the sum of all grades
sum_grade = Grade_sub1 + Grade_sub2 + Grade_sub3 + Grade_sub4 + Grade_sub5

# 3- Calculate the Average grade of 5 subjects
Average_grade = sum_grade / 5

# 4- Determine and print the letter grade based on Average_grade
if Average_grade > 90:
    print("Grade A")
elif Average_grade > 80:
    print("Grade B")
elif Average_grade > 70:
    print("Grade C")
elif Average_grade > 60:
    print("Grade D")
else:
    print("Grade E - Failed")


##B-Program
"""Write a program that will that will ask student for their grade in 5 subject
calculate your average grade and print the grade from A-E
A>90
B>80
C>70
D>60
E===Failed"""
# #Program to execute
# #1-The grade in each subject should be known, 
Grade_sub1 = int(input("Enter the grade of the subject1:"))
Grade_sub2 = int(input("Enter the grade of the subject2:"))
Grade_sub3 = int(input("Enter the grade of the subject3:"))
Grade_sub4 = int(input("Enter the grade of the subject4:"))
Grade_sub5 = int(input("Enter the grade of the subject5:"))
# #2-then we calculate the sum_grade of all grades
sum_grade = Grade_sub1 + Grade_sub2 + Grade_sub3 + Grade_sub4 + Grade_sub5
print(sum_grade)
# #3- Calculate the Average_grade of 5 subject
Average_grade= sum_grade / 5
print(Average_grade)
# Tell the grade of student
if Average_grade>90:
    print("Grade A")
if Average_grade>80:
    print("Grade B")
if Average_grade>70:
    print("Grade C")    
if Average_grade>60:
    print("Grade D")
elif Average_grade<=60:
    print ("Grade E")
else:
    print("Error")
