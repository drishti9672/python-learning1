#tuples= it is also a datatype like lists but unlike lists it is immutablle
a=(1,4,67,2.3,"drishti")
print(a)
print(a[1])
print(a[1:5])

b=(1,) # if u are making a single tuple u must use(,)  in last 
print(type(b))

c=(1)
print(type(c))#python will think it as integer


print(a.append(5))
print(a)