def subset(array1,array2):
    for i in array1:
        if i not in array2:
            return False
    return True
a=[2,3,4]
b=[7,6,4,2,3,]
print(subset(a,b))
 



