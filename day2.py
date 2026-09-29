#arithmetic operation
#%use for remainder
#**=use for power raising
a=2
b=4
print(a%b)
print(a**b) 

"""if u wnt to make on more then one line comment in single click then  select them
 just press ctrl+/ simultaneously"""

#relational / comparisional operators(== , != , < , > , <= , <=)
  #give output in true or false 

  #assignment operators 
#=, += , _= , *= , /= , %= , **= 
a+=10
print(a)#12

#logical operators(not , and , or)

#not
print(not False) #true
print(not(a==b))#true
print(not(a!=b))#false

#and
c=True
d=False
e=True
f= False
print(c and d)#false
print(c and e)#true
print(d and f)#false

#or
print(c or d)#true
print(d and f)#false


#datatypes= int , bool , float , str , complex


#type conversion  #python do it by itself
a1=2#int
a2=2.3#float
print(a1+a2) #2.0+2.3==4.3

#type casting(you do the conversion manually)
b1="2" 
b2=2.3
#now if i print b1+b2 it wll me wrong as b1 is string
 
b1=int("2")#can be coverted in float too
print(b1+b2)#now ans will be 4.3
c1=2
c1=str(2)
print(type(c1)) #now c1 is string

#input in python
name = input("enter your name =")
print("hello",name) #write name in terminal and press enter
#input is considered as str type eiter its word or int
print(type(name))
value=input("enter a num=")
print (type(value))#string
