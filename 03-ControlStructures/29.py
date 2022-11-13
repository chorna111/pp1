total=0
i=0
avg=0
while True:
    a=int(input("Enter number"))
    if a==0:
        
        print("Result: Quantity=",i,"Sum=",total,"Mean=",avg)
        break
    else:
        total=total+a
        i=i+1
        avg=int(total/i)
        
        

