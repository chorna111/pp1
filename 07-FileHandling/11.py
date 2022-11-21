arrays=["Don't look up","Call me by your name","To the bones","Bohemian Rhapsody","Tourist"]
f=open('films.txt','w')
for i in arrays:
    f.write(i)
    f.write('\n')
f.close()
f=open('films.txt','r')
print(f.read())

