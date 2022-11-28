import json

with open("data.json") as file:
    data = json.load(file)

for k in data:
    for key,value in k.items():
        print(key,':',value)
#lub

i=0
while i<len(data):
    for k,y in data[i].items():
        print(k,':',y)
    i+=1
