class TV:
    def __init__(self):
        self.is_on=False
        self.channel_no=1
        self.array=[]

    

    def turn_on(self):
        self.is_on=True
    def turn_off(self):
        self.is_on=False
    def show_status(self):
        if self.is_on==True:
            print(f'TV IS ON and the channel is {self.channel_no}')
        elif self.is_on==False:
            print('TV IS OFF')
    def set_channel(self,new_channel_no):
        self.channel_no=new_channel_no
    def set_channels(self,channels_list):
        
        for i in channels_list:
            self.array.append(i)
    def show_channels(self):
        s=', '
        
        s=s.join(self.array)
        print(f'available channels:{s}')
tv=TV()
tv.show_status()
tv.turn_on()
tv.show_status()
tv.set_channels(['TVP1',"TVP2",'Polsat','TVN','Filmbox','Discovery'])
tv.show_channels()
tv.show_status()
tv.turn_off()
