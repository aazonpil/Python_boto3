
user_number= int(input("Enter the number: "))  # Convert input to integer
if 1 <=user_number and 100 >= user_number:
    if user_number % 2 == 0:
        print(f"{user_number} is Even")
    else:
        print(f"{user_number} is Odd")
else:
    print("Error")
