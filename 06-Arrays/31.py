array=[4,2,8,4,7,9,5]
e=[]
o=[]
for i in array:
    if i%2==0:
        e.append(i)
    else:
        o.append(i)
print(e+o)