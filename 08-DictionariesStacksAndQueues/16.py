import json
with open('students.json','r') as file:
    a=json.load(file)
    c=[]
    
    for i in a:
        c.append({'name':i['name'],'surname':i['surname'],'student id':i['student id']})
       
with open('limited.json','w',encoding='utf-8') as file2:
    json.dump(c,file2,indent=3)


            
                




 


