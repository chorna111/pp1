a=range(1,31)
for i in a:
    if i%3==0 and not i%5==0:
        print("THREE", end=" ")
    if i%5==0 and not i%3==0:
        print("FIVE",end=" ")
    if i%3==0 and i%5==0:
        print("BINGO",end=" ")
    if not i%5==0 and not i%3==0:
        print(i,end=" ")



    





