def Check_Even_Odd_number(user_number):
    for number in range(0,100):

        if user_number % 2 == 0:
            result= f"{user_number} is Even"
            return result
        else:
            result = f"{user_number} is Odd"
            return result
    

#Main and calling the function 
user_number= int(input("Enter the number: "))  # Convert input to integer
result=Check_Even_Odd_number(user_number)

print(result)


