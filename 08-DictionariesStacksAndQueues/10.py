array=[{
    'country':'Poland',
    'population':30000000
},
{
    'country':'Germany',
    'population':80000000
},
{
    'country':'Danmark',
    'population':3000000
},
{
    'country':'Ukraine',
    'population':39000000
},
{
    'country':'Sweden',
    'population':10000000
}]

a=0
while a<len(array):
    for key,value in array[a].items():
        print(value,end=':')
    print()
    a+=1




