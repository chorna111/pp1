def conver(a):
    m=[]
    for i in a:
        for j in i:
            m.append(j)
    return m
print(conver([[2,3,4],[5,6,7]]))
print(conver([[5,0,3,7,5],[9,0,9,1,2]]))
print(conver([[2,1],[3,5],[7,4],[2,6]]))