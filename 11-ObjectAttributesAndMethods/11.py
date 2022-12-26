import math
class Math:
    @staticmethod
    def circle(radius):
        return (math.pi*(radius**2))
    def rectangle(side1,side2):
        return side1*side2
    def triangle(base,height):
        return (0.5*base*height)
area1=Math.circle(3)
area2=Math.rectangle(4,7)
area3=Math.triangle(6,2)
print(area1)
print(area2)
print(area3)

