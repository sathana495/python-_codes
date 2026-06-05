#single inheritence
#one class access another class called single inheritence
'''class dad():
    def money(self):
        print('dads money')
class son(dad):
    def laptop(self):
        print('sons laptop')
prajith=son()
prajith.money()'''#here a class access the dads class

#multiple inheritence
#if one class access two or more class thet called multiple inheritence
'''class sister():
    def phone(self):
        print('sisters phone')
class dad():
    def money(self):
        print('dads money')
class son(sister,dad):
    pass
prajith=son()
prajith.phone()
prajith.money() ''' #here the son class access sister and dada's class

#multilevel inheritence
#each class access another class called multilevel inheritence
'''class mom():
    def sweet(self):
        print('moms sweet')
class dad(mom):
    def money(self):
        print('dads money')
class sister(dad):
    def phone(self):
        print('sisters phone')
class son(sister):
    pass
prajith=son()
prajith.phone() 
prajith.sweet()'''#here each class another class like  dad access moms sweet sister access dads class here dad class has a mom class
#and sister class access dad class now the sister class has a mom and dad class then sos class access whatever he want 

#herarical inheritence
#one class accessed by many class called herarical inheritence
'''class dad():
    def money(self):
        print('dads money')

class son1(dad):
    pass

class son2(dad):
    pass  

class son3(dad):
    pass   

s2=son2()
son2.money()'''#here teh dad class accessed by 3 son class

#hybired inheritence
#this type include many type ineritence
'''class dad():
    def money(slef):
        print('dads money')
class land():
    def importentland(self):  
        print('a land')      
class prajith(dad):
    pass
class sathana(dad):
    pass
class bharathi(dad,land):
    pass    
mom=bharathi()
mom.money()'''

#super keywords
class frds():
    def __init__(self):
        print('hello')
    def abi(self):
        print('abinaya')
class student(frds):
    def __init__(self):
        super().abi()
        print('s1')
class teacher(student):
    def __init__(self):
        super().__init__()
        print('teacher1')                
sana=student()
#the super keyword(super().__init__()) used inherite the classes