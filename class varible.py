#variable...................
class phone():
    price=50000
    def __init__(self,brand,charger):
        self.brand=brand
        self.charger=charger
    def display(self):
        print('brand:',self.brand)
        print('charger:',self.charger)
        print('price:',self.price)  
    price=10000      
vivo=phone('vivo','c-type')
vivo.display()
oppo=phone('oppo','b=type')
oppo.display()
#class variable is used to allocate the common variable like(price=50000)
#and we can update the variable again like(price=10000)
    





        
