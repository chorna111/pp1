class Phone:
    def __init__(self,mark,model,storage):
        self.mark=mark
        self.model=model
        self.storage=storage
        self.is_on=True
        self.volume=1
        self.airplanemode_ison=False
    def __str__(self):
        if self.is_on:
            if self.airplanemode_ison:
                return f'Phone mark:{self.mark}\nPhone model:{self.model}\nPhone storage:{self.storage}.\nPhone is on, it\'s volume is {self.volume} and airplane mode is on'
            else:
                return f'Phone mark:{self.mark}\nPhone model:{self.model}\nPhone storage:{self.storage}.\nPhone is on, it\'s volume is {self.volume} and airplane mode is off'
        else:
            if self.airplanemode_ison:
                return f'Phone mark:{self.mark}\nPhone model:{self.model}\nPhone storage:{self.storage}.\nPhone is off, it\'s volume is {self.volume} and airplane mode is on'
            else:
                return f'Phone mark:{self.mark}\nPhone model:{self.model}\nPhone storage:{self.storage}.\nPhone is off, it\'s volume is {self.volume} and airplane mode is off'


    def turn_on(self):
        self.is_on=True
        
        
    def turn_off(self):
        self.is_on=False
    
 
    def increase_volume(self):
        if self.is_on:
            self.volume+=1
            
        else:
            print(f'{self.model} is off, you cannot increase volume')
    def decrease_volume(self):
        if self.is_on:
            self.volume-=1
        if self.volume<0:
            self.volume=0
            

        else:
            print(f'{self.model} is off, you cannot decrease volume')
    def turn_on_airplane(self):
        if self.is_on:
            self.airplanemode_ison=True
       
  
    def turn_offairplane(self):
        if self.is_on:
            self.airplanemode_ison=False
        
phone1=Phone('Apple','Iphone 11','128gb')
phone2=Phone('Samsung','Galaxy 11','256gb')
phone3=Phone('Aplle','Iphone 14 Pro max','512gb')
phone1.turn_on_airplane()
phone1.increase_volume()
phone1.increase_volume()
phone1.increase_volume()
phone2.decrease_volume()
phone2.decrease_volume()
phone2.decrease_volume()
phone3.turn_off()

print(phone1)
print(phone2)
print(phone3)
   


