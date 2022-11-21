import random
a=random.randint(100,999)
f=open('num.txt','w')
for i in range(50):
    f.write(f'{random.randint(100,999)}\n')
f.close
f=open('num.txt','r')
print(f.read())
f.close()