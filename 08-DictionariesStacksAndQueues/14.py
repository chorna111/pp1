import re
icao={
    'A':'Alfa',
    'B':'Bravo',
    'C':'Charlie',
    'D':'Delta',
    'E':'Echo',
    'F':'Foxtrot',
    'G':'Golf',
    'H':'Hotel',
    'I':'India',
    'J':'Juliett',
    'K':'Kilo',
    'L':'Lima',
    'M':'Mike',
    'N':'November',
    'O':'Oscar',
    'P':'Papa',
    'Q':'Quebec',
    'R':'Romeo',
    'S':'Sierra',
    'T':'Tango',
    'U':'Uniform',
    'V':'Victor',
    'W':'Whiskey',
    'X':'Xray',
    'Y':'Yankee',
    'Z':'Zulu'}
a=input('enter text ')
a=str(a)
k=''
for i in a:

    for x,y in icao.items():
        if x==i or x.lower()==i:
            k=k+' '+y
#lub
s=''
for key,value in icao.items():
    v=value.lower()
    s=s+' '+value+' '+v
spelled=''
for j in a:
    
    x=re.findall(fr'\b{j}\w+',s)
    spelled=spelled+' '+x[0]
print(f'Spelled text:{spelled.title()}')