names=['Genoefa','Onufry','Celestyna','Alijzy','Pankracy']
max=names[0]
for item in range(0,int(len(names))):
    if int(len(names[item]))>int(len(max)):
        max=names[item]
print(f"Longest name:{max}")
