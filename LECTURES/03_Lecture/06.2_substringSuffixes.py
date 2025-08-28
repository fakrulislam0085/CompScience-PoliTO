'''
s.count("substring") is a string method that counts the occurrences
of a substring within a given string s.
'''
word = "mango, apple, banana, mango, blueberry, apple, jackfruit, mango"

print("Mango count-", word.count("mango"))
print("Apple count-", word.count("apple"))



'''
s.find(substring) is a string method that returns the index of the first occurrence 
of a specified substring within a given string s. If the substring is not found, 
it returns -1.
'''
varsity = "politecnico di torino technology"

print("first index of our substr: ", varsity.find("tec"))
print("first index of our substr: ", varsity.find("fa"))
print("first index of our substr: ", varsity.find("poli"))
