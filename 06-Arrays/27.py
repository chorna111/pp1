array=[5,1,9,6,1]
max=array[0]
min=array[0]
largest=0
smallest=0
for i in array:
    if i>max:
        max=i
    elif i<min:
        min=i
print(f'array:{array}\nresult:{max-min}')
