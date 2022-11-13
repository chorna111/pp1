a=int(input("Enter the dog's age in human years"))
if a<=2:
    age=int(a*10.5)
    print("The dog's age in dog's years is",age,"years")
else:
    age=int((a-2)*4+(2*10.5))
    print("The dog's age in dog's years is",age,"years")