contacts = {"key1": "12345", "key2": "67890", "key3": "54321"}

#check if a key is present in dictionary
#check if a value is present in dictionary
if "key1" in contacts.keys():
    print("Yes, 'key1' is one of the keys in the dictionary")

if "12345" in contacts.values():
    print("Yes, '12345' is one of the values in the dictionary")

#using get() method to access the value of a key
if contacts.get("key1"):
    print(contacts.get("key1"))

#using default value in get() method
number = contacts.get("key4", "Missing")
print(number)  #prints "Missing" as key4 is not present in dictionary

#length of dictionary
print(len(contacts))



#removing key-value pair from dictionary
contacts.pop("key1")    #pop() method returns the value of the key that is removed so we can store it
stored_value = contacts.pop("key2")
print(contacts)

del contacts["key3"]   #del keyword also removes the key-value pair from dictionary
print(contacts)

#clearing the dictionary
contacts.clear()    #clear() method removes all the key-value pairs from the dictionary