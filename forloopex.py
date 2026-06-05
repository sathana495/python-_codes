#for loo is usually used to the number iteration is known
'''for i in 'apple':
    print(i)'''#here range is a 'apple',and the apple is range for i

#range function
'''for i in range(6):
    print(i)'''
#example
'''for i in range(1,6):
    print(i)'''
#quiz 1 two table
'''for i in range(1,11):
    print(i,'x','2','=',i*2)'''
#quiz 2: get input and fine the between number of input
'''a=int(input())
b=int(input())
for c in range(a+1,b):
    print(c)'''
#quiz 3: print even number between 1 to 10
'''for i in range(1,11):
    if(i%2==0):
      print(i)'''
#quiz 4:count the odd number between 1 to 10
'''count=0
for i in range(1,11):
    if(i%2!=0):
        count=1+count
print(count)  '''
#quiz 5:count the odd and even number between 1 to 10
'''o_count=0
e_count=0
for i in range(1,11):
    if(i%2==0):
        e_count=e_count+1
    else:
        o_count=o_count+1
print(e_count)
print(o_count)'''
#quiz 6:count the number which are divisible by 3 and 5 range 1 to 100
'''count=0
for i in range(1,101):
    if(i%3==0 and i%5==0):
        count=count+1
print(count)'''
#quiz 7:find the sum of the number 1 to 10
'''sum=0
for i in range(1,11):
    sum=sum+i
print(sum) '''
# here we are using list
'''a=[]
print('enter a number')
for i in range(5):
    b=int(input('enter a number'+str(i)))
    a.append(b)     
print(a)                                                                                                                      

sum=0
for i in a:
    sum=sum+i
print(sum)    '''
# nested for loop...
'''for i in range(1,6):
    for j in range(1,3):
        print(i,j,end="")'''
#quiz 1:
'''for i in range(1,3):
    print('week',i)
    for j in range(1,4):
        print('day',j,)'''
#quiz 2:
'''for i in range(1,5):
    print()
    for j in range(1,i+1):
        print(j,end="")'''
#practice 1
'''sum=0
for i in range(1,11):
    sum=i+sum
print(sum)'''
#practice 2
'''text="python"
for cr in text:
    print(cr) '''
#practice 3:while loop
'''i=1
while(i<=10):
    print(i)
    i=i+1'''
#practice 4:multiblication table for 3
'''for i in range(1,11):
    print(i,'x','3','=',i*3)'''
#practice 5:print even number between 1 to 20
'''for i in range(1,21):
    if(i%2==0):
        print(i)'''
#practice 6:Count down from 5 to 1
'''a=5
while(a>0):
    print(a)
    a=a-1'''
#practice 7:Problem: Given a list [1, 2, 3, 4, 5], find the sum using a loop
'''a=[1,2,3,4,5]
b=0
for i in a:
    b=b+i
print(b)'''
#Problem: Count how many vowels are in "hello world" using a loop.
'''text='hello world'
vowels='aeiou'
count=0
for i in "hello world":
    if i in vowels :
        count=count+1
print(count)'''

