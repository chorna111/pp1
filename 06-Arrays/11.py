def mounth(n):
    n=int(n)
    array=['january','february','march','april','may','june','july','august','september','october','november','december']
    for i in range(0,len(array)):
        while n==i+1:
            return array[i]

print(mounth(11))



