array=[[True,False],[True,True],[False,False]]
for row in range(0,3):
    for column in range(0,2):
        if array[row][column]==True:
            array[row][column]=False
        else:
            array[row][column]=True
print(array)
