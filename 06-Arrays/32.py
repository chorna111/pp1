
def commas(array):
    a=""
    for i in array:
        i=str(i)
        a=a+i+","
    return a[0:-1]
        
      
print(f'array:{[2,3,4,5]}\nstring:{commas([2,3,4,5])}')

