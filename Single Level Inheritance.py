class F15:
    def light(self):
        print("Ok Switching on the lights")
    def fan(self,speed):
        print("Fan is on and the speed is ",speed)
        self.s = speed
    def cpu(self):
        print("Powering on the system")
        print(self.s)

chandu = F15()
class shopping(F15):
    def __init__(self,place):
        self.place=place
        print("Welcome to shopping at ",place)
    def dresstype (self,dt):
        self.s1 =dt
    def price (self,pr):
        self.s2 = pr
    def size (self,sz):
        self.s3 = sz
    def display (self):
        print(self.s1,self.s2,self.s3)
details = shopping("Raymond")
details.dresstype("Cotton")
details.price(5000)
details.size("L")
details.display()
details.light()
details.fan(5)
details.cpu()
