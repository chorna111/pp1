array=[2,3,2,5,8,1,9,8]
k=[]
for i in array:
    if not array.count(i)>1:
        k.append(i)
        
print(f'array:{array}\nunique elements:{k}')

            