"""write a python program that will display the account_id from 
the arn below: arn:iam::123456789012:user/Development/product_1234/* .
Display on the screen : the aws  account id is : "accound_id".  and give me all the details"""
# 2-Automatic method with find()
arn = "arn:iam::123456789012:user/Development/product_1234/*"
lenth= len(arn)
print (f"The arn lenth is :{lenth}")

# Find the start index by locating the second colon after "iam::" and add 1
start_index = arn.find("iam::") + 5

# Find the end index by locating the colon after the account ID
end_index = arn.find(":user")

# Extract the account ID using the identified indices
account_id = arn[start_index:end_index]

print(f"the aws_account_id is : {account_id}")

