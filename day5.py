#exampple2
a=int(input("enter a num="))
b=float(input("enter a num="))
c=int(input("enter a num="))
if(a>=b and a>=c):
    print("a is greatest of all three numbers")
elif(b>c):
    print("b is greatest of all three numbers")
else:
    print("c is greatest of all three numbers")

#list
marks=[2 , 5, 6, 7, 0, 45, 95.5 , "karan ", "arjun "," dipti ", None,45.5]#different datatyes can be saves as values in list but  in strings it cant be cdone
print(marks)
#list are mutable mns the acces and assigning both can done on indexes but in str it u can access but cant assign diff values
student=["karan",97,"rama Vihar", "Delhi"]
student[0]="drishti"
print(student)
print(student[3])
#list slicing=same as string slicing
print(student[2:3])
print(student[0:3])
print(student[-3:-1]) 

#list methods
a=[12,3,78]
b=["drishti", "d","mango"]
#list.append() #returns None (unlike string) bcz it make changes in real list mns after this method u print that list updated list will  print
print(a.append(67)) 
print(b.append("zebra"))
print(a)
print(b)
#list.sort()
print(a.sort())  
print(b.sort())
print(a)  
print(b)

#list.sort(reverse=True)
print(a.sort(reverse=True))#this both reverse will done in updated list not the originsl we have written first as we know before this we have done many othr methods on list 
print(b.sort(reverse=True))
print(a)
print(b)

#list.reversse
a.reverse()#in above we have written print to see that  these  all listmethods reverses none when we write print before the code
b.reverse()
print(a)
print(b)

#list.insert(ind,elemnt)
a.insert(1,3.9)
b.insert(2,"litchi")
print(a)
print(b)

#list.remove()
#list.pop(index)