def identity_matrix(n):
    arr=[[0 for i in range(n)]for j in range(n)]
    p=0
    for i in range(n):
        arr[p][p]=1
        p=p+1
    return arr

for i in identity_matrix(3) :
    print(i)  
    print()  
for i in identity_matrix(5) :
    print(i)  
    print() 
for i in identity_matrix(8) :
    print(i)  
    print() 

