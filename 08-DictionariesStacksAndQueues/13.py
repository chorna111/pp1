import json
student={
    'name':'Jan',
    'surname':'Nowak',
    'age':18,
    'field of studies':'applied informatics',
    'grades':{'pp':'4','ask':'5','english':'5'}
}
with open('student.json','w',encoding='utf-8') as file:
    json.dump(student,file,indent=len(student))

