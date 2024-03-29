n = 0
while n <= 15:
    n = n+1
    if n %3 == 0 and n %5 == 0:
        print("FooBar")
    elif n %3 ==0:
        print("Foo")
    elif n %5 == 0:
        print("Bar")
    else:
        print(n) # if not a multiple of 3 or 5 within the range