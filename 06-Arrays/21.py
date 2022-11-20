def compare(array1,array2):
    
    if len(array1)==len(array2):
        for item in range(0,len(array1)):
            if array1[item]==array2[item]:
                return True
    else:
        return False
array1=['water','book','sky']
array2=['water','book','sky']
if compare([array1],[array2])==True:
    print(f'array1:{array1}\narray2:{array2}\ncomparison:arrays are the same')
else:
    print(f'array1:{array1}\narray2:{array2}\ncomparison:arrays are not the same')


   
        
            


          