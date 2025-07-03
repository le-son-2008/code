class UpperString():
    def __init__(self):
        self.s=''
    def getString(self):
        self.s=input("String:")
    def printString(self):
        print(self.s.upper())
ob=UpperString()
ob.getString()
ob.printString()