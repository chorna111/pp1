import json
d={'name':'3 comrades',
'author':'Erique Marie Remark',
'originally published':'1936',
'genre':'war novel',
'language':'german'}
with open("favourite.json",'w') as file:
    json.dump(d,file,indent=6)
