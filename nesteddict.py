#nested dictionary= a sub dictionary in a dictionary

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
print(dict)
print(dict["subjects"]["wad"])
dict["name"]="sachi"
dict["subjects"]["cs"]=99
dict["subjects"]["IT"]=99
print(dict)