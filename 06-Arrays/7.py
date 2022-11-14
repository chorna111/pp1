
array=[1,2,3,4,5]
array[0]-=1
print(array)
array[-1]+=4
print(array)
array[int((len(array)-1)/2)]=array[int((len(array)-1)/2)]*2
print(array)
for item  in range(0,len(array)):
    array[item]+=3
print(array)

