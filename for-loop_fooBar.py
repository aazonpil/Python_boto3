# using for-loop
for number in range (1, 16):
    if number %3 == 0 and number %5 == 0:
        print("FooBar")
    elif number %3 ==0:
        print("Foo")
    elif number %5 == 0:
        print("Bar")
    else:
        print(number) # if not a multiple of 3 or 5 within the range