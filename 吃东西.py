import random as r

class fish:
    def __init__(self):
        self.x=r.randint(0,10)
        self.y=r.randint(0,10)


    def move (self ):
        self.x-=1
        print('我现在的位置：',self.x,self.y)

class goldfish(fish):
    pass

class shark(fish):
    def __init__(self):
        super().__init__()
        self.hungry= True

    def eat (self):
        if self.hungry:
            print("吃吃吃")
            self.hungry=False

        else:
            print("吃不下了")
