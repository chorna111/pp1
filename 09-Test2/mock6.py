def f(age,course,average):
    import json
    d=open('/Users/onostasia/Downloads/test.json','r')
    file=json.load(d)
    d.close()
    total=0
    number=0
     
    for i in file:
        if i['age'] >=age:
            for j in i['studies']['courses']:
                if j['name']==course:
                    p=0
                    total=0
                    avg=0
                    for b in j['grades']:
                        total=total+b
                        p=p+1
                    avg=total/p
                    if avg>=average:
                        number=number+1
                else:
                    continue
        else:
            continue


        
       


    return number
print(f(21,'statistics',4))

       




