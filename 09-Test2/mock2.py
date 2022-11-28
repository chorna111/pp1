def f(human_age):
    human_age=int(human_age)
    if human_age==1 or human_age==2:
        dogyears=human_age*10
    else:
        dogyears=20+((human_age-2)*4)
    return dogyears
print(f(15))
print(f(2))
