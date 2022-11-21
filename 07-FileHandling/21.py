f=open('smth.txt','w')
for i in range(1,11):
    f.write(f'{i},{i**2},{i**3}\n')
f.close()
f=open('smth.txt','r')
print(f.read())
