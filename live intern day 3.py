#control flow statements
#conditional flow
'''age = int(input('enter the your age:'))
if age>18:
    print('you eligible for vote')
elif age==18: 
    print('your eligible for vote')
else:
    print('your not eligible') '''


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

'''for i in range(5):
    for j in range(5):
        print('*',end="")
    print()    



for i in range(5):
    for j in range(i):
        print('*',end="")
    print() '''
# quiz 1
'''n = int(input("Enter number of rows: "))

for i in range(1, n+1):
    for j in range(1, i+1):
        print(j, end=" ")
    print()'''
#quiz 2
'''n = int(input("Enter n: "))

for i in range(1, n+1):
    print(f"Table of {i}")
    for j in range(1, 11):
        print(i, "x", j, "=", i*j)
    print()'''


'''for i in range(1,11):
    print(i,'x','2','=',i*2)'''

#quiz 3
'''num=int(input('enter a number:'))
if(num%2==0):
    print('E')
else:
    print('O')'''

#quiz 4
'''n = int(input("Enter number: "))

for i in range(2, n+1):
    is_prime = True
    for j in range(2, i):
        if i % j == 0:
            is_prime = False
            break
    if is_prime:
        print(i, end=" ")'''

#quiz 5
'''marks = int(input('enter student mark:'))
if marks >= 75:
    print('Distinction')
elif marks>= 50 and marks<=74:
    print('pass')
elif marks<50:
    print('fail')
else:
    print('enter your correct mark') '''  

#quiz 6
n = int(input("Enter rows: "))
m = int(input("Enter columns: "))

print("Enter Matrix A:")
A = []
for i in range(n):
    row = list(map(int, input().split()))
    A.append(row)

print("Enter Matrix B:")
B = []
for i in range(n):
    row = list(map(int, input().split()))
    B.append(row)

# Addition
result = []
for i in range(n):
    row = []
    for j in range(m):
        row.append(A[i][j] + B[i][j])
    result.append(row)

print("Result Matrix:")
for row in result:
    print(row)










    


