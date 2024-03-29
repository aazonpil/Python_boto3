# reversed_name_list = []
# n=len(first_name)
# first_name="Arnaud"
# for letter in first_name:
#     n=n-1
#     reversed_name_list.append(first_name[n])
#     print(reversed_name_list)
    


# # Given first name
# first_name = "arnaud"

# # Initialize an empty list to store the reversed name
# reversed_name_list = []

# # Calculate the length of the string to determine the start point for indexing
# length = len(first_name)

# # Loop through the string's length and use negative indexing without slicing
# for i in range(length):
#     # Calculate the index from the end of the string moving backwards
#     index = length - 1 - i
#     # Append the character at the calculated index to the reversed_name_list
#     reversed_name_list.append(first_name[index])

# # Print the reversed name as a list
# print(reversed_name_list)

#forward
word = "LEMOGE"

length = len(word)  # This is 6 for "LEMOGE"
list=[]

for i in range(length):
    forward_index = i  # Directly using i as the forward index
    list.append(word[forward_index])
    

#reverse
word = "LEMOGE"
length = len(word)  # This is 6 for "LEMOGE"
list=[]

for i in range(length):
    forward_index=i
    reverse_index =length-1-forward_index  # Directly using i as the forward index
    list.append(word[reverse_index])
    join_reversed="".join(list)

print(f"The reverse of word {word} is in the list: {join_reversed}")