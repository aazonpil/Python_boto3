
for number in range(1, 10):
    if number == 5:
        break  # Exit the loop when number is 5
    print(number)
    
for n in range(0, 10):
    if n % 2 != 0:
        continue  # Use continue to skip odd numbers, not break
    print(n)

