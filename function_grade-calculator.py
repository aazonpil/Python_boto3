def grade_calculation(Average_grade):
#Calculate the Average grade of 5 subjects
    Average_grade = (Grade_math + Grade_English + Grade_Chemitry + Grade_Bio + Grade_Physic)/5
    return Average_grade




#Main
    # 1-The grade in each subject should be known,
    Grade_math = float(input("Enter the grade of the subject 1: "))  # Use float for decimal input
    Grade_English= float(input("Enter the grade of the subject 2: ")) 
    Grade_Chemitry= float(input("Enter the grade of the subject 3: "))
    Grade_Bio= float(input("Enter the grade of the subject 4: "))
    Grade_Physic= float(input("Enter the grade of the subject 5: "))
    
# call the function
  # Display the output automatically
Average_grade =(Grade_math + Grade_English + Grade_Chemitry + Grade_Bio + Grade_Physic)/5
print(f"Average_grade is :{Average_grade}")
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


def grade_calculation(Grade_math, Grade_English, Grade_Chemitry, Grade_Bio, Grade_Physic):
    # Calculate the Average grade of 5 subjects
    Average_grade = (Grade_math + Grade_English + Grade_Chemitry + Grade_Bio + Grade_Physic) / 5
    return Average_grade

# Main
# 1- The grade in each subject should be known,
Grade_math = float(input("Enter the grade of Math: "))  # Use float for decimal input
Grade_English = float(input("Enter the grade of English: "))
Grade_Chemitry = float(input("Enter the grade of Chemistry: "))
Grade_Bio = float(input("Enter the grade of Biology: "))
Grade_Physic = float(input("Enter the grade of Physics: "))

# 2- Call the function and calculate average grade
Average_grade = grade_calculation(Grade_math, Grade_English, Grade_Chemitry, Grade_Bio, Grade_Physic)
print(f"Average Grade: {Average_grade}")

# 3- Determine the letter grade based on average grade
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
