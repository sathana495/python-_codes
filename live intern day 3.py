#control flow statements
#conditional flow
age = int(input('enter the your age:'))
if age>18:
    print('you eligible for vote')
elif age==18: 
    print('your eligible for vote')
else:
    print('your not eligible') 


'''age = int(input('enter the age:'))
weight = int(input('enter the weight:'))
if age>20:
    if weight>50:
        print('you can donate')
    else:
        print('your weight is low')    

else:
    print('your age is low')'''


#loop control flow
#for loop
'''for i in range(5):
    print(i)'''

#revers order
'''for i in range(100,0,-1):
    print(i)'''

'''for i in 'sathana':
    print(i)'''

for i in range(5):
    for j in range(5):
        print('*',end="")
    print()    



for i in range(5):
    for j in range(i):
        print('*',end="")
    print() 








    


