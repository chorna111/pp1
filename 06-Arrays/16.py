array=[15,8,31,47,2,19]
a=int(len(array))
b=[]
for item in range(1,a+1):
    b.append(array[-item])
print(f'existed array:{array}\nreverse array:{b}')
