import re
f=open("/Users/onostasia/Downloads/grades.txt", "r")
x=f.read()
a=re.findall("\d.\d",x)
f.close()
total=0
for i in a:
    
    total+=float(i)
    avg=round((total)/(len(a)),2)
print(x)
print(f"student's average grade is{avg}")