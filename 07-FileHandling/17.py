f=open("/Users/onostasia/Downloads/sample2.txt", "r")
a=open('copylines.txt','w')
for line in f:
    a.write(f'{line}')
f.close()
a.close()
