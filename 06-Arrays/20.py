array=[12,6,4,9,10]
def star(n):
    n=int(n)
    for i in range(0,int(len(array))):
        if n==array[i]:
            return "*"*n
for item in array:
    print(f'{item}:{star(item)}')