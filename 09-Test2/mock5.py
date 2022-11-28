def f(first_letter,last_letter):
    import re
    a=first_letter
    b=last_letter
    d=open('/Users/onostasia/Downloads/test.txt','r')
    text=d.read()
    d.close()
    letters=re.findall(fr"\b{first_letter}\w+{last_letter}\b",text)
    total=0
    for i in letters:
        total+=1
   
   
   
        

    
    
    return total
print(f('w','d'))

