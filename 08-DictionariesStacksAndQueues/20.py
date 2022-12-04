stack=[]
a=18
print(f'Natural number: {a}')
while True:
    s=a%2
    a=a//2

    stack.append(s)
    if not a==0:
        continue
    else:
        break
t=len(stack)-1
print('Binary number:',end='')
for i in range(t,-1,-1):
        print(stack[i],end=' ')


