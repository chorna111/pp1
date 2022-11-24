f=open("/Users/onostasia/Downloads/MeatAndFish.txt", "r")

a=f.read()
f.close()
d=open("/Users/onostasia/Downloads/GrainsAndBread.txt", "r")
b=d.read()

d.close()
c=open('shoppinglist.txt','w')
c.write(f'{a}\n{b}')
c.close()
