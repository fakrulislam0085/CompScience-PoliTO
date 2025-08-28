'''
The 'in' operator checks whether a specific substring is present in a string.
It returns True if the substring is found in the string, and False otherwise.
'''

sentence = "I know C, C++ programming. So now, python is like speaking my mother tongue to me"
print("my" in sentence)     #output true
print("mother" not in sentence)     #output false as we used 'not' operator
print("Ami" in sentence)    #output false
print("kochu" not in sentence)      #output true as we used 'not' operator

if "program" in sentence:
    print("the substring is present in our sentence")


