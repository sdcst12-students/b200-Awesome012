class rectangle:
    length = 0
    width = 0

    def perimeter(self):
        p = self.length + self.width + self.length + self.width
        return p

    def area(self):
        pass

    def __init__(self,a,b):
        self.length = a
        self.width = b



r1 = rectangle(3,4)
r2 = rectangle(5,6)

print(r1.length)
print(r1.perimeter() )