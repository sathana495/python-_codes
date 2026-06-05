#polymorphism
#if u give the same fuction polymorphism overrides the value and give the another class output
#quiz 1
class animals():
    def greek(self):
        print('animal make sound')
class dog(animals):
    def voice(self):
        print('dog barks')
class bird(dog):
    def sound(self):
        print('bird sings')        
b1=bird()
b1.greek()
#quiz 2
'''class shape():
    def area(self):
        return 0
class rectangle(shape):
    def area(self,):
        d=int(input())
        e=int(input()) 
        print(d*e)

r1=rectangle()
r1.area()'''#this class overrides a shape class

#quiz 3:
'''class person():
    def __init__(self,name):
       self.name=name
       
class student(person):
    def __init__(self,name,grade):
        self.grade=grade
        super().__init__(name)
    def display(self):
        print('name:',self.name) 
        print('grade:',self.grade)   
       
s1=student('sana','A')
s1.display()'''
#quiz 4:
'''class vehical():
    def start(self):
        print('vehical start')
class car(vehical):
    def start(self):
        print('car started')        
c1=car()
c1.start()'''
#quiz 5:
'''class empolyee():
    def __init__(self,name,salary):
        self.name=name
        self.salary=salary
class manager(empolyee):
    def __init__(self,name,salary,department):
        self.department=department
        super().__init__(name,salary)
        
        
    def display(self):
        print('name:',self.name)
        print('salary:',self.salary)
        print('department:',self.department)

m1=manager('sathana',45000,'computer')
m1.display()'''




       