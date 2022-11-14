array=[[3,9,2],[2,4,5],[7,1,6],[0,4,8]]
sum=0
for row in array:
    for el in row:
        if el%2==0:
            sum+=el
print(sum)
