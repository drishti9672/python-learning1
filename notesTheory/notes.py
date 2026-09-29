#multiline statements

#implicit continuation
num1=51
num2=85
num3=94
num4=53.5
num5=81.22
sum=(num1+num2+
     num3+num4) #using barckets we can write statement in mutlti line
print(sum)

#explicit continuation
add=num1+num2+\
num3+num4
print(add)


# (to check whether a specific vallue or variable belongs to a given datatype 
# use isinstance(object,type))

print(isinstance(2,int))
print(isinstance(3.5,int))
print(isinstance(1+3j,complex))



