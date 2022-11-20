array=[[19, 40], [5,3],[-7,11],[29,90]]
largest=array[0][0]
smallest=array[0][0]
for i in range(0,len(array)):
    for j in range(0,len(array[i])):
        if array[i][j]>largest:
            largest=array[i][j]
            index1=i
            index2=j
print(f'The largest value in the array is {largest} and it is in the {index1+1} row and {index2+1} column')
for p in range(0,len(array)):
    for k in range(0,len(array[i])):
        if array[p][k]<smallest:
            smallest=array[p][k]
            index3=p
            index4=k
print(f'The smallest value in the array is {smallest} and it is in the {index3+1} row and {index4+1} column')

       
    

