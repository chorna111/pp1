import random
class Arrays():
    def method_name(numberel,value):
        arr=[]
        for i in range(numberel):
            arr.append(value)
        return arr
    @staticmethod
    def array1(m,f,t):
        
        a=[]
        for i in range(m):
            a.append(random.randint(f,t))
            
        return a
    def array2(a,f,t):
        total=0
        for i in range(len(a)):
            if a[i] in range(f,t):
                total+=1
        print(total)
myarray=Arrays.method_name(10,4)
myarray2=Arrays.array1(20,-7,8)
print(myarray)
print(myarray2)
Arrays.array2(myarray,-1,2)
Arrays.array2(myarray2,-1,2)




