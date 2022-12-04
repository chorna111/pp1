a=input('rpn expression')
stack=[]
for item in a:
    if item not in '/*+-=':
        stack.append(int(item))
    elif item=='=':
       print(stack.pop())   
    else:
        right=stack.pop()
        left=stack.pop()
        if item=='+':
            stack.append(left+right)
        if item=='-':
            stack.append(left-right)
        if item=='*':
            stack.append(left*right)
        if item=='/':
            stack.append(int(left/right))
    
    




