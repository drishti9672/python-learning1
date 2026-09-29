#to check whether the list is palindrome or not
a=[1,"drishti",3,"drishti",1]
b=a.copy()  #produces a shallow copy of a list
b.reverse()

if(a==b):
    print("plindrome")
else:
    print("not a palindrome")



