#strings can be created using single , double or triple quotes 

#special escape characters
#1=if u want to write two differnt liines in differnt lines withouyt writing in diff lines in code use=\n
print("my name is drishti sharma.\ni am 19 years old" )
#2= if u wnt to create a tab space between two lines use \t
print("I am drishti sharma.\tI am 19 years old") 

#operation on strings
#1: concatenation(used for adding two or nome strings)
str1="Drishti"
str2=" Sharma"
print(str1 +str2)
#2:lenghth of sting
a="Drishti"
print(len(a))
b="Sharma"
print(len(b))
print("hello"+"world")
print(len(str1+" "+str2)) #space in quotes is also considered as characters so ans will be 15
print ("hello"+" "+"world")

#indexing:positioning of characters
str="Drishti"
c=str[3]
print(c)#s

#slicing
st ="apna college"
print(st[2:5])#mns part come will be: (na ) mns first index is included but sec is not
print(st[0:7])
print(st[0:12])#i wnt whole words
print(st[0:]) #it also means that u wnt to include whole world
print(st[0:len(st)])# len of str does not count from 0 so your whole word will print
print(st[ :12])#it mean u wnt to 0 index also

#in index neg indexing is also done , and it start with -1 ;(-3 , -2 , -1)
x= "apple"
print(x[-4:-1])#-1 is not included 
print(x[ : ]) # apple



