def occurs(number,array):
  
    
    for i in array:
        if i==number:
            return True
        
    return False
number=int(input('Number:'))
array=[15,38,7,23,14]
occurs(number,array)
if occurs(number,array)==True:
    print(f"Number:{number}\narray:{array}\nresult:number {number} appears in the array")
else:
    print(f"Number:{number}\narray:{array}\nresult:number {number} does not appear in the array")




