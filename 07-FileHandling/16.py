f=open("/Users/onostasia/Downloads/sample2.txt", "r")
a=f.read()
f.close()
b=open('copy.txt','w')
c=b.write(f'{a}')
b.close()

