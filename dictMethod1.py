 #dictionary methods
   #  1)dict.keys()  : gives us the collection of keys

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

print(dict.keys())

#if u want that the collection of keys should be printed in form of list   - casting

print(list(dict.keys()))
print(tuple(dict.keys()))

print(len(dict))
print(len(list(dict.keys())))
print(len(dict["subjects"]))


#dict.values() =  gives the collection of values
 
print(dict.values())
print(list(dict.values()))
print(len(list(dict.values())))


#dict.items() = gives us the collection of pairs in form of tuples
 
print(dict.items())
print(tuple(dict.items())) # yha pr sbme brackets ache se delh lio khi ppr me ajaye likna
print(list(dict.items()))
print(len(list(dict.items())))
print(list(dict.items())[1])
list= list(dict.items())#accesing
print(list[1])#accessing
