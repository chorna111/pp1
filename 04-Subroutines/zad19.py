def ToF(x,y,z):
    x=int(x)
    y=int(y)
    z=int(z)
    if z<=y and z>=x:
        return True
    else:
        return False
print(ToF(10,30,-10))

