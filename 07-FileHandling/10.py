f=open('data.txt','w')
f.write('Name:Anastasiia\nSurname:Chorna\nUniversity:UEK\nField of study:Applied Informatics')
f.close()
f=open('data.txt','r')
print(f.read())
f.close()
