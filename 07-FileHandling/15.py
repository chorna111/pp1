f=open("/Users/onostasia/Downloads/sample2.txt", "r")
a=int((len(f.readlines()))//5+1)
f.close()
f=open("/Users/onostasia/Downloads/sample2.txt", "r")
for i in range(a):
    print(f.readline())
    print(f.readline())
    print(f.readline())
    print(f.readline())
    print(f.readline())
    a=input('enter')
f.close()
