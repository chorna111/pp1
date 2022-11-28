def f(dictionary,x,y):
    total=0
    for key in dictionary.keys():
        for i in dictionary[key]:
            if i>=x and i<=y:
                total+=i
            else:
                total+=0
    return total
print(f({'arr1':[4,5,6],'arr2':[7,5]},5,6))
print(f({'arr1':[2,6,5],'arr2':[7,1],'arr3':[2,9,8,1]},5,10))

