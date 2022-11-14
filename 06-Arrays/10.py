array=[1,2,3,4,5,6,7,8,9]
even=0
odd=0
i=array[0]
while i<len(array)+1:
    if i%2==0:
        even+=1
    else:
        odd+=1
    i=i+1
print(f'Number of even:{even}.Number of odd:{odd}')