a=input('enter the name of the file:')
with open(f"{a}", 'r') as f:
    total=0
    b=f.readlines()
    for i in b:
        total+=1
print(f'file name:{a}')
print(f"number of lines:{total}")


    







   