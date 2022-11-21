file=open('countries.txt')
i=1
for line in file:
    
    print(i,line,end='')
    i=i+1
file.close()