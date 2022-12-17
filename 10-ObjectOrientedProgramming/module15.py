import random
class THERMOMETER:
    def turn_on(self):
        self.turned_on=True
        self.turned_off=False
    def turn_off(self):
        self.turned_on=False
        self.turned_off=True
    def measure(self):
        if self.turned_on:
            self.degree=float(random.randint(37,42))

    def display(self):
        if self.turned_on:
            if self.degree>=37 and self.degree<41:
                print(f'Temperature: {self.degree} (fever)')
            elif self.degree>=41:
                print(f'Temperature: {self.degree} (CRITICAL TEMPERATURE!!!)')
        else:
            print('Thermometer is turned off')



