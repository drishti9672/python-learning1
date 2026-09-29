#dictionary are used to store values in form key: values
#unorderd , mutable , dont create duplicate key

dict={
    "name": "drishti",
    "subjects": ["maths","python","IT workshop","web application development"],
    "age":19,
    93.5 : 23,
    (1,2,"drishti") : 32 #every data type which is unmutable can be used in place of key


}

print(dict)
print(dict["name"])
print(dict["age"])
print(dict[93.5])
dict["name"]= "Sachi"
dict["Surnmae"]="Sharma"  # yes we can add a new key and value just like we change a value in dictionary
print(dict)

b={} #null dictionary
print(b)
b["name"]="nivedita"
print(b)






