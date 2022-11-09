class Circle:
    PI=3.14

    def __int__(self):
        self.radius=0
        self.area=0
        self.circumference=0

    def acceptRadius(self,radius):
        self.radius=radius

    def calculateArea(self):
        self.area=self.PI*self.radius*self.radius

    def calculateCircumference(self):
        self.circumference=2*self.PI*self.radius

    def display(self):
        print("Radius of object is ",self.radius)
        print("Area of object is ",self.area)
        print("Circumference of object is ",self.circumference)

def main():
    print("Enter Radius")
    radius=int(input())

    dobj1=Circle()
    dobj1.acceptRadius(radius)
    dobj1.calculateArea()
    dobj1.calculateCircumference()
    dobj1.display()

    print("Enter Radius")
    radius = int(input())

    dobj2 = Circle()
    dobj2.acceptRadius(radius)
    dobj2.calculateArea()
    dobj2.calculateCircumference()
    dobj2.display()

if __name__=="__main__":
    main()