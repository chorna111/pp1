import re
f=open("/Users/onostasia/Downloads/sample2.txt", "r")
a=f.read()
x=re.findall('\w{6,}',a)
f.close()
for i in x:
    print(i)
