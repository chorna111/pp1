import csv
with open("/Users/onostasia/Downloads/student.csv") as csvfile:
    spam=csv.reader(csvfile)
    rows=[]
    for row in spam:
        rows.append(row)
    k=[]    
    for i in range(1,len(rows)):
        if int(rows[i][2])<30:
            rows[i]=rows[i][0],rows[i][1],rows[i][4]
            k.append(rows[i])
print(k)
largest1=0
largest2=0
for d in range(0,3):
    if len(k[d][0])>largest1:
            largest1=len(k[d][0])
for d in range(0,3):
    if len(k[d][1])>largest2:
        largest2=len(k[d][1])



for j in k:
     print(j[0],"  "+" "*(largest1-len(j[0])),j[1],"  "+" "*(largest2-len(j[1])),j[2])






    


       