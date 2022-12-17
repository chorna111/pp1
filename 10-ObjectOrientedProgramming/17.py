class STATISTICS:
    def __init__(self):
        self.array=[]
        
    def add(self):
        a=input('Enter a number')
        self.array.append(a)
    def display(self):
        s=', '
        s=s.join(self.array)
        print(s)
    def determinegreatest(self):
        self.greatest=self.array[0]
        for i in self.array:
            
            if int(i)>int(self.greatest):
                self.greatest=i
                continue
                
    def determinesmallest(self):
        self.smallest=self.array[0]
        for j in self.array:
            
            if int(j)<int(self.smallest):
                self.smallest=j
                continue
    def arithmeticmean(self):
        total=0
        for i in self.array:
            total=total+int(i)
        self.amean=total/len(self.array)
    def median(self):
        if len(self.array)%2==0:
            self.median=(int(self.array[len(self.array)//2])+int(self.array[len(self.array)//2-1]))/2
        else:
            self.median=self.array[len(self.array)//2]
    
    def display(self):
        print(f'Greatest number:{self.greatest}\nSmallest number:{self.smallest}\nArithmetic mean:{self.amean}\nMedian:{self.median}')


stat=STATISTICS()
stat.add()
stat.add()
stat.add()
stat.add()
stat.add()
stat.determinegreatest()
stat.determinesmallest()
stat.arithmeticmean()
stat.median()
stat.display()

