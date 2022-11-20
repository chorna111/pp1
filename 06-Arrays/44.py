def transpose(m):
    
    result = [[m[j][i] for j in range(len(m))] for i in range(len(m[0]))]
    
    return result
for i in transpose([[1,2,3],[4,5,6],[7,8,9]]):
    print(i)
    print()
for i in transpose([[1,2,3,4,5],[6,7,8,9,0]]):
    print(i)
    print()



