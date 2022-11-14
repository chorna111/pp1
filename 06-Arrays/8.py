array=[-15,8,-31,47,-2,19]

max=array[0]
min=array[0]
for i in array:
    if i>max:
        max=i

    elif i<min:
        min=i
print(f"max:{max}")
print(f'min:{min}')
