import mymath
while True:
    a=mymath.read_number()
    b=mymath.generate_number()
    if a==b:
        print("computer's number is ",b)
        print("you won")
        break
    else:
        print("computer's number is ",b)
        print("try again!")