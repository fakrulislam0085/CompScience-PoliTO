#creating a dictionary 
# A dictionary is a collection which is unordered, changeable and indexed. In Python dictionaries are written with curly brackets, and they have keys and values.
contacts = {"Key1": "value1", "Key2": "value2", "Key3": "value3"}
print(contacts)

#accessing elements of dictionary 
# You can access the items of a dictionary by referring to its key name, inside square brackets:
print(contacts["Key1"]) 

#creating empty dictionary  
mydict = {}
myemptydict = dict() 
print(mydict)
print(myemptydict)

#adding or modifying elements to dictionary
contacts["Key4"] = "value4"
contacts["Key1"] = "value5"
print(contacts)