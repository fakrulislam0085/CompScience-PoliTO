'''A tuple is similar to a list, but once created, its contents cannot be
modified (a tuple is an immutable version of a list)'''
#writing style
triple = (5, 10, 15) 
triple2 = 5, 10, 20
print(triple2)


#concatenation
tuple1 = (5, 10, 15) 
tuple2 = 20, 25, 30
tupleFinal = tuple1 + tuple2 
print(tupleFinal)


#multiple assignment
(a, b) = (3, 4) 
(a, b) = (b, a)
print(a)



#returning multiple values from a function using tuple
#function definition
def readDate() :
    print("Enter a Date: ")
    month = int(input("month: "))
    day = int(input("day: "))
    year = int(input("year: "))
    return (year, month, day)      #returns a tuple

'''Function call: assign entire value to a tuple'''
date = readDate()
print(date)

'''Function call: use tuple assignment'''
(year, month, day) = readDate()
print(f"{day}/{month}/{year}")



#the enumerate function
name = 'ciao'
for index, char in enumerate(name) :
    print(index, char)