def f(player1, player2):
    total1=0
    total2=0
    for i in player1:
        if i=='A' or i=='K' or i=='Q' or i=='T' or i=='J':
            i=10
        else:
            i=int(i)
        total1=total1+i
    for j in player2:
        if j=='A' or j=='K' or j=='Q' or j=='T' or j=='J':
            j=10
        else:
            j=int(j)
        total2=total2+j
    if total1>total2:
        return True
    else:
        return False
print(f('AJ972','AQT72'))
print(f('9532','K8'))
print(f('987','AT4'))



