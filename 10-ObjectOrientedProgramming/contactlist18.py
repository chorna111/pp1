class CONTACTLIST:
    def __init__(self):
        self.array=[]
    
    def add_new(self,contact):

        self.array.append(contact)
        
    def display(self):
        
        for i in self.array:
            print(i) 
       

        
