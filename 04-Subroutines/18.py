def sum(x):
    x=str(x)
    total=0
    for i in x:
        i=int(i)
        total=total+i
        i=i+1
    return total
print(sum(7182))
