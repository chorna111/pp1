arr=[7,3,7,9,0],[2,9,0,1,5],[3,8,6,4,7]
for i in range(5):
        a = arr[0][i]
        arr[0][i] = arr[len(arr)-1][i]
        arr[len(arr)-1][i] = a
print(arr)