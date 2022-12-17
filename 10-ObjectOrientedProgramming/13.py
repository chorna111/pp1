class TV:
    def __init__(self):
        self.is_on=False
        self.channel_no=1
        self.array=[]
        self.volume=0

    

    def turn_on(self):
        self.is_on=True
    
    def turn_off(self):
        self.is_on=False

    def show_status(self):
        if self.is_on==True:
            try:
                print(f'TV IS ON and the channel is {self.channel_no} ({self.array[self.channel_no-1]}), volume level:{self.volume}')
            except:
                print(f'TV IS ON and the channel is {self.channel_no},volume level:{self.volume}')
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
    def increase_volume(self):
        if self.volume<=10:
            self.volume+=1
        else:
            self.volume=self.volume
    def decrease_volume(self):
        if self.volume<=10:
            self.volume-=1
        else:
            self.volume=self.volume

tv=TV()
tv.show_status()
tv.turn_on()
tv.increase_volume()
tv.increase_volume()
tv.increase_volume()
tv.decrease_volume()
tv.increase_volume()
tv.show_status()