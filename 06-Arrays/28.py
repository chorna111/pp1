def median(array):
    
    if len(array)%2==0:
        median=((array[len(array)//2])+(array[(len(array)//2)-1]))/2

        
    else:
        median=array[len(array)//2]
    return median
print(median([1,0,9,4,6]))
print(median([6,8,3,1,0,5,7]))
print(median([1,0,3,9,4,6]))
