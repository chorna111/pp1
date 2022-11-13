from turtle import xcor


def appearing(x,y):
    count=0
    x=str(x)
    y=str(y)
    for i in y:
        
        if i==x:
            count=count+1
    return count
print(appearing("e","You never get a second chance to make a first impression"))
