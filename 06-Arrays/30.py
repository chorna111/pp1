array=[4,2,8,4,7,9,5]
max=array[0]
min=array[0]
largest=0
smallest=0
for i in array:
    if i>max:
        max=i
    elif i<min:
        min=i
k=[]
k.append(min)
k.append(max)
print(f'array:{array}\nresult:{k}')