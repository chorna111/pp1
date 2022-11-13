amount=int(input("Enter the amount in PLN:"))
a=int(amount/5)
b=int(amount%5)
if amount%5==0:
    print(f"The amount of PLN {amount} in coins:")
    print("5 zł - ",a)
elif amount%5==2:
    print(f"The amount of PLN {amount} in coins:")
    print("5 zł -", a)
    print("2 zł -", 1)
elif amount%5==3:
    print(print(f"The amount of PLN {amount} in coins:"))
    print("5 zł - ",a)
    print("2 zł - ",1)
    print("1 zł - ",1)