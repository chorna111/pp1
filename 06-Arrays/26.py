arr=[5,1,9,6,1]
arr1=[[5,1,9,6,1]]
for i in range(len(arr)):
        for j in range(0,len(arr)-1):
            if arr[j]>arr[j+1]:
                
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
print(f'array:{arr1}\nresult:{arr[-2]}')
             
