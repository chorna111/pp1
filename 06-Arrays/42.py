arr=[7,3,7,9,0],[2,9,0,1,5], [3,8,6,4,7]
for i in range(3):
    
    for j in range(5):
        if j==0 or j==len(arr[i]):
            
            b=arr[i][len(arr[i])-1]
            a=arr[i][j]
            arr[i][j]=arr[i][len(arr[i])-1]
            arr[i][len(arr[i])-1]=a
print(arr)
