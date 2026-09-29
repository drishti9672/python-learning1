#String methods
#1=string.ends with()
str1="i am drishti sharma "
print (str1.endswith("rma")) #false=bcz in str 1 there is a gap after rma 
print(str1.endswith("ma "))#true 

#str.capitalize
print(str1.capitalize())
print(str1)#here i is not capatalize bcz the fnctn works only whn u write code
#if u wnt to save capital i in ur str 1 then just save this code like beliow
str1=str1.capitalize()
print(str1)#now i will be capitalise

#st.replace
print(str1.replace("drishti","sachi"))
print(str1.replace("a","o"))

#str.find
print(str1.find("i"))#this fn gives us the index no of first occurence of word, character u give in the code

print(str1.find("drishti"))
print(str1.find("f"))

#str.count
print(str1.count("am"))
print(str1.count("i"))


name=input("enter your name=")
print("hello",name)
print(len(name))


#conditonal statements 
age1=24
age2=18


if(age1==18):
    print("person cannot apply for license")
    print("person cannot vote")
elif(age1>=18):
    print("can vote and can apply for license") 
elif(age1<=18):
    print("can marry")       #when u use elif after if it will ccheck the conditional statements upto the statement is true
      

if(age1==18):
    print("cannot vote and apply for licence")
if(age1<=18):
    print("cannot marry")
if(age1>=18):
    print("can vote")#if u use if statements only every condition wll be checked
else:
    print("person is not born")
#indentation=proper spacing

#example 
marks=int(input("enter your marks="))
if(marks >=90):
    grade="A"
elif(marks >=80 and marks<90):
    grade="B"
elif(marks >=70 and marks<80):
    grade="C"
else:
    grade="D" 
print("your grade =>",grade)

#nesting = condition in a condition
age=95
if(age>=18):
    if(age>=80):
        print("cannot drive")
    else:
        print("can drive")
if(age<18):
    print("cannot drive")


number=int(input("enter a no="))
if(number%2==0): 
    print("even")
else:
    print("odd")
