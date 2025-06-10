'''
Using “+” to concatenate strings is an example of a concept called
operator overloading. The “+” operator performs different functions, depending 
on the types of the involved values:

o integer + integer → integer addition
o float + float → float addition 
o float + integer → float addition
o string + string → string concatenation
o list + list → list concatenation
'''

#Concatenate two strings
first_name = "Fakrul"
last_name = "Islam"
name = first_name + " " + last_name  #string Concatenation 
print(name)



#Remember, strings are immutable in python, so you can not modify a value of an index
#Accessing Characters in a String
greeting = "Buongiorno"
first_char = greeting[0]
last_char = greeting[-1]      #accessing last char
slicing1 = greeting[0 : 4]    #from first to n(here, 4) index
slicing2 = greeting[ : 4]     #from first to n(here, 4) index
slicing3 = greeting[4 : 10]   #from n to n1(here, n=4, n1=10) index
slicing4 = greeting[4 : ]     #from n to last
slicing5 = greeting[ : ]      #make a copy of our string

print(first_char,last_char)
print(slicing1,'\n',slicing2,"\n",slicing3,'\n',slicing4,'\n',slicing5, sep = "")
#we have used sep = "", this function to remove the frontal space from every new line




#string portion
varsity = 'Politecnico Di Torino'
odd_index = varsity[1 :: 2]     #give us only odd index char
even_index = varsity[ :: 2]     #give us only even index char
increment_index = varsity[3: 9 : 2]     #Include all the char from 3 to 9 using an increment of n(here 2) of the index steps
print(f"{odd_index}\n{even_index}\n{increment_index}")



#Find out length of a string
l1 = len(greeting)
l2 = len(name)      #It counts space as an index too
print(l1)
print(l2)



#string repetition
dash = "-" * 50
name = 'Fariha' * 10
letter = 'a' * 5 + " " + 'b' * 5
print(dash)
print(name)
print(letter)
