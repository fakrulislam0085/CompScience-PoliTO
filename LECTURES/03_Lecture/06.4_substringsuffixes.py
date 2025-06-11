'''
s.isalnum(): Returns True if all characters in s are alphanumeric (letters and/or digits) and s is not empty.
s.isalpha(): Returns True if all characters in s are alphabetic (letters only) and s is not empty.
s.isdigit(): Returns True if all characters in s are digits and s is not empty.
s.isspace(): Returns True if all characters in s are whitespace characters (like spaces, tabs, newlines) and s is not empty.
s.islower(): Returns True if all alphabetic characters in s are lowercase and s contains at least one letter.
s.isupper(): Returns True if all alphabetic characters in s are uppercase and s contains at least one letter.
'''

s1 = "Hello123"
s2 = "Hello"
s3 = "12345"
s4 = "   "
s5 = "hello"
s6 = "HELLO"

print(s1.isalnum())   # True - s1 contains only letters and digits
print(s2.isalpha())   # True - s2 contains only letters
print(s3.isdigit())   # True - s3 contains only digits
print(s4.isspace())   # True - s4 contains only whitespace
print(s5.islower())   # True - s5 contains only lowercase letters
print(s6.isupper())   # True - s6 contains only uppercase letters
