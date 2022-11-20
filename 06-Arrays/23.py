def bubblesort(arr):
   
    for i in range(len(arr)):
        for j in range(0,len(arr)-1):
            if arr[j]>arr[j+1]:
                
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
    return arr
print(bubblesort([3,2,7,5,1]))
print(bubblesort([78,56,79,3,5,65,34]))
print(bubblesort([9,8,7,6,5,4,3]))


