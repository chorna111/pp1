import json

with open("euro.json","r") as f:
    rates=json.load(f)
    print(rates)
a='Date            Buying Rate      Selling Rate'
b=len(a)
print(a)
print('='*b)
for i in rates['rates']:
    if int(len(str(i['bid'])))==6:
        print(i['effectiveDate'], "    ",i['bid'], "          ",i['ask'])
    else:
        print(i['effectiveDate'], "    ",i['bid'], "           ",i['ask'])
       



      
