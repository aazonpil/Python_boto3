#Write a program that will ask the user body in pound and then to convert it: transfort into float
user_weigh_lbs= input(" the use body_weigh in pound is: ")
User_weigh_lbs= float(user_weigh_lbs)
# To convert from lbs to kg, use 1 lbs --> 0.453592 kg .
number= 0.453592 # let put 0.453592 in a variable
User_weigh_kg= User_weigh_lbs*number
#Display the three decimal digit
print(f"the user weigh in kg is {User_weigh_kg:.3f}")