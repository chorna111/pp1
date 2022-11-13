a=int(input("Enter the first side of a triangle"))
b=int(input("Enter the second side of a triangle"))
c=int(input("Enter the third side of a triangle"))
s=(a+b+c)/2
area=int((s*(s-a)*(s-b)*(s-c))**(1/2))
print(f"the area of a triangle is {area}")