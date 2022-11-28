def f(array2D):
    total=0
    k=[]
    p=0
    for i in range(len(array2D[0])):
        total=0
        for j in range(len(array2D)):
            total=total+array2D[j][i]
        k.append(total)
    return k
print(f([[3,6,2,7],[9,5,4,0],[2,8,0,9]]))
print(f([[4,5,6,],[7,2,3]]))
print(f([[2,3],[7,8],[9,0],[5,6],[2,3]]))