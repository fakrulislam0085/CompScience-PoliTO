#To check the data type of a variable, we can use type() function

x = 10
name = 'Islam'
a = 52.52
is_jobHolder = False

print(type(x))
print(type(name))
print(type(a))
print(type(is_jobHolder))


#We can convert one types data to another type data
a = "10"        #it is a string
b = int(a)      #now a is a integer
print(type(b))


z = 10      #z is a integer
text = "I have " + str(z) + str(b) + " Oranges"
print(text)