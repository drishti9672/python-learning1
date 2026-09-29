# dict.get("key")
  
dict={ 
    "name":"drishti",
    "age":19,
    "subjects":{
        "Maths":95,
        "cs":96,
        "wad":98,
    },
     "house":"victory",
 }

print(dict.get("age"))
 #the thng is we can use simple here print(dict["age"]) like
print(dict["age"])
#but we prefer get method more instead of this bcz  if we enter such key which dont exist in dict error will come but if we use get method it will print none instead of giving error

print(dict.get(sum))




#dict.update()
print(dict.update({"city":"delhi"})) #kuch reply me ni deta ye
print(dict)

#or u can also do
newDict={5:6, "rollno": 53}
print(dict.update(newDict))
print(dict)
