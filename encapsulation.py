#encapsulation 
#encapsulation is used to product
'''class company():
    def __init__(self):
        self.__companyname='google'
    def companyname(self):
        print(self.__companyname)
c1=company()
c1.companyname() '''#only class accessed by within the class 

class company():
    def __init__(self):
        self.__name='BMW'
c1=company()
 
print(c1.__name)   