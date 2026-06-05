#example goa
'''class goa:
    name=''
    drink=''
    def party():
        print('kets party...')
    def bitch():
        print('enjoy the bitch...')

abi=goa()
shivani=goa()
sathana=goa()

abi.name='abi'
shivani.name='sivani'
sathana='sathana'


abi.drink='yes'
shivani.drink='no'


abi.party()'''
#laptop
'''class laptop():
    price=""
    procesor=""
    ram=""
hp=laptop()
dell=laptop()

hp.price=50000
hp.procesor='i5'
hp.ram='16gp

dell.price=45000
dell.procesor='i7'
dell.ram='8gp

print(dell.ram)'''
# constructor:
#constructor is a unique function that gets called autometically when an object is created of a class(inite)
'''class laptop:
    def __inite__(self):
        self.ram="16gp"
        self.price=''
    def disply(self):
        print("price:",self.price)
        print("rem:",self.ram)    

hp=laptop()
dell=laptop()

hp.ram="8gp"
hp.price=50000

dell.ram='16gp'
dell.price=45000

print(dell.ram)
print(dell.price)

print(hp.price)
print(hp.ram)

hp.disply()
dell.disply()'''

#quiz 1:
'''class student:
    def __init__(self):
        self.name=""
        self.rigesternumber=""
    def display(self):
        print("name:",self.name)
        print("rigesternumber:",self.rigesternumber)

abi=student()
sivani=student()

abi.name='abinaya'
abi.rigesternumber=20

sivani.name='sivadharshini'
sivani.rigesternumber=32

print(abi.name)
print(abi.rigesternumber)

print(sivani.name)
print(sivani.rigesternumber)

abi.display()
sivani.display()'''
#quiz 2:
'''class furit:
    def __init__(self,col):
        self.color=''

apple=furit('red')
print(apple.color)'''
#quiz 3:
class teacher:
    def __init__(self,name,regno):
        self.name=name
        self.regno=regno
    def display(self):
        print('name:',self.name)
        print('regno:',self.regno)

t1=teacher('priya',34)
t2=teacher('aruna',43)

t1.display()
t2.display()
#quiz 4:
'''class calculator:
    def __init___(self,c,d):
        self.num1=c
        self.num2=d
    def add(self,self.num1,self.num2):
        print('add:',c+d)

opj1=calculator(10,4)
opj1.add()'''
