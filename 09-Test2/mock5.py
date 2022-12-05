def f(first_letter,last_letter):
    import re
    a=first_letter
    b=last_letter
    d=open('/Users/onostasia/Downloads/test.txt','r')
    text=d.read()
    d.close()
    letters=re.findall(r"\b%s\w+%s\b"%(first_letter,last_letter),text)
    return len(letters)
print(f('w','d'))


