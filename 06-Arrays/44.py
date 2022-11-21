def transpose(m):
    try:
        result = [[m[j][i] for j in range(len(m))] for i in range(len(m[0]))]
    except:
        result=[]
        for i in m:
            result.append(i)

    
    
    return result
for i in transpose([[1,2,3],[4,5,6],[7,8,9]]):
    print(i)
    print()
for i in transpose([[1,2,3,4,5],[6,7,8,9,0]]):
    print(i)
    print()
for i in transpose([1,2,3,4,5]):
    print([i])
    print()




