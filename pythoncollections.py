#python collection
#list[]...
'''a=[1,2,3,4]
b=[4,5,6]
a.append('sathana')#append is used to store the item in the last of list
a.insert(0,11)#insert is used to store the item whatever u want
a[0]=11#it is used to modify the item 
a.pop(2)#it used to remove item what u want 
a.extend(b)#extend is used to merge 2 list
print(a)'''
#allow dubilicate item
#insert any data type
#we can modify the list item
#insert(),append(),extend(),pop()
#...........................................................
#tuble()
#allow dublilicate iten
#insert any data type
#we cannot modify the item and add or remove
#but we are casting a tuble
'''a=(1,2,3,4)
b=list(a)
b.insert(0,12)
print(a)
print(b)'''
#............................................................
#set{}
#it dosnot allow dubilicate item
#stored any data type
#we cannot modify the item but we can add and remove the item
#set are unorder
#add(),remove(),update(),POP()

'''A={1,2,3,4}
A.add(6)
A.remove(3)
print(A)'''
#.............................................................
#dictionary{}
#do not allow dublicate item
#stroed any data type
#keyvalue pair{'name':'sathana'}
a={
    'name':'sathana',
    'age':18,
    'department':'computer',
}
a['age']=19#we can modify the item
a['clg']='padmavani' #we can store new key value pair 
a.pop('clg')#we can delete the item what we want
a.clear()#it is used to clear all the item 
print(a)
