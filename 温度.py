
class cell:
    def __init__(self , value=26):
        self.value =float(value)

    def __get__(self, instance, owner):
        return self.value

    def __set__(self,instance,value):
        self.value=float(value)


class Fah:
    def __get__(self,instance,owner):
        return instance.ce*1.8+32

    def __set__(self,instance,owner):
        instance.ce=(float(value)-32)/1.8


class Temperature:
    ce=cell()
    fah=Fah()
    
